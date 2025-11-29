
# Dataset

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



# Part 1 — Extract Unique Items

def get_unique_items(sales):
    return list({record["item"] for record in sales})

unique_items = get_unique_items(sales)
print("Unique Items:", unique_items)



# Part 2 — Total Net Revenue per Item

item_net_revenue = {
    item: sum(
        (record["price"] * record["quantity"]) * (1 - record["discount"])
        for record in sales if record["item"] == item
    )
    for item in unique_items
}

print("Net Revenue per Item:", item_net_revenue)



# Part 3 — Identify High-Performing Items (revenue > 2000)

top_items = [item for item, revenue in item_net_revenue.items() if revenue > 2000]
print("Top Items:", top_items)



# Part 4 — Filter Sales for High-Performing Items

filtered_sales = [record for record in sales if record["item"] in top_items]
print("Filtered Sales:", filtered_sales)


# Part 5 — Total Quantity Sold per Branch

branch_quantities = {
    record["branch"]: sum(r["quantity"] for r in filtered_sales if r["branch"] == record["branch"])
    for record in filtered_sales
}

print("Quantity Sold per Branch:", branch_quantities)


# Part 6 — Most Successful Branch

most_successful_branch = max(branch_quantities, key=branch_quantities.get)
print("Most Successful Branch:", most_successful_branch)
