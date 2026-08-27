print("Welcome to our Fast-Food Restaurant!")
print("1. Order a Sandwich")
print("2. Order a Pizza")
print("3. Order a Burger")

choice = int(input("Enter your choice (1-3): "))

match choice:
    case 1:
        print("\nYou selected Sandwich.")
        print("1. Veg Club Sandwich")
        print("2. Grilled Cheese Sandwich")
        sub_choice = int(input("Select Sandwich type (1-2): "))
        
        match sub_choice:
            case 1:
                print("Order placed for Veg Club Sandwich.")
            case 2:
                print("Order placed for Grilled Cheese Sandwich.")
            case _:
                print("Invalid Sandwich choice!")
                
    case 2:
        print("\nYou selected Pizza.")
        print("1. Thin Crust Pizza")
        print("2. Cheese Burst Pizza")
        print("3. Fresh Dough Pizza")
        sub_choice = int(input("Select Pizza type (1-3): "))
        
        match sub_choice:
            case 1:
                print("Order placed for Thin Crust Pizza.")
            case 2:
                print("Order placed for Cheese Burst Pizza.")
            case 3:
                print("Order placed for Fresh Dough Pizza.")
            case _:
                print("Invalid Pizza choice!")
                
    case 3:
        print("\nYou selected Burger.")
        print("1. Aloo Tikki Burger")
        print("2. Paneer Tikka Burger")
        print("3. Peri Peri Burger")
        sub_choice = int(input("Select Burger type (1-3): "))
        
        match sub_choice:
            case 1:
                print("Order placed for Aloo Tikki Burger.")
            case 2:
                print("Order placed for Paneer Tikka Burger.")
            case 3:
                print("Order placed for Peri Peri Burger.")
            case _:
                print("Invalid Burger choice!")
                
    case _:
        print("Invalid Main Menu choice! Please select 1, 2, or 3.")