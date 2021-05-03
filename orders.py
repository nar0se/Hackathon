class Order:  
    def __init__(self, order_id=None, order_price=None, order_quantity=None, order_make=None, order_model=None, order_color=None, order_year=None, order_customername=None, order_customertype=None, order_discount=None):
        self.order_id=order_id
        self.order_price=order_price
        self.order_quantity=order_quantity
        self.order_make=order_make
        self.order_model=order_model
        self.order_color=order_color
        self.order_year=order_year
        self.order_customername=order_customername
        self.order_customertype=order_customertype
        self.order_discount=order_discount

    def setOrder_id(self, order_id):
        self.order_id = order_id
    def getOrder_id(self):
        return self.order_id

    def setOrder_price(self, order_price):
        self.order_price = order_price
    def getOrder_price(self):
        return self.order_price

    def setOrder_quantity(self, order_quantity):
        self.order_quantity = order_quantity
    def getOrder_quantity(self):
        return self.order_quantity

    def setOrder_make(self, order_make):
        self.order_make = order_make
    def getOrder_make(self):
        return self.order_make

    def setOrder_model(self, order_model):
        self.order_model = order_model
    def getOrder_model(self):
        return self.order_model

    def setOrder_color(self, order_color):
        self.order_color = order_color
    def getOrder_color(self):
        return self.order_color

    def setOrder_year(self, order_year):
        self.order_year = order_year
    def getOrder_year(self):
        return self.order_year

    def setOrder_customername(self, order_customername):
        self.order_customername = order_customername
    def getOrder_customername(self):
        return self.order_customername

    def setOrder_customertype(self, order_customertype):
        self.order_customertype= order_customertype
    def getOrder_customertype(self):
        return self.order_customertype

    def setOrder_discount(self, order_discount):
        self.order_discount = order_discount
    def getOrder_discount(self):
        return self.order_discount
