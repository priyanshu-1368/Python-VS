age = int(input("Enter your age: "))

if age <= 0:
    print("You entered an invalid age.")
elif age >= 1 and age <= 12:
    print("You are a child.")
elif age >= 13 and age <= 19:
    print("You are a teenager.")
elif age >= 20 and age <= 59:
    print("You are an adult.")
else:
    print("You are a senior citizen.")