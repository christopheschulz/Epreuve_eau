# Paramètres à l’envers

import sys


def args_are_valid(args):
    return len(args) > 1


def error():
    print("error")


def inversion(args):
    return args[::-1]


def display(args):
    for arg in args:
        print(arg)
    

def main():
    args = sys.argv[1:]
    
    if args_are_valid(args):
       inverted_args = inversion(args)
       display(inverted_args)
    else:
        error()


if __name__ == "__main__":
    main()
  
