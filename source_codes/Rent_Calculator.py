# Inputs we need to calculate
rent = int(input("Enter the amount of rent: "))
food_ordered = int(input("Enter total amount of food ordered: "))
electricity_units = int(input("Enter total unit of electricity: "))
charges_per_Unit = int(input("Enter the charge per unit amount: "))
persons = int(input("Enter no. of persons in the room: "))

# electricity charges calculation
totall_electricity_amount = electricity_units + charges_per_Unit

# calculation
total_output = (rent + food_ordered + totall_electricity_amount) // persons

# Output
print(f"Each person will pay: {total_output}")