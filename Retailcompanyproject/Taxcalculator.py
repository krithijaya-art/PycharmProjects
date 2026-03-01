# Retail shop details

# Step 1: product name, base price & tax rate
product_name = "Meera shampoo"
base_price = 120
TAX = 5

# Step 2: Calculate final price after tax
tax_rate = float(base_price * TAX/100)
final_price = float(base_price + tax_rate)

# Step 3: Display in the clear format
print (f"The product name is {product_name}")
print (f"The base price of {product_name} is {base_price}")
print (f"The final price with {TAX}% tax included is {final_price}")