# Devin Theriault
# 07/14/2026
# P5LAB
# Using user-defined functions

import random

def disperse_change(change):
    # Convert value to an integer.
    change = round(change * 100)


    # Determine how many coins are needed.
    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickels = change // 5
    change = change - (num_nickels * 5)

    num_pennies = change

    # If and else statements

    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} Dollar")
        else:
            print(f"{num_dollars} Dollars")

    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} quarter")
        else:
            print(f"{num_quarters} quarters")

    if num_dimes > 0:
        if num_dimes == 1:
            print(f"{num_dimes} Dime")
        else:
            print(f"{num_dimes} Dimes")

    if num_nickels > 0:
        if num_nickels == 1:
            print(f"{num_nickels} nickel")
        else:
            print(f"{num_nickels} nickels")

    if num_pennies > 0:
        if num_pennies == 1:
            print(f"{num_pennies} penny")
        else:
            print(f"{num_pennies} pennies")

    

def main():
    # Logic goes here

    # Generate the amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed:.2f}")

    # Create variable to represent money put into machine
    money_in = float(input("How much cash will you put in the self-checkout? "))

    # Calculate change owed to the customer
    change = money_in - amount_owed
    print(f"Change owed: ${change:.2f}")

    # Call the disperse_change function
    disperse_change(change)
    


# Call the main function
main()
