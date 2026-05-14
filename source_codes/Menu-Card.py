# menu list of food items
menu = {
    'Pizza' : 130,
    'Pasta' : 80,
    'Noodles' : 70,
    'Thali' : 120,
}

# counter to manage the order list
order_count = 0

# welcome message and menu card
print("\033[1m""---- Welcome to Our Restaurant ----""\033[0m")
for key,value in menu.items():
    print(f"{key} : {value}")

# asking user for order
order_1 = input("Your First order plz: ")
if order_1 in menu:
    order_count += menu[order_1]
    print(f"Your order {order_1} has been placed")
else:
    print("we are unavailable to provide you with this order")

# asking for another order
while True:
    another = input("Do you want another order (Yes/No):")
    if 'Yes' == another:
        order_2 = input("Your next order plz: ")
        if order_2 in menu:
            order_count += menu[order_2]
            print(f"Your order {order_2} has been placed")
        else:
            print("we are unavailable to provide you with this order")
    elif 'No'== another:
        break

print(f"The total amount to be paid {order_count}")