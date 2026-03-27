
# Supermarket Billing System 

products = {
    1: ("Rice", 60),
    2: ("Sugar", 45),
    3: ("Milk", 33),
    4: ("Bread", 25),
    5: ("Eggs", 6)
}

TAX = 0.12

print("===== Welcome to MORE Supermarket =====")
customer = input("Enter Customer Name: ")

cart = {}
subtotal = 0

while True:
    print("\nAvailable Products:")
    for key, value in products.items():
        print(key, "-", value[0], "₹", value[1])

    print("6 - Exit")

    choice = int(input("Select product number: "))

    if choice == 6:
        break

    if choice in products:
        quantity = input("Enter quantity: ")

        if not quantity.isdigit():
            print("Invalid quantity! Try again.")
            continue

        quantity = int(quantity)
        name, price = products[choice]

        total_price = price * quantity
        subtotal += total_price

        if name in cart:
            cart[name] += quantity
        else:
            cart[name] = quantity

        print(f"{name} added successfully!")
    else:
        print("Invalid choice!")


tax_amount = subtotal * TAX
grand_total = subtotal + tax_amount

print("\n========== RECEIPT ==========")
print("MORE Supermarket")
print("Location: NARSAPURAM")
print("Customer:", customer)
print("------------------------------")

for item, qty in cart.items():
    print(f"{item} x{qty}")

print("------------------------------")
print("Subtotal:", subtotal)
print("Tax (12%):", tax_amount)
print("Grand Total:", grand_total)
print("------------------------------")
from datetime import datetime
print(datetime.now())
print("Thank you! Visit Again!")


