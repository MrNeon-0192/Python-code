print("Enter the marks of 5 subjects: \n")

marKOne=int(input("Subject 1: "))
marKTwo=int(input("Subject 2: "))
marKThree=int(input("Subject 3: "))
marKFour=int(input("Subject 4: "))
marKFive=int(input("Subject 5: "))

tot=marKOne+marKTwo+marKThree+marKFour+marKFive
avg=tot/5

print("Total Marks: ",tot)
print("Average Marks: ",avg)

if avg==100:
    print("Grade: A+")
elif avg>91 and avg<=100:
    print("Grade: A")
elif avg>81 and avg<=91:
    print("Grade: B")
elif avg>71 and avg<=81:
    print("Grade: C")
elif avg>61 and avg<=71:
    print("Grade: D")
else:
    print("Grade: F")