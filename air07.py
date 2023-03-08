## Modules and Functions

import sys

def error_handling(arguments):
    if not len(arguments) > 3:
        print("Error !")
        sys.exit()
    for i in arguments[1:]:
        if not i.isdigit():
            print("Error not digit!")
            sys.exit()


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
                index_min = j
        
        if index_min != i:
            array[i], array[index_min] = array[index_min], array[i]
        
    return array


def sorted_insert(array, new_element):
    new_element = int(new_element)
    for i in range(len(array)):
        array[i] = int(array[i])
        if array[i] > new_element:
            array.insert(i, new_element)
            break
        elif i == len(array) - 1 and array[i] <= new_element:
            array.insert(i + 1, new_element)
    return array


def affichage(array):
    result = ""
    for i in array:
        result += f"{i} "
    print(result)


## Error handling

error_handling(sys.argv)


## Parsing 

array_recu, element_recu = sys.argv[1:-1], sys.argv[-1]


## Resolution 

check_array = selection_sort(array_recu)

new_array = sorted_insert(check_array, element_recu)


## Display 

affichage(new_array)
