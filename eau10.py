# Index wanted

import sys

arguments = sys.argv[1:]

def index_wanted(args):
    
    a_rechercher = args[-1]
    recherche = args[:-1]

    for i in range(len(recherche)):
        if recherche[i] == a_rechercher:
            return i
    
    return -1

def verification_arguments(args):
    ok = False
    if len(args) >= 2:  
        ok = True
    return ok

def erreur():
    print("error")

if __name__ == "__main__":
    if verification_arguments(arguments):
       print(index_wanted(arguments))
     
    else:
        erreur()