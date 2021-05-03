
import os
from os import system
from car import Car
import sqlOps1 as sql 
from mysql.connector import connect
import connection1 as c
from customers import Customer
system('cls')

fields = ['customer_type', 'First Name', 'Last Name', 'Age', 'Phone', 'Veteran', 'Disabled'] 

def insertcustomer():
    customer = Customer()
    typeSelection = int(input('Are you a buyer or a seller? Enter 1 for buyer and 2 for seller >> '))
    if typeSelection == 1:
        customerType = 'buyer'
    elif typeSelection == 2:
        customerType = 'seller'
    else:
        print('Invalid Customer Type Selection')
    customer.setCustomerType(customerType)
    fname = input('What is your first name? >> ')
    customer.setcustomer_firstname(fname)
    lname = input('What is your last name? >> ')
    customer.setcustomer_lastname(lname)
    age = int(input('What is your age? >> '))
    customer.setcustomer_age(age)
    phone = input('What is your phone? >> ')
    customer.setcustomer_phone(phone)
    print()
  

def cardata():
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products')
        print('This is our inventory:')
        for row in cursor:
            print(f'''
                car_id: {row[0]}
                car_make: {row[1]}
                car_model: {row[2]} 
                car-year: {row[3]} 
                car_color: {row[4]} 
                car_price: ${row[5]}
            -------------------------------------------------------
            ''')
        cursor.close() 
        conn.close() 
    except(Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySQL', error)
