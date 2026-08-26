temperature = float(input("Enter the temperature in Celsius: "))


if temperature <= 0:
    print("It's very cold weather.")
elif temperature >= 0 and temperature < 10:
    print("It's a bit cold weather.")
elif temperature >= 10 and temperature < 20:
    print("It's a cold weather.")
elif temperature >= 20 and temperature < 30:
    print("It's normal weather.")
elif temperature >= 30 and temperature < 40:
    print("It's hot weather.")
else:
    print("It's very hot weather.")