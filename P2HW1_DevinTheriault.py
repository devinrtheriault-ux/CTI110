# Devin Theriault
# 06/18/2026
# P2HW1
# String Formatting

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

print(f'{"Location:":<18} {destination}')
print(f'{"Initial Budget:":<18} ${budget:.2f}')
print(f'{"Fuel:":<18} ${gas:.2f}')
print(f'{"Accomodation:":<18} ${accom_hotel:.2f}')
print(f'{"Food:":<18} ${food:.2f}')

print("-" * 30)
print()

print(f'{"Remaining Balance:":<16} ${expense_result:.2f}')
