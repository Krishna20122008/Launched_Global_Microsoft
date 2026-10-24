
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]

categories = ("Electronics", "Accessories", "Gaming")

product_ids = {101, 102, 103, 104, 105}
product_ids.add(106)

product_prices = {
    "Laptop": 45000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Monitor": 8000,
    "Headphones": 2000
}

print("Available Products:", products)
print("Product Categories:", categories)
print("Available Product IDs:", product_ids)
print("Product Prices:", product_prices)

name = input("Enter product name: ")
quantity = int(input("Enter quantity: "))

if name in product_prices:
    price = product_prices[name]
    total = price * quantity

    if total >= 5000:
        discount = total * 0.20
    elif total >= 2000:
        discount = total * 0.10
    elif total >= 1000:
        discount = total * 0.05
    else:
        discount = 0

    final_bill = total - discount

    message = name + " | Quantity: " + str(quantity)
    print("\nProduct Details:", message)
    print("Total Price: Rs.", total)
    print("Discount: Rs.", discount)
    print("Final Bill: Rs.", final_bill)

else:
    print("Product not available.")
