import sys


def verification_arguments(args):
    return len(args) > 1

def erreur():
    print("error")

def inversion(args):
    return args[::-1]

def affiche(args):
    for arg in args:
        print(arg)
    

if __name__ == "__main__":
    arguments = sys.argv[1:]
    
    if verification_arguments(arguments):
       arguments_inversés = inversion(arguments)
       affiche(arguments_inversés)
    else:
        erreur()
