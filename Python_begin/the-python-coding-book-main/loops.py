for pizza_with_cheese in range(8):
    print("Box" ,pizza_with_cheese+1)


for DRY in range(10):
    # f-string: formatted string, don't forget the curly brackets.
    # - Will replace curly brackets with a number relative to the instance in the loop
    print(f"{DRY + 1}. Don't Repeat Yourself")

import random

num = 0

while num <= 20:
    # Be sure to important libraries before initializion
    num = random.randint(1, 25)
    print(f"This is a random number: {num}")

print("You have found a number larger than 20")

X = random.randint(1,10)

if X == 2:
    print(f"a is indeed {X}. YAYYY!!")
print("We out")

a = random.randint(1,20)
b = random.randint(1,20)

if a > 10: 
    print("a is a fairly large number")
    if b > 10:
        print("b is also a large number")
