days=int(input("Enter the number of days: "))

year=days//365
month=(days%365)//30
week=((days%365)%30)//7
day=(((days%365)%30)%7)//1

if month>=12:
    year+=1
    month=0

print("The number of years is", year)
print("The number of months is", month)
print("The number of weeks is", week)
print("The number of days is", day)