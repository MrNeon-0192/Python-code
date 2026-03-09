x=int(input("Enter a number: "))


if x<0:
    print("The number can not be negative")
else:
    sqrt=x**0.5
    print("The square of", x, "is", x**2)
    print("The square root of", x, "is", sqrt)
    print("The cube of", x, "is", x**3)
    print("The cube root of", x, "is", x**(1/3))
