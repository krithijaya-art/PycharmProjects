import array

sales = array.array('i', [120, 150, 180, 200, 170, 190, 210])

last_week_sales = sales[-7:]

top_3_sales = sales[-3:]

ny_sales = sales[:3]

print("Last week's sales:", last_week_sales)
print("Top 3 sales days:", top_3_sales)
print("New York store sales:", ny_sales)
