# Numerical Python for Quantitative Applications
# Numpy introduces data type (ndarray)
# 
import random as alias_random
import numpy as np # Or any other alias besides np

marks = [34, 42, 22, 43, 50, 47]
marks = np.array(marks)

# Below method is the same with +, -, /, etc.
new_marks = []
for mark in marks:
    new_marks.append(mark * 2)

# print(new_marks)

# OR


final_marks = [test_mark / 2 for test_mark in marks]

# print(final_marks)a

np_marks = marks * 2
#print(np_marks)

numbers_a = np.array([[2,3,4,5,6], [1,2,32,3,34], [1,2,3,5,8]])
numbers_b = np.array([7,10,14,15,24])

print(numbers_a)
# print(numbers_b)
# print(numbers_a + numbers_b)

print(alias_random.randint(0,10))
print(numbers_a.shape)
print(numbers_a[1,2])
print(numbers_a[0:2, :2])

# range(1_000_000) = range(1,000,000)
temperatures = [alias_random.randint(-100, 350) / 10 for _ in range(1_000_000)] 

#print(temperatures[0:10])

def convert_loop(temp_C):
    result = []
    for temperature in temp_C:
        result.append(temperature * 1.8 + 32)
    return result

def convert_comp(temp_c):
    result = [temperature * 1.8 + 32 for temperature in temp_c]
    return result

def convert_numpy(temp_c):
    return np.array(temp_c) * 1.8 + 32

#print(temperatures[:10]) # [0:10]
print(convert_loop(temperatures) == convert_comp(temperatures) == convert_numpy(temperatures))

# TO see how long code takes to run, use timeit

import timeit
#print(timeit.timeit("a=5", number=1_000_000))

print('\nUsing "Classic" Method with for loop and list:')
print(timeit.timeit("convert_loop(temperatures)", number=100, globals=globals()))

# List comprehension are more efficient than the for loop method
print("\nUsing a List comprehension")
print(timeit.timeit("convert_comp(temperatures)", number=100, globals=globals()))

print("\nUsing Numpy:")
print(timeit.timeit("convert_numpy(temperatures)", number=100,globals=globals()))
