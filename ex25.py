#
#
#
def break_words(stuff):
    words = stuff.split(' ')
    return words
    #this function will break up words

def sort_words(words):
    return sorted(words)
    #sorts words

def print_first_word(words):
    word = words.pop(0)
    print(word)


def print_last_word(words):
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
