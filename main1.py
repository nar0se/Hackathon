import os  
from os import system
import customers
from customers import Customer
import operations1
from operations1 import insertcustomer
from operations1 import cardata
import calculations
from calculations import calculatePrice
import sqlOps1
from sqlOps1 import carselection
import decimal
from decimal import Decimal



system('cls')


print('Welcome to the FANDK Dealership. Let us get you in a new car today.')

print("\033[1;31;40m")
print(f'''

                                              _____________
                                  ..---:::::::-----------. ::::;;.
                               .'""""""                  ;;   \  ":.
                            .''                          ;     \   "\__.
                          .'                            ;;      ;   \\";
                        .'                              ;   _____;   \\/
                      .'                               :; ;"     \ ___:'.
                    .'--...........................    : =   ____:"    \ \
               ..-""                               """'  o"""     ;     ; :
          .--""  .----- ..----...    _.-    --.  ..-"     ;       ;     ; ;
       .""_-     "--""-----'""    _-"        .-""         ;        ;    .-.
    .'  .'                      ."         ."              ;       ;   /. |
   /-./'                      ."          /           _..  ;       ;   ;;;|
  :  ;-.______               /       _________==.    /_  \ ;       ;   ;;;;
  ;  / |      """"""""""".---."""""""          :    /" ". |;       ; _; ;;;
 /"-/  |                /   /                  /   /     ;|;      ;-" | ;';
:-  :   """----______  /   /              ____.   .  ."'. ;;   .-"..T"   .
'. "  ___            "":   '""""""""""""""    .   ; ;    ;; ;." ."   '--"
 ",   __ """  ""---... :- - - - - - - - - ' '  ; ;  ;    ;;"  ."
  /. ;  """---___                             ;  ; ;     ;|.""
 :  ":    FANDK   """----.    .-------.       ;   ; ;     ;:
  \  '--_Dealership      \   \        \     /    | ;     ;;
   '-..   """"---___      :   .______..\ __/..-""|  ;   ; ;
       ""--..       """--"                    .   ". . ;
             ""------...                  ..--""      " :
                        """"""""""""""""""    \        /
                                               "------"
                                              
''')
print("\033[1;37;40m")

insertcustomer()

sellergoaway = input('It looks like you are a seller, correct? [Y/N] >> ')
if sellergoaway.upper() == 'Y':
    print('Please visit our sister Dealership that deals with used cars at www.FANDKusedonly.com') 
    exit()
    
cardata()


print("Let's see if you qualify for some discounts")

veteran = input('Are you a Veteran [Y/N] ').upper()

disabled = input('Do you have a disability? [Y/N] ').upper()


counter = 1

total_price = 0
grand_price = 0
while True:
    customerchoice = int(input(f'Please enter id number {counter} [1-22] for the car you would like to purchase >> '))
    if (customerchoice < 1) or (customerchoice > 22):
        print('Invalid choice. Please enter a number between 1 and 22.')
    else:
        counter += 1
    car = sqlOps1.carselection(customerchoice)
    price = car.getCar_price()
    color = car.getCar_color()
    total_price = calculatePrice(color, price, veteran, disabled)
    print(f'After any applicable discount, your total price is ${total_price}')
    finaloption=input('Do you want to purchase another car? [Y/N]')
    if finaloption.upper() == "N":
        break
    if counter == 6:
        break
print('Thanks for visiting our FANDK Dealership. Have a great day!')
