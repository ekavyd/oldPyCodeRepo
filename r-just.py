#
#
#spacer string

def right_just(str_in):
    spacer = 70 - (len(str_in))
    spacer_str = " " * spacer
    comb = spacer_str + str_in
    print(f" {comb} ")

print("what string should we right justify?")
userin = input("> ")
right_just(userin)






