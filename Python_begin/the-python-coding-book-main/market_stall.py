# market_stall.py
# Function definitions thats a member within a class is callled a method
class Product:
    # init method: Tells the program how to intialize the class (Product) when I create one
    # import market_stall -> market_stall.Product() -> market_stall.Product().name = "GEB"
    def __init__(self, product_name, cost, sell_price, n_stock):
        self.name = product_name
        self.cost_price = cost
        self.selling_price = sell_price
        self.number_in_stock = n_stock
    
    # self.name is an instance variable - a.k.a data attributes
    # self.decrease_stock() is a method
    def decrease_stock(self, quantity):
        self.number_in_stock -= quantity

    def change_cost_price(self, new_price):
        self.cost_price = new_price

    def change_selling_price(self, new_price):
        self.selling_price = new_price

    def show_stock(self):
        print(f"{self.name} | Number in stock: {self.number_in_stock}")

class CashRegister:
    def __init__(self):
        self.income = 0
        self.profit = 0
        self.cash_available = 100
    
    # item: Product is an example of type hinting
    def register_sale(self, item: Product, quantity: int):
        sale_amount = quantity * item.selling_price
        self.income += sale_amount
        self.cash_available += sale_amount
        self.profit += quantity * (item.selling_price - item.cost_price)
        item.decrease_stock(quantity)




# TODO: Create a class for coffee with the different configuration of coffees

