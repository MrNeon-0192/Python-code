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
        
    

