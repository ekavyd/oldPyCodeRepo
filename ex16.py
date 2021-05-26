from sys import argv

script, filename = argv

print (f"We're going to erase {filename} .")
print ("If you don't want that hit CRTL-C . ")
print ("If you do want that, hit return.")

input("?")

print("OPening the file...")
target = open(filename, "w")

print("Truncating file")
target.truncate()

print("Now I'm going to ask you for 3 lines to put back in the file.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm goign to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we will close the file")
target.close()