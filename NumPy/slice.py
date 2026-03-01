import numpy as np

# Create a 2D array (like a small table with rows and columns)
sales = np.array([
    [100, 150, 200],
    [80, 120, 160],
    [90, 110, 140],
    [70, 100, 130]
])

# Accessing a specific data value (row 1, column 2)
value = sales[1, 2]
print("Value at row 1, column 2:", value)

# Slicing rows 0 to 2 and columns 1 to 2
slice_part = sales[0:3, 1:3]
print("Sliced subarray (rows 0 to 2, columns 1 to 2):")
print(slice_part)
