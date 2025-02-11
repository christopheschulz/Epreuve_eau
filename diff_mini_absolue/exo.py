import sys

arguments = sys.argv[1:]

def diff_min_absolue(args):
    args.sort()
    print(args_int)
    minimum_absolue = float('inf')

    for i in range(1,len(args)):
        soustraction = abs(args[i]) - abs(args[i-1])
        if soustraction < minimum_absolue:
            minimum_absolue = soustraction

    return minimum_absolue

def verification_arguments(args):
    ok = False
    if len(args) >= 3 :  
        ok = True
    return ok

def erreur():
    print("error")

if __name__ == "__main__":
    try:
        args_int =[abs(int(arg)) for arg in arguments]
    except :
        erreur()

    if verification_arguments(args_int):
       print(diff_min_absolue(args_int))
     
    else:
        erreur()