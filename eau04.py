import sys

def verification_arguments(args):
    ok = False
    if len(args) == 1:
        if args[0].isdigit():
            ok = True
    return ok

def erreur():
    print("-1")

def est_prochain_premier(nombre:str):
    nombre_premier = False
    nombre_controle = int(nombre)
    while not nombre_premier:
        nombre_controle += 1
        nombre_premier = est_premier(nombre_controle)
    return nombre_controle
        
def est_premier(a):
    if a < 2:
        return False
    
    for i in range(2,a):
        if a%i == 0:
            return False
    return True        

    

if __name__ == "__main__":
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        print(est_prochain_premier(arguments[0]))
    else:
        erreur()