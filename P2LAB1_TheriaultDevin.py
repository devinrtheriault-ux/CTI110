# Devin Theriault
# 06/16/2026
# P2LAB1
# Program will calculate the diameter, circumference, and area of a circle

#Import math codule to use the constant, math.pi
import math

#Get radius from user
radius = float(input("What is the radius of the circle? "))
print()

#Calculate diameter
diameter = 2 * radius

#Display diameter with one decimal point
print(f"The diameter of the circle is {diameter:.1f}\n")

#Calculate circumference
circumference = 2 * math.pi * radius

#Display circumference with two decimal places
print(f"The circumference of the circle is {circumference:.2f}\n")

#Calculate the area
area = math.pi * radius**2

#Display area with three decimal places
print(f"The area of the circle is {area:.3f}")