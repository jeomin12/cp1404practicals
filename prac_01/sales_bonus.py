"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
#  Get sales input from the user
sales = float(input("Enter sales: $"))
while sales > 0:
    # Calculating bonus based on sales amount
    if sales < 1000:
        bonus = sales * 0.10  # 10% bonus for sales under $1000
    else:
        bonus = sales * 0.15  # 15% bonus for sales $1000 or over
    print(f"The bonus is {bonus:.0f}")
    sales = float(input("Enter sales: $"))
print("Invalid sales amount")