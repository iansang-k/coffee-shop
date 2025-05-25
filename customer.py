from order import Order

class Customer:
    all = []

    def __init__(self, name):
        self._orders = []
        self.name = name
        self.__class__.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 1:
            raise ValueError("Customer name cannot be empty")
        if len(value) > 15:
            raise ValueError("Customer name cannot exceed 15 characters")
        self._name = value
        
    def orders(self):
        return self._orders
    
    def coffees(self):
        return list(set(order.coffee for order in self._orders))
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order

    def __repr__(self):
        return f"<Customer name={self.name}>"
    
    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders():
            return None
        
        spending = {}

        for order in coffee.orders():
            if order.customer not in spending:
                spending[order.customer] = 0
            spending[order.customer] += order.price
        return max(spending.items(), key=lambda item: item[1])[0]