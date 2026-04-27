def add(p,q):
    print(p+q)
def subtract(p,q):
    print(p-q)
def multiply(p,q):
    print(p*q)
def divide(p,q):
    print(p/q)

print("Please select the operation:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide")

choice = input("Enter choice(1/2/3/4):")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    add(num1,num2)
elif choice == '2':
    subtract(num1,num2)
elif choice == '3':
    multiply(num1,num2)
elif choice == '4':
    divide(num1,num2)
else:
    print("Invalid input")