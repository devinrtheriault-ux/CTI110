# Devin Theriault
# 06/25/2026
# P3HW2
# Salary Calculator

# request employee info
name = input("Enter employee name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly pay rate: "))

# Evaluate overtime
if hours > 40:
    # Calculate Overtime
    overtime_hours = hours - 40
    # Calculate over pay
    overtime_pay = overtime_hours * (rate * 1.5)
    # Calculate salary for regular hours
    regular_pay = 40 * rate
    # Calculate gross pay
    gross_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    regular_pay = hours * rate
    gross_pay = regular_pay

# Display Results
print("----------------------------------")
print("Employee Name:", name)
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<12}')
print("---------------------------------------------------------------")
print(f'{hours:<15}{rate:<12}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<12}')