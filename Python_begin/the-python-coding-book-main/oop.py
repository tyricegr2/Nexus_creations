# Object-oriented programming - A merge of storing data using data types and performing actions with the data
"""
items = ["Geb", "Pizza", "Coffee", "Apple Watch"]
cost_items = [10.00, 0.50, 1.00, 83.70]
selling_price = [25.00, 2.50, 3.00, 400.00]
stock = [100000, 50, 100, 500000]

daily_income = 0

# Input items and quantity sold
item_sold = input("Enter item sold: ").title()
quantity = int(input("Enter quantity sold: "))
item_index = items.index(item_sold)

# Work out required values
profit = quantity * (selling_price[item_index] - cost_items[item_index])
daily_income += selling_price[item_index] * quantity

# Update stock
stock[item_index] -= quantity
# TODO: Add check to make sure stock does not go below zero

print(profit)
print(daily_income)
print(stock[item_index])
"""
# Refactoring
# Dictonaries like the one below allow for new items to be added or removed
# Ex (Below) - GEB : [cost of book, selling price, stock] 
items = {
        "GEB" : [10.00, 25.00, 100000],
        "Pizza" : [0.50, 2.50, 50],
        "Coffee" : [1.00, 3.00, 100],
        "Apple Watch" : [83.70, 400.00, 500000],
        }
daily_income = 0

#Input items and quantity sold
def get_sale_info():
    item_sold = input("Enter item sold: ").title()
    quantity = int(input("Enter quantity sold: "))
    return item_sold, quantity

def get_profit(item_sold, quantity):
    profit = quantity * (items[item_sold][1] - items[item_sold][0])
    return profit

def update_income(item_sold, quantity):
    return daily_income + items[item_sold][1] * quantity

#Update the stock

item_sold, quantity = get_sale_info()
profit = get_profit(item_sold, quantity)
daily_income = update_income(item_sold, quantity)
update_stock(item_sold, quantity)

print(profit)
print(daily_income)
print(items[item_sold][2])
