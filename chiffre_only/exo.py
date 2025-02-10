import sys

chiffre= ["0","1","2","3","4","5","6","7","8","9"]

def chiffre_only(chaine):
   for c in chaine:
       if c not in chiffre:
           return False
   return True

def verification_arguments(args):
    ok = False
    if len(args) == 1:
            ok = True
    return ok

def erreur():
    print("error")

if __name__ == "__main__":
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        print(chiffre_only(arguments[0]))
    else:
        erreur()