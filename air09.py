## Modules and Functions 

import sys


def error_handling(arguments):
    if not len(arguments) > 2:
        print("Error!")
        sys.exit()


def left_turn(array):
    # mettre le premier élément à la fin 
    array.append(array[0])
    # puis on déplace a gauche
    for i in range(len(array)-1):
        array[i] = array[i + 1]
    # on efface le dernière élément
    array.remove(array[-1])
    
    return array


def print_array(array):
    for i in range(len(array)):
        if len(array) == 1:
            print(array[i])
        elif i == len(array) -1:
            print(array[i])
        else:
            print(array[i], end= ", ")


## Error handling

error_handling(sys.argv)


## Parsing 

array_recu = sys.argv[1:]


## Resolution 

new_array = left_turn(array_recu)

## Display 

print_array(new_array)
