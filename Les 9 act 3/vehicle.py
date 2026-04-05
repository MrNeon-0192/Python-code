choice = int(input("Enter your choice:\n1. Car\n2. Bike\n"))

if choice == 1:
    choice2 = int(input("What car?\n1. Audi\n2. BMW\n"))
    
    if choice2 == 1:
        print("You chose Audi")
    elif choice2 == 2:
        print("You chose BMW")
    else:
        print("Invalid car choice")

elif choice == 2:
    choice3 = int(input("What bike?\n1. Yamaha\n2. Honda\n"))
    
    if choice3 == 1:
        print("You chose Yamaha")
    elif choice3 == 2:
        print("You chose Honda")
    else:
        print("Invalid bike choice")

else:
    print("Invalid choice")