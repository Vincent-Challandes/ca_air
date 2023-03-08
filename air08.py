## Modules and Functions

import sys

def error_handling(arguments):
    if not len(arguments) > 3:
        print("Error!")
        sys.exit()
    
    index = ""
    for i in range(1,len(arguments)):
        if arguments[i] == "fusion":
            index = i
            break
    
    if index != i:
        print("Error need word \"fusion\"")
        sys.exit()
    
    for j in range(1, len(arguments)):
        if j == index:
            continue
        elif not arguments[j].isdigit():
            print("Error not digit!")
            sys.exit()

    return index


def selection_sort(array):
    n = len(array)
    # permet de parcourir tous le tableau
    for i in range(n - 1):
        # index_min permet de prendre l'élément minimum du tableau
        index_min = i
        for j in range(i + 1, n):
            # ATTENTION convertir en int pour que ça soit trié correctement
            array[j], array[index_min] = int(array[j]), int(array[index_min])
            if array[j] < array[index_min]:
                print("Error your arrays not sorted!")
                sys.exit()
        
    return array


def sorted_fusion(array1, array2):
    for i in array2:
        i = int(i)
        for j in range(len(array1)):
            array1[j] = int(array1[j])
            if array1[j] > i:
                array1.insert(j, i)
                break
            elif j == len(array1) - 1 and array1[j] < i:
                array1.insert(j + 1, i)
            
    return array1
    

def affichage(array):
    result = ""
    for i in array:
        result += f"{i} "
    print(result)


## Error handling

index = error_handling(sys.argv)


## Parsing

array_1, array_2 = selection_sort(sys.argv[1:index]), selection_sort(sys.argv[index + 1:])


## Resolution 

new_array = sorted_fusion(array_1, array_2)


## Display

affichage(new_array)
