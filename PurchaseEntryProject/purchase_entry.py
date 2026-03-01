
customer_details = {
    "name": "John Wick",
    "email": "johnwick@example.com",
    "loyalty_card": "12345ABC"
}


purchase_history = {
    "favorite_coffee": "Caramel Macchiato",
    "visits_per_month": 5,
    "total_spent": 150
}

#customer_profile = {**customer_details, **purchase_history}

customer_profile = customer_details.copy()
customer_profile.update(purchase_history)

print(customer_profile)

customer_profile = customer_details.copy()
customer_profile.update(purchase_history)