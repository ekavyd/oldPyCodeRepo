from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#comment
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exists? {exists(to_file)}")
print("Ready! Hit the return button to proceed.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, done")

out_file.close()
in_file.close()