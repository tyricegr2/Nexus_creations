items = {'Coffee': 4, 'Tea': 2, 'Chocolate': 3}

income = 0
for item in items.keys():    
    qty = input(f"How much {item}s have you sold? ")
    qty = int(qty)
    income = income + qty * items[item]
    print(income)
print(f"\nThe income today was ${income:0.2f}")
