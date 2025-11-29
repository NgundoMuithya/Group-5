sales = [
    {"branch": "Nairobi", "item": "Laptop", "category": "Electronics",
     "price": 780, "quantity": 4, "discount": 0.05, "date": "2025-01-03"},

    {"branch": "Nairobi", "item": "Phone", "category": "Electronics",
     "price": 520, "quantity": 6, "discount": 0.10, "date": "2025-01-03"},

    {"branch": "Mombasa", "item": "Headphones", "category": "Accessories",
     "price": 150, "quantity": 10, "discount": 0.00, "date": "2025-01-04"},

    {"branch": "Nakuru", "item": "Laptop", "category": "Electronics",
     "price": 780, "quantity": 2, "discount": 0.00, "date": "2025-01-04"},

    {"branch": "Nairobi", "item": "Tablet", "category": "Electronics",
     "price": 310, "quantity": 3, "discount": 0.10, "date": "2025-01-05"},

    {"branch": "Mombasa", "item": "Phone", "category": "Electronics",
     "price": 520, "quantity": 4, "discount": 0.00, "date": "2025-01-05"},

    {"branch": "Nakuru", "item": "Keyboard", "category": "Accessories",
     "price": 80, "quantity": 12, "discount": 0.15, "date": "2025-01-05"},

    {"branch": "Nairobi", "item": "Monitor", "category": "Electronics",
     "price": 260, "quantity": 5, "discount": 0.05, "date": "2025-01-06"},

    {"branch": "Mombasa", "item": "Tablet", "category": "Electronics",
     "price": 310, "quantity": 2, "discount": 0.00, "date": "2025-01-06"},
]

# Question 1
items = [sale['item'] for sale in sales]
unique_items = list(set(items))
print(f"Question 1: {unique_items}\n")

# Question 2
item_net_revenue = {item_name: sum( (sale['price'] * sale['quantity'] * (1 - sale['discount'])) for sale in sales if sale['item'] == item_name ) for item_name in unique_items}
print(f"Question 2: {item_net_revenue}\n")

# Question 3
top_items = [item for item, revenue in item_net_revenue.items() if revenue > 2000]
print(f"Question 3: {top_items}\n")

# Question 4
filtered_sales = [sale for sale in sales if sale['item'] in top_items]
print(f"Question 4: {filtered_sales}\n")

# Question 5
branch_total_quantities = {
    branch: sum(s['quantity'] for s in filtered_sales if s['branch'] == branch)
    for branch in {s['branch'] for s in filtered_sales}
}
print(f"Question 5: {branch_total_quantities}\n")

# Question 6
highest_branch = max(branch_total_quantities, key=branch_total_quantities.get)
print(f"Question 6: {highest_branch}")
