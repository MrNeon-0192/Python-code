num=int(input("Enter a number: "))
t=num
numlength=0
while t>0:
    numlength=numlength+1
    t=int(t/10)

if numlength>=4:
    numlength=int(numlength/2)
    chk=0
    while num>0:
        rem=num%10
        if chk==numlength:
            middone=rem
        elif chk==numlength-1:
            midtwo=rem
        num=int(num/10)
        chk=chk+1
    prod=middone*midtwo

    print("The product of the middle two digits is: " + str(middone) + "*" + str(midtwo) + "=" + str(prod))
else:
    print("The number is not a 4 or more digit number.")
    

