product={
    "name":"bat",
    "price":2900,
    "quality":"topnotch",
    "rating":4.9
}

print(product)

print(product["name"],product["price"])


product["name"]="MRF Bat"

print(product)

product2=[
    {
    "name":"bat",
    "price":2900,
    "quality":"topnotch",
    "rating":4.9
}
]

for i in product2:
    print(i["name"],i["price"])


