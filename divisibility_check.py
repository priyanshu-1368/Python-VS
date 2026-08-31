for i in range(1, 51):
    if i % 2 == 0:
        if i % 3 == 0:
            print(f"{i}: Divisible by both \n")
        else:
            print(f"{i}: Divisible by 2 \n")
    elif i % 3 == 0: 
        print(f"{i}: Divisible by 3 \n")
    else:
        print(f"{i}: Not divisible by 2 or 3 \n")