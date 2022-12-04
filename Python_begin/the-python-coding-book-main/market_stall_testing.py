# market_stall_testing.py
# Dont have to do market_stall.Product() if Product is important from market_stall
from market_stall import Product, CashRegister

# Class is created and therefore a data type is created to meet my specific need
first_prod = Product("Coffee", 1.1, 2.5, 30)
second_prod = Product("Tea", 0.5, 1.75, 60)

#type(first_prod.name) = <class 'market_stall.Product'>

first_prod.show_stock()
second_prod.show_stock()
# Two arguments passed through decrease_stock: first_prod, 10 (self, quantity)
first_prod.decrease_stock(10)
second_prod.decrease_stock(1)

print()
first_prod.show_stock()
second_prod.show_stock()

till = CashRegister()
print(till.income)
print(till.profit)
print(till.cash_available)

till.register_sale(first_prod, 10)
print()

print(till.income)
print(till.profit)
print(till.cash_available)
first_prod.show_stock()
