x_kg = float(input("Enter the number of kg of sweets: "))
a_tmt = float(input("Enter the cost of X kg of sweets: "))

cost_per_kg = a_tmt / x_kg
cost_of_y_kg = cost_per_kg * x_kg

print("The cost of 1 kg of sweets is", cost_per_kg, "manats.")
print("The cost of Y kg of sweets is", cost_of_y_kg, "manats.")