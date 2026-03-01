import numpy as np


data = np.loadtxt("amazon_data.csv", delimiter=",", skiprows=1, usecols=(1, 2, 3))


sales = data[:, 0]
customers = data[:, 1]
orders = data[:, 2]

total_sales = np.sum(sales)
avg_sales = np.mean(sales)
max_sales = np.max(sales)
min_sales = np.min(sales)

total_customers = np.sum(customers)
avg_customers = np.mean(customers)

total_orders = np.sum(orders)
avg_orders = np.mean(orders)


print("Yearly Data Analysis")
print("----------------------------")
print(f"Total Yearly Sales: ${total_sales:,.2f}")
print(f"Average Monthly Sales: ${avg_sales:,.2f}")
print(f"Highest Sales in a Month: ${max_sales:,.2f}")
print(f"Lowest Sales in a Month: ${min_sales:,.2f}")
print()
print(f"Total Registered Customers: {int(total_customers):,}")
print(f"Average Customers per Entry: {int(avg_customers):,}")
print()
print(f"Total Orders: {int(total_orders):,}")
print(f"Average Orders per Entry: {int(avg_orders):,}")
