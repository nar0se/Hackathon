class Car:  
    def __init__(self, car_id=None, car_make=None, car_model=None, car_year=None, car_color=None, car_price=None):
        self.car_id=car_id
        self.car_make=car_make
        self.car_model=car_model
        self.car_year=car_year
        self.car_color=car_color
        self.car_price=car_price

    def setCar_id(self, car_id):
        self.car_id = car_id
    def getCar_id(self):
        return self.car_id

    def setCar_make(self, car_make):
        self.car_make = car_make
    def getCar_make(self):
        return self.car_make

    def setCar_model(self, car_model):
        self.car_model = car_model
    def getCar_model(self):
        return self.car_model

    def setCar_year(self, car_year):
        self.car_year = car_year
    def getCar_year(self):
        return self.car_year

    def setCar_color(self, car_color):
        self.car_color = car_color
    def getCar_color(self):
        return self.car_color

    def setCar_price(self, car_price):
        self.car_price = car_price
    def getCar_price(self):
        return self.car_price


