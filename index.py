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

items = [sale['item'] for sale in sales]
unique_items = list(set(items))
print(unique_items)
item_net_revenue = {item_name: sum( (sale['price'] * sale['quantity'] * (1 - sale['discount'])) for sale in sales if sale['item'] == item_name ) for item_name in unique_items}

top_items = [item for item, revenue in item_net_revenue.items() if revenue > 2000]
print(top_items)
# Calculate net revenue for each item and identify those with revenue > 2000
filtered_sales = [sale for sale in sales if sale['item'] in top_items]
print(filtered_sales)
branch_total_quantities = {
    branch: sum(s['quantity'] for s in filtered_sales if s['branch'] == branch)
    for branch in {s['branch'] for s in filtered_sales}
}

branch_quantities = list(branch_total_quantities.values())
print(branch_quantities)