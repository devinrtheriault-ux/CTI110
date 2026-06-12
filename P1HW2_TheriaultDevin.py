# Devin Theriault
# 06/12/2026
# P1HW2
# Budget/ Travel Expenses

# Introduction
print("This program calculates and displays travel expenses")
print()

# Inputs
budget = int(input("Enter budget: "))
print()
destination = (input("Enter your travel destination: "))
print()
gas = int(input("How much do you think you will spend on gas?: "))
print()
accom_hotel = int(input("Approximately, how much will you need for accomodation/hotel?: "))
print()
food = int(input("Last, how much do you need for food?: "))
print()

# Calculations
expenses = gas + accom_hotel + food
expense_result = budget - expenses

# Display Results
print("--------Travel Expenses--------")
print("Location:", destination)
print("Initial Budget:", budget)
print()

print("Fuel:", gas)
print("Accomodation:", accom_hotel)
print("Food:", food)
print()

print("Remaining Balance:", expense_result)

