#
#
#

print("How many numbers would you like to print?" )
usrin = int(input("> "))

i = 1
numbers = []

while i<(usrin+1):
    print(f"At the top i is {i}")
    numbers.append(i)

    i+=1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i} \n")

print("The numbers: ")

for num in numbers:
    print(num)

