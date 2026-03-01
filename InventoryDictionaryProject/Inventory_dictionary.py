walmart_inventory = {}


walmart_inventory[1001] = {"name": "Smartphone", "price": 299.99, "stock": 50}
print("After adding new product:", walmart_inventory)


walmart_inventory[1001]["price"] = 279.99
walmart_inventory[1001]["stock"] = 45
print("After updating product:", walmart_inventory)


removed_product = walmart_inventory.pop(1001)
print("Removed product:", removed_product)
print("Final inventory:", walmart_inventory)
