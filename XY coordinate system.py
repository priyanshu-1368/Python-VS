value_x = float(input("Enter the x-coordinate: "))
value_y = float(input("Enter the y-coordinate: "))

if value_x > 0 and value_y > 0:
    print("The point is in Quadrant 1.")
elif value_x < 0 and value_y > 0:
    print("The point is in Quadrant 2.")
elif value_x < 0 and value_y < 0:
    print("The point is in Quadrant 3.")
elif value_x > 0 and value_y < 0:
    print("The point is in Quadrant 4.")
else:
    print("The point is on the x and y axes.")