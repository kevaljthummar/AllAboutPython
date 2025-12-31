items = [
        {"name": "Notebook", "price": 250, "category": "Stationery"},
        {"name": "Pen", "price": 100, "category": "Stationery"},
        {"name": "Bag", "price": 1200, "category": "Accessories"},
        {"name": "Bottle", "price": 400, "category": "Utensils"},
    ]
    
# Write your code below this line
name_list = [item["name"] for item in items if item["price"] < 500]
uniq_categories = {item["category"] for item in items}
name_price_mapping = {item["name"]:item["price"] for item in items}
discounted_prices = list(int(item["price"] * 0.90) for item in items)

print(name_list)
print(uniq_categories)
print(name_price_mapping)
print(discounted_prices)