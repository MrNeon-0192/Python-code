def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)

print("Factorial of 5 is", factorial(5))
print("Factorial of 0 is", factorial(0))
print("Factorial of 1 is", factorial(1))
print("Factorial of 10 is", factorial(10))
print("Factorial of 6 is", factorial(6))