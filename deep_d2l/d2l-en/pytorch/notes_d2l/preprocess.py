# Pandas can be used to store extracted data 

import os

os.makedirs(os.path.join('..', 'data'), exist_ok=True)
data_file = os.path.join('..', 'data', 'house_tiny.csv')
with open(data_file, 'w') as f:
    f.write('''Numrooms, RoofType, Price
NA,NA,127500
2,NA,106000
4,Slate,178100
NA,NA,140000''')

import pandas as pd

data = pd.read_csv(data_file)
print(data)


inputs, targets = data.iloc[:, 0:2], data.iloc[:,2]
inputs = pd.get_dummies(inputs, dummy_na=True)
inputs = inputs.fillna(inputs.mean())
print(inputs)

import torch

X, y = torch.tensor(inputs.values), torch.tensor(targets.values)

print(y)
