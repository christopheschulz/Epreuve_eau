# Par ordre Ascii

import sys


def tranform_in_ascii_number(array):
    word_ascii_number = []
    for arg in array:
        char_ascii_number = []
        for a in arg:
            char_ascii_number.append(ord(a.lower()))
        word_ascii_number.append(char_ascii_number)
    return word_ascii_number


def par_ordre_ascii(a_trier,arguments):
    for i in range(2,len(a_trier)):
        if a_trier[i][0] < a_trier[i-1][0]:
            arguments[i],arguments[i-1] = arguments[i-1],arguments[i]

    return arguments
        

def erreur():
    print("error")
    exit()


def verification_arguments(args):
    ok = False
    is_string = all(arg.isalpha() for arg in args)
    if is_string:
        if len(args) >= 2:
            ok = True
    return ok


def main():
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        a_trier = tranform_in_ascii_number(arguments)
        triee = par_ordre_ascii(a_trier,arguments)
        for word in triee:
            print(word,end=" ")
        print()
    else:
        erreur()

if __name__ == "__main__":
    main()