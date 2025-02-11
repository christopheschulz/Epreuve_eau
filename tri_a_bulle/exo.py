import sys


def my_bubble_sort(array):
    new_array = array[:]
    for i in range(len(array) - 1):
       
        for j in range(len(array) - 1 - i):
            if new_array[j] > new_array[j + 1]:
                new_array[j], new_array[j + 1] = new_array[j + 1], new_array[j]  # Échange des éléments
                
        
    return new_array


def erreur():
    print("error")
    exit()


if __name__ == "__main__":
    arguments = sys.argv[1:]
    try:
        args_int =[abs(int(arg)) for arg in arguments]
        liste_triee = my_bubble_sort(args_int)
        for l in liste_triee:
            print(l,end=" ")
        print()
    except :
        erreur()

    