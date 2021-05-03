class Customer:  
    def __init__(self, customer_type=None, customer_firstname=None, customer_lastname=None, customer_age=None, customer_phone=None, customer_veteran=None, customer_disabled=None):
        self.customer_type=customer_type
        self.customer_firstname=customer_firstname
        self.customer_lastname=customer_lastname
        self.customer_age=customer_age
        self.customer_phone=customer_phone
        self.customer_veteran=customer_veteran
        self.customer_disabled=customer_disabled

    def setCustomerType(self, customer_type):
        self.customer_type = customer_type
    def getCustomerType(self):
        return self.customer_type

    def setcustomer_firstname(self, customer_firstname):
        self.customer_firstname = customer_firstname
    def getcustomer_firstname(self):
        return self.customer_firstname

    def setcustomer_lastname(self, customer_lastname):
        self.customer_lastname = customer_lastname
    def getcustomer_lastname(self):
        return self.customer_lastname

    def setcustomer_age(self, customer_age):
        self.customer_age = customer_age
    def getcustomer_age(self):
        return self.customer_age

    def setcustomer_phone(self, customer_phone):
        self.customer_phone = customer_phone
    def getcustomer_phone(self):
        return self.customer_phone

    def setcustomer_veteran(self, customer_veteran):
        self.customer_veteran = customer_veteran
    def getcustomer_veteran(self):
        return self.customer_veteran

    def setcustomer_disabled(self, customer_disabled):
        self.customer_disabled = customer_disabled
    def getcustomer_disabled(self):
        return self.customer_disabled