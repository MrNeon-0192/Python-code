h=input("Enter the month: ")

o=["March", "April", "May", "June", "July", "August", "September"]
p=["October", "November", "December", "January", "February"]

if h in o:
    print("That month is in the summer season.")
elif h in p:
    print("That month is in the winter season.")
else:
    print("That is not a month.")