V1 = float(input("Enter the velocity of the first car (V1 km/h): "))
V2 = float(input("Enter the velocity of the second car (V2 km/h): "))
S = float(input("Enter the initial distance between the cars (S km): "))
T = float(input("Enter the time in hours (T hours): "))

total_velocity = V1 + V2

total_distance = T * total_velocity

distance_between_cars = S + total_distance

print("The distance between the cars after", T, "hours is:", distance_between_cars, "km")