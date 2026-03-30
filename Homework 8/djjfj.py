def swap(a,b,c):
    temp=a
    a=b
    b=c
    c=temp
    return a,b,c

a=int(input("Enter a value: "))
b=int(input("Enter a value 2: "))
c=int(input("Enter a value 3: "))
print("Before swap: ", a, b, c)
a,b,c=swap(a,b,c)
print("After swap: ", a, b, c)
