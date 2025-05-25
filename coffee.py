class Coffee:
    def __init__(self, name):
        self._orders = []
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Expected string for coffee name, got {type(value).__name__}")
        value = value.strip()
        if len(value) < 3:
            raise ValueError(f"Coffee name must be >= 3 characters, got {len(value)}")
        self._name = value
    
    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0 
        total = sum(order.price for order in self._orders) 
        return total / len(self._orders)

    def __repr__(self):
        return f"<Coffee name={self.name}>"