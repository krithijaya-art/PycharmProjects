nested_dict = {
    "key1": {
        "sub_key1": "value1",
        "sub_key2": "value2"
    },
    "key2": {
        "sub_key3": "value3",
        "sub_key4": "value4"
    }
}

# Accessing a value
value = nested_dict["key1"]["sub_key1"]

# Updating a value
nested_dict["key2"]["sub_key3"] = "new_value"

# Adding a new sub-dictionary
nested_dict["key3"] = {
    "sub_key5": "value5",
    "sub_key6": "value6"
}
-----------------------------------------------

amazon_inventory = {
    "Electronics": {
        "Mobile": {"Price": 500, "Stock": 30, "Rating": 4.5},
        "Laptop": {"Price": 800, "Stock": 15, "Rating": 4.7}
    },
    "Clothing": {
        "Shirt": {"Price": 5, "Stock": 50, "Size": ["S", "M", "L"]},
        "Jeans": {"Price": 6, "Stock": 40, "Size": ["M", "L", "XL"]}
    },
    "Books": {
        "Novel": {"Price": 1, "Stock": 100, "Author": "John Smith"},
        "Textbook": {"Price": 2, "Stock": 20, "Author": "Dr. Brown"}
    }
}


print("Mobile Price:", amazon_inventory["Electronics"]["Mobile"]["Price"])


amazon_inventory["Clothing"]["Shirt"]["Stock"] -= 5


amazon_inventory["Electronics"]["Tablet"] = {"Price": 300, "Stock": 25, "Rating": 4.3}


print(amazon_inventory)
