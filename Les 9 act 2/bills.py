unit=int(input("Enter the number of units consumed: "))

if unit <= 50:
    bill = unit * 2.60
    supcharge = 25
elif unit <= 100:
    bill = 130 + (unit - 50) * 3.25
    supcharge = 35

elif unit <= 200:
    bill = 130 + 162.50 + (unit - 100) * 5.26
    supcharge = 50
else:
    bill = 130 + 37.50 + 526 + (unit - 200) * 8.45
    supcharge = 75
total= bill + supcharge
print("The total bill is: Rs. %.2f}" %total)