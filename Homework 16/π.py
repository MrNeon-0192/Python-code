import math
def circumference(radius):
    if radius<0:
        return "Radius cannot be negative"
    circumference= 2*math.pi*radius
    return circumference
r=0.00000000000000000000000000005
result=circumference(r)
if isinstance(result, float):
    print(f"The circumference of the circle with radius {r} is {result}")
else:
    print(result)