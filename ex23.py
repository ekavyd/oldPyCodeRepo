#import sys
#script, encoding, error = sys.argv

#---------functions-------
def main(l_file):
    line = l_file.readline()

    if line:
      print_line(line)
      return main(l_file)

def print_line(line):
    next_lang = line.strip()
    raw_bytes = next_lang.encode()
    cooked_string = raw_bytes.decode()
    print(raw_bytes, "<=====>", cooked_string)

#---------functions-------



lang = open("languages.txt")

main (lang)