# Personal Financial Budgeting script

import csv 
import pandas as pd

# Income Variables
expected_pay = 86100
pot_comms = 17220
investments = 0
monthly_income_salary = 7800

#TODO Verify if variables below should be fixed later on

#Expense Variables
place_to_live = 1160
total_income_tax = 2800
savings = 1900
renters_insurance = 20
car_insurance = 0
utilities = 102 
internet = 50
cell_phone = 0
food = 600
gym = 0
martial_arts = 0
car = 670
entertainment = 62
gas = 200

#TODO Create an input user method here or find a way to make it easy to change this value
extras = 183 

# TODO Potentially change form of income_rows to be similar to expense_rows
Income_rows = [
        {
            "Expected Pay": expected_pay, 
            "Potential Commisions": pot_comms,
            "Investments (Stock, Crypto, Web3, Acorns)" : investments,
            "Monthly Income (Salary)" : monthly_income_salary
        }
    ]


expense_rows = [ ['Place to live', place_to_live, 'Dallas: Infinity on the Mark'],
                 ['Total Income Tax', total_income_tax, 'Yearly Tax of $18,516'],
                 ['Savings', savings, "At least less than 10% of expected monthy salary"],
                 ['Renters Insurance', renters_insurance, "Lemonad $20/month"],
                 ['Car Insurance', car_insurance, "For the next 3-5 months?"],
                 ['Internet/Wi-Fi', internet, "Spectrum: $50/month"],
                 ['Cell Phone Bill', cell_phone, "TODO: Need to transfer from Dad to me"],
                 ['Food/Groceries', food, "Take-out primarily; Groceries secondary"],
                 ['Gym', gym, "Don't currently have a membership"],
                 ['Martial Arts', martial_arts, "Currently doing Cuong Nhu for free"],
                 ['Car', car, "2023 Hyundai Sonata"],
                 ['Entertainment', entertainment],
                 ['Gas', gas, "Average of 2 fill ups per month"],
                 ['Extras', extras, "Updated monthly"] ]

expense_df = pd.DataFrame(expense_rows, columns = ['Expense', 'Cost of Expense', 'Description'])

def add_expenses():
    return expense_df.loc[:,'Cost of Expense'].sum()

def net_profit():
    return monthly_income_salary - add_expenses()

def net_savings():
    return net_profit() + savings

print(add_expenses())
print(net_profit())
print(net_savings())
# with open('current_budget.csv', 'w', encoding='UTF8', newline='') as f:

