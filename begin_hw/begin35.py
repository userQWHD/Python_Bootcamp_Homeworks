V = float(input("Enter the velocity of the boat in still water (V km/h): "))
U = float(input("Enter the river flow velocity (U km/h): "))
T1 = float(input("Enter the time spent going along the lake (T1 hours): "))
T2 = float(
    input("Enter the time spent going against the stream of the river (T2 hours): "))

distance1 = T1 * V

distance2 = T2 * (V - U)

total_distance = distance1 + distance2

print("The distance covered by the boat is:", total_distance, "km")
