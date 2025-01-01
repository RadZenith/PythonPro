# Convert Kg to g 
kg = int(input("Enter your weidght in kg: "))
g = kg * 1000
print("Your weight is", str(g)+"g")
print("Your weight is ", g, "g", sep="")

# Area of triangle
x = int(input("Enter x: "))
y = int(input("Enter y: "))

area = int((x*y)/2)
print("Area =", area)

# Simple Calculator
x = int(input("Enter x: "))
y = int(input("Enter y: "))

print(x, "+", y, "=", x+y)
print(x, "-", y, "=", x-y)
print(x, "*", y, "=", x*y)
print(x, "/", y, "=", x/y)


# Slicing Number
x = int(input("Enter a number in range of 100 to 999: "))
temp = x % 10
print(temp)
x = x // 10
temp = x % 10
print(temp)
x = x // 10
temp = x % 10
print(temp)

# Convert Degree to Radian
# R = D * (3.14 / 180)
d = int(input("Enter Degree: "))
r = d * (3.14 / 180)
print("Radian:", r)