import sys

arguments = sys.argv[1:]

def entre_min_max(args):
    minimum = int(min(args))
    maximum = int(max(args))

    for i in range(minimum,maximum):
        print(i,end=" ")
    print()

def verification_arguments(args):
    ok = False
    if len(args) == 2:
            if args[0].isdigit() and args[1].isdigit():
                ok = True
    return ok

def erreur():
    print("error")

if __name__ == "__main__":
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        entre_min_max(arguments)
     
    else:
        erreur()