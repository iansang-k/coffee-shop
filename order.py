class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        # Add this order to customer's and coffee's order lists
        customer._orders.append(self)
        coffee._orders.append(self)

    @property 
    def customer(self):
        return self._customer 
    
    @customer.setter 
    def customer(self, value):
        from customer import Customer
        if not isinstance(value, Customer):
            raise TypeError("Customer must be a Customer instance")
        self._customer = value

    @property 
    def coffee(self):
        return self._coffee 
    
    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        self._coffee = value

    @property 
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if value < 1.0 or value > 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = value

    def __repr__(self):
        return f"<Order customer={self.customer.name} coffee={self.coffee.name} price={self.price}>"