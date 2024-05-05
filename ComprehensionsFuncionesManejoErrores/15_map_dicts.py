product = [
    {"product": "camisa", "price": 100},
    {"product": "pantalones", "price": 300},
    {"product": "gorra", "price": 50},
]
""" 
prices = []
for p in product:
    prices.append(p["price"])


print(prices)

 """
prices = list(map(lambda item: item["price"], product))
print(prices)


def add_taxes(item):
    item["taxes"] = item["price"] * 0.19
    return item


new_items = list(map(add_taxes, product))
print(new_items)
print(product)
