rowSize=int(input("Please enter the number of rows: "))
if rowSize%2==0:
    halfDiam=int(rowSize/2)
else:
    halfDiam=int((rowSize/2)+1)
    space=halfDiam-1
for i in range(1,halfDiam+1):
    for j in range(1, space+1):
        print(" ",end="")
    space=space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        num=num+1
    print()
space=1
for i in range(1,halfDiam):
    for j in range(1,space+1):
        print(" ",end="")
    space=space+1
    num=1
    for j in range(1,2*(halfDiam-i)):
        print(end=str(num))
        num=num+1
    print()