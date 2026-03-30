print("Enter a number (Numerator): ")
num=int(input())
print("Enter a number (Denominator): ")
numd=int(input())

if num%numd==0:
    print("\n The number " + str(num) + " is divisible by " + str(numd))
else:   
    print("\n The number " + str(num) + " is not divisible by " + str(numd))