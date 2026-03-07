# Import the built-in array module
# This allows us to create arrays that store elements of the same data type efficiently
import array

# Create an array of floating-point numbers ('f' means 32-bit float)
# These represent temperature readings for different months
temperatures = array.array('f', [29.5, 30.0, 28.7, 31.2, 32.0, 29.8])

# Print the complete array of temperature readings
print("All temperatures:", temperatures)

# Use slicing to extract the first three temperature readings
# [:3] means start from index 0 up to (but not including) index 3
first_three_readings = temperatures[:3]

# Access the last recorded temperature using negative indexing
# [-1] always refers to the last element in a sequence
last_recorded_temperature = temperatures[-1]

# Print the first three readings
print("First 3 readings:", first_three_readings)

# Print the last recorded temperature
print("Last recorded temperature:", last_recorded_temperature)