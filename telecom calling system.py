print("Welcome to Telecom Customer Care")
print("1. Press 1 for English")
print("2. Press 2 for Hindi")
print("3. Press 3 for Gujarati")

lang_choice = int(input("Enter your choice (1-3): "))

match lang_choice:
    case 1:
        print("\nYou have selected English.")
        print("1. Prepaid Services")
        print("2. Postpaid Services")
        print("3. Broadband Services")
        sub_choice = int(input("Select an option (1-3): "))
        
        match sub_choice:
            case 1:
                print("Routing to English Prepaid agent...")
            case 2:
                print("Routing to English Postpaid agent...")
            case 3:
                print("Routing to English Broadband agent...")
            case _:
                print("Invalid option selected.")
                
    case 2:
        print("\nAapne Hindi chuna hai.")
        print("1. Prepaid Sevaayein")
        print("2. Postpaid Sevaayein")
        sub_choice = int(input("Vikalp chunein (1-2): "))
        
        match sub_choice:
            case 1:
                print("Hindi Prepaid agent se sampark kiya jaa raha hai...")
            case 2:
                print("Hindi Postpaid agent se sampark kiya jaa raha hai...")
            case _:
                print("Aamanya vikalp.")
                
    case 3:
        print("\nTame Gujarati pasand karyu chhe.")
        print("1. Prepaid Seva mate")
        print("2. Postpaid Seva mate")
        sub_choice = int(input("Vikalp pasand karo (1-2): "))
        
        match sub_choice:
            case 1:
                print("Gujarati Prepaid agent sathe jodai rahya chho...")
            case 2:
                print("Gujarati Postpaid agent sathe jodai rahya chho...")
            case _:
                print("Khotoy vikalp.")
                
    case _:
        print("Invalid language choice! Please press 1, 2, or 3.")