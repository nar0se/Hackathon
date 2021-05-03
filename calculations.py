import os
from os import system
from decimal import Decimal

system('cls')

def calculatePrice(color, price, veteran, disabled):
    print(f'The price for your car is ${price}')
    total_price = price
    if (color == 'black'):
        total_price = total_price * Decimal(.75)
    # 25% discount for the color black
    if (color == 'white'):
        total_price = total_price - 400
    # $400 rebate for the color white
    if ((veteran == 'Y') or (disabled == 'Y')):
        total_price = (total_price * Decimal(.75)) - 500
    # 25% + $500 rebate for veteran or disabled status
    total_price *= Decimal(1.05)
    # taxes
    return round(total_price, 2)
    # total rounded to two decimals


    
    
