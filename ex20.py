#---------------functions
def add(a, b):
 print(f"\n ADDING {a} + {b} ")
 return a + b

def subtract(a,b):
 print(f"\n SUBTRACTING {a} - {b} ")
 return a - b

def multiply(a, b):
 print(f"\n MULTIPLYING {a} * {b} ")
 return a * b

def divide(a, b):
 print(f"\n DIVIDING {a} / {b} ")
 return a / b
#--------------functions

print("Let's do some math functions!")

print(" What is your age? ")
age = int(input("> "))
print(" What is your height? ")
height = int(input("> "))
print(" What is your weight? ")
weight = int(input("> "))
print(" What is your iq? ")
iq = int(input("> "))

print(f"\n Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
print(f"\n Now we will perform the mathamatical operations on each value by 10")

age2 = add(age, 10)
height2 = subtract(height, 10)
weight2 = multiply(weight, 10)
iq2 = divide(iq, 10)

print("The new values are.....:\n")
print(f"\n Age: {age2}, Height: {height2}, Weight: {weight2}, IQ: {iq2}")
