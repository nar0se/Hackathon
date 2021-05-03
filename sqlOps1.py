import os
from os import system
import connection1 as c
from mysql.connector import connect
from car import Car

system('cls')

# Defines user info and prints rows from Dbeaver

def readUserInfo():
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM customers')
        for row in cursor:
            print(f'''
            id .............. {row[0]}
            Customer ........ {row[1]}   
            First Name ...... {row[2]}   
            Last Name ....... {row[3]}
            Age.............. {row[4]}
            Phone ........... {row[5]}
            Veteran ......... {row[6]} 
            Disabled ........ {row[7]}         
            ''')
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)

# This is another field being implemented from Dbeaver

def insertCustomerInfo(customer):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO customers (customer_type, customer_firstname, customer_lastname, customer_age, customer_phone, customer_veteran, customer_disabled) VALUES ('{customer.getCustomerType()}', '{customer.getcustomer_firstname()}', '{customer.getcustomer_lastname()}', {customer.getcustomer_age()}, '{customer.getcustomer_phone()}', '{customer.getcustomer_veteran()}', '{customer.getcustomer_disabled()}')")
        conn.commit()
        readUserInfo()
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)  

# This another field from Dbeaver that brings carselections from the table products

def carselection(customerchoice):
    conn = c.returnConnection()
    selectacar = Car()
    try: 
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM products WHERE car_id = {customerchoice}")
        for row in cursor:
            selectacar.setCar_id(row[0])
            selectacar.setCar_make(row[1])
            selectacar.setCar_model(row[2])
            selectacar.setCar_year(row[3])
            selectacar.setCar_color(row[4])
            selectacar.setCar_price(row[5])
        conn.commit()
        cursor.close() 
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error) 
    return selectacar
    



