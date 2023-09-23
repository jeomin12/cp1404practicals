# Get number of items input from the user
number_of_items = int(input("Number of items: "))
total_price = 0
# Check whether number of items is less than zero
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price = item_price + total_price
# Check if the total price is above $100 to apply the 10% discount
if total_price > 100:
    discount_price = total_price * 0.9
    print (f"Total price for 3 items is ${discount_price:.2f}")
else:
    print(f"Total price for 3 items is ${total_price:.2f}")


