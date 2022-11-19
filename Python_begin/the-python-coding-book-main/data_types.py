# STrings are immutable data types = cant be changed once the string is created
# Lists are mutable = flexible containers that can change
# Sequences = data type with ordered items in it
# iterable = can go through items in data type one after the other
# Method = function specific to a data type and associated with it like .append()

num_int = 5
num_float = 3.344
name = "Tyrice"

numbers = [2,34,5,3]
more_numbers = range(20)

print(type(num_int))
print(type(more_numbers))
print(more_numbers)

#for item in name:
 #   print(item)

numbers[3] = 7
numbers.append(321221)
numbers.pop(0) # Removes first item

name.replace("r","x")

print(numbers)
print(name.upper())

# Data Structures: Tuples and Dictionaries\

# Tuples utilize parantheses isntead of square brackets
# Tuples like strings are immuatable. Cant change values inside
#   Using tuples when I know the data would not change means less likely for bugs to occur
num_tup = (1, 1, 2, 3, 5, 8, 13, 21)
num_lists = [1, 1, 2, 3, 5, 8, 13, 21]

print(type(num_tup))

# Dictionaries
    # Not sequences
    # Dict. are mutable
student_names = ["Nirvana", "Eros", "X", "Uzar", "Socrates"]
test_results = [110, 80, 200, 90, 150]
# Dictionary of Students and grades
# First part of item is the key, 2nd part is the value
student_marks = {"Nirvana": 110, "Eros": 80, "X": 200, "Uzar": 90, "Socrates": 150}
print(type(student_marks))
print(student_marks["Nirvana"])

student_marks["Marcus"] = 100
print(student_marks)
print(student_marks.keys())
print(student_marks.values())


