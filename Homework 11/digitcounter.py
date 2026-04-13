m=int(input("Enter a number: "))

count=0

while m>0:
    m=m//10
    count=count+1
print(count)