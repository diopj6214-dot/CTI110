# Jibreel Diop
# 2/12/26
# P1HW2
# This program calculates and displays travel expenses


# Pseudocode:
# Ask user for their budget
# Ask user for travel destination
# Ask user for gas expense
# Ask user for accommodation expense
# Ask user for food expense
# Add all expenses together
# Subtract total expenses from budget
# Display formatted results

print("This program calculates and displays travel expenses")
print()

#User input
budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")


gas = int(input("How much do you think you will spend on gas?  "))
hotel = int(input("Approximately, how much will you need for accomodation/hotel?  "))
food = int(input("Last, how much do you need for food?  "))


#Caculations
total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses


#Output
print()
print("------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print()
print(f"Fuel: {gas}")
print(f"Accommodation: {hotel}")
print(f"Food: {food}")
print()
print(f"Remaining Balance: {remaining_balance}")