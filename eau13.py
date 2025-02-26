import sys

def my_select_sort(array):
    new_array = array[:] 
    
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if new_array[j] < new_array[min_index]:
                min_index = j
        
        new_array[i], new_array[min_index] = new_array[min_index], new_array[i]   
    return new_array

def erreur():
    print("error")
    exit()

if __name__ == "__main__":
    arguments = sys.argv[1:]
    try:
        args_int =[abs(int(arg)) for arg in arguments]
        liste_triee = my_select_sort(args_int)
        for l in liste_triee:
            print(l,end=" ")
        print()
    except :
        erreur()