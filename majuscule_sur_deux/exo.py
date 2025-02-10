import sys
def une_maj_sur_deux(chaine:str):
    maj = 0
    chaine_modifiée = ""
    for i in range(len(chaine)):
        # On regarde si maj est paire si oui majuscule sinon minuscule
        if maj%2 == 0:
            chaine_modifiée += chaine[i].upper()
        else:
            chaine_modifiée += chaine[i].lower()
        # on n'incrémente la variable maj que si ce n'est pas un espace
        if not chaine[i] == " ":  
            maj += 1
    return chaine_modifiée


def verification_arguments(args):
    ok = False
    if len(args) == 1:
        if not args[0].isdigit():
            ok = True
    return ok

def erreur():
    print("error")

if __name__ == "__main__":
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        print(une_maj_sur_deux(arguments[0]))
    else:
        erreur()