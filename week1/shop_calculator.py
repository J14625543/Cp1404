DISCOUNT_THRESHOLD = 100.0
DISCOUNT_RATE = 0.9

total_price = 0.0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid input")
    number_of_items = int(input("Number of items: "))

for i in range(1, number_of_items + 1):
    price_per_item = float(input("Price of item: "))
    total_price += price_per_item

if total_price >= DISCOUNT_THRESHOLD:
    total_price *= DISCOUNT_RATE

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
