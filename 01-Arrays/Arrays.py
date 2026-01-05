"""
Topic: Python Array Basics
Purpose: Understanding array module and NumPy arrays
Note: For DSA problem-solving, Python lists are preferred.
"""

import array
import numpy as np

# Integer array
val = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

# Double (float) array
val2 = array.array('d', [1, 2, 3, 4, 5, 6, 7, 8, 9])

# Unicode character array
val3 = array.array('u', ['a', 'b', 'c', 'd'])

# Accessing elements using index
for i in range(6):
    print(val[i], end=" ")

print()

# Iterating directly
for x in val:
    print(x, end=",")

print("\n")

print("Float array:", val2)
print("Char array:", val3)

# Array properties
print("Typecode:", val.typecode)

# Reverse array
val.reverse()
print("Reversed:", val)

# Insert, append, update
val.insert(1, 25)
val.append(100)
val[2] = 200  # overwrites value at index 2

# Copy array
copy_array = array.array(val.typecode, (x for x in val))
print("Updated array:", val)

# NumPy arrays
np_array = np.array([1, 2, 3, 4])
print("NumPy array:", np_array)

np_linspace = np.linspace(10, 20, 10)
print("NumPy linspace:", np_linspace)
