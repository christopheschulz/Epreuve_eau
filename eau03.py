# Suite de Fibonacci

import sys


def verification_arguments(args):
    ok = False
    if len(args) == 1:
        if args[0].isdigit():
            ok = True
    return ok


def erreur():
    print("-1")


def suite_de_fibonacci(nombre)-> list:
    result =[0,1]
    if int(nombre) == 0:
        return [0]
    elif int(nombre) == 1:
        return [1]
    else :
        for i in range(2,int(nombre)+1):
            result.append(result[i-1]+result[i-2])
        return result


def main():
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        suite = suite_de_fibonacci(arguments[0])
        # on imprime le dernier de la liste de fibonnacci
        print(suite[-1])
    else:
        erreur()


if __name__ == "__main__":
    main()
    

