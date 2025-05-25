# Coffee Shop

This is a simple Python project that uses Object-Oriented Programming to model a coffee shop system. It allows customers to order different coffees, and tracks their orders and spending.

---

## How It Works

- **Customer** : Has a name and can place orders.
- **Coffee** : Has a name and can be ordered by customers.
- **Order** : Connects a customer and a coffee with a price.

---

## Features

- Customers can place multiple orders.
- Orders record which customer and coffee, along with a price.
- Coffees can return all customers who ordered them.
- Average price for a coffee can be calculated.
- Validation for names and prices is included.

---

## Relationships

- One Customer → Many Orders
- One Coffee → Many Orders
- Many Customers ↔ Many Coffees (through Orders)

---


