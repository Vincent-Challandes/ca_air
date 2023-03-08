## Modules and Functions

import sys

def error_handling(arguments):
    if not len(arguments) > 2:
        print("Error!")
        sys.exit()


def check_pass_sanitaire(array, string):
    new_array = []
    for i in array:
        if not string.lower() in i and not string.upper() in i:
            new_array.append(i)
    return new_array


def print_array(array):
    for i in range(len(array)):
        if len(array) == 1:
            print(array[i])
        elif i == len(array) -1:
            print(array[i])
        else:
            print(array[i], end= ", ")


## Error hanlding 

error_handling(sys.argv)


## Parsing 

array_de_strings, string_recu = sys.argv[1:-1], sys.argv[-1]


## Resolution 

resultat = check_pass_sanitaire(array_de_strings, string_recu)


## Display

print_array(resultat)
