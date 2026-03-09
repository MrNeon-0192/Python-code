print("Enter the marks of the following subjects:")
subject1 = int(input("Math: "))
subject2 = int(input("Science: "))
subject3 = int(input("English: "))
subject4 = int(input("History: "))
subject5 = int(input("Geography: "))

total = subject1 + subject2 + subject3 + subject4 + subject5
perc=(total/500)*100

print("The percentage marks are:", perc)