# Devin Theriault
# 06/19/2026
# P2HW2
# Grading Program

# Input the grades
# Program groups them up and runs calculations
# Program then displays the calculations in an easy to read manner.

#Collect Grades 
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

#Group the modules and calculate
grades = [module1, module2, module3, module4, module5, module6]

lowest = min(grades)
highest = max(grades)
total_sum = sum(grades)
average = total_sum / 6

#Display results
print("\n------------Results------------")
print(f'{"Lowest Grade:":<18} {lowest:.2f}')
print(f'{"Highest Grade:":<18} {highest:.2f}')
print(f'{"Sum of Grades:":<18} {total_sum:.2f}')
print(f'{"Average:":<18} {average:.2f}')
print("-" * 35)

