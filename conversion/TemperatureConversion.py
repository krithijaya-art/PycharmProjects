#Temperature conversion program

# Step 1 : Input Temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Step 2: Convert Celsius to Farenheit
farenheit = (celsius * 1.8) + 32
print(f"Temperature in Farenheit is: {farenheit:.2f}°F")

# Step 3: Input Temperature in Farenheit
farenheit = float(input("\nEnter temperature in Farenheit: "))

#Step 4: Convert Farenheit to Celsius
celsius = (farenheit - 32) * 5 / 9
print(f"Temperature in Celsius is: {celsius:.2f}°C")
