# Devin Theriault
# 06/18/2026
# P2LAB2
# Usage of dictionary

# Dictionary containing vehicles and their MPG.
vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = vehicle_mpg.keys()

#Display Key
print(keys)
print()

# Ask user to enter vehicle name
vehicle = input("Enter a vehicle to see it's mpg:")
if vehicle in vehicle_mpg:
    mpg = vehicle_mpg[vehicle]
print()

# Display vehicle's MPG
print(f"The {vehicle} gets {mpg} mpg.\n")

# Ask user for number of miles that will be driven
miles = float(input(f"How many miles will you drive the {vehicle}?"))

# Calculate gallons of gas needed
gallons_needed = miles / mpg

# Display result for gas needed
print(f"\n{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")

