#
#
#do twice

def do_twice(func1, text_in):
    func1(text_in)
    func1(text_in)

def func11(text_in):
    print(text_in)

print("Please input a text to echo:")
text_in = input("> ")
do_twice(func11, text_in)







