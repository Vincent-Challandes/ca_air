## Modules and Functions

import sys

def error_handling(arguments):
    if not len(arguments) > 2:
        print("Error !")
        sys.exit()
    for i in arguments[1:]:
        if not i.lstrip("-").isdigit():
            print("Error not digit!")
            sys.exit()

def my_quick_sort(array):
    # permet de retourner le nombre une fois qu'il est à la bonne place
    if len(array) <= 1:
        return array
    else:
        # ici on prend array[0] mais on peut très bien prendre array[-1] par-contre faut modifierla boucle par for i in range(len(array) - 1)
        # pour pas avoir array[i] == array[pivot]
        pivot = array[0]
        left = []
        right = []
        for i in range(1, len(array)):
            array[i], pivot = int(array[i]), int(pivot)
            if array[i] < pivot:
                left.append(array[i])
            else:
                right.append(array[i])
        # on renvoi les array left et right jusqu'a obtenir des tableau de 1 occurance et le tri est fair car poussé à leur place définitive
        # left + pivot + right permet l'ordre du retour donc on prent 1 er étage on fait left pivot right et la on descand dans sous tableau
        # on fait à gaude du premier pivot left pivotleft2 right puis au centre premier pivot donc left pivot1 right puis a droite left pivotright2 right
        # puis on descend de la même manière jusqu'à avoir dans chaque tableau left et right une occurence
        return my_quick_sort(left) + [pivot] + my_quick_sort(right)


def print_array(array):
    for i in array:
        print(f"{i}", end=" ")
    print("")


## Error handling

error_handling(sys.argv)


## Parsing

array_nb = sys.argv[1:]


## Resolution

new_array_nb = my_quick_sort(array_nb)


## Display

print_array(new_array_nb)
