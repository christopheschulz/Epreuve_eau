# String dans string

import sys

def str_dans_str(args):
    return args[1] in args[0]

def verification_arguments(args):
    ok = False
    if len(args) == 2:
        if not args[0].isdigit() and not args[1].isdigit():
            ok = True
    return ok

def erreur():
    print("error")

if __name__ == "__main__":
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        print(str_dans_str(arguments))
    else:
        erreur()