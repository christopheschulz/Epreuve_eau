import sys

def majuscule(chaine):
    split_chaine = chaine.split()
    chaine_modifiée =[]
    for word in split_chaine:
        chaine_modifiée.append(word[0].upper()+word[1:].lower())
    return " ".join(chaine_modifiée)

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
        print(majuscule(arguments[0]))
    else:
        erreur()