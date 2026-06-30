# Devin Theriault
# 06/30/2026
# P4LAB2
# Use while and for loops

'''
Get Integer from user
Determine if integer is positive or negative
if number is postive, display multiplication table
if number is negative, tell user program cannot accept it
Ask user to run again?
if yes, run program
if no, end program
'''

run_again = 'yes'

while run_again != "no":

    # Get integer from user
    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        # display multiplication for that value and range (1-12)
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else: 
        print("This program does not handle negative values:")
    
    run_again = input("Would you like to run the program again? ")

# User entered no, loop has ended
print("Program is ending....")