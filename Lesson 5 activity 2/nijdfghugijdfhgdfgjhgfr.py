Sold=float(input("Enter the selling price: "))  
Cost=float(input("Enter the cost price: "))

if Sold>Cost:
    amount=Sold-Cost
    print("The profit is {0}".format(amount)) 
else:
    print("No profit is made.")

    