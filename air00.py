## Modules and Functions

import sys

def error_handling(arguments):
    if not len(arguments) == 2:
        print("Error!")
        sys.exit()

def fonction_split(string_a_couper, string_separateur):
    array_split = []
    index_debut = 0
    for i in range(len(string_a_couper)):
        if string_a_couper[i] in string_separateur:
            array_split.append(string_a_couper[index_debut:i])
            index_debut =   i + 1         
        # permet d'ajouter la dernière découpe de string
        elif i == len(string_a_couper) - 1:
            # [index_debut  i + 1] +1 pour intégrer la dernière lettre de la string
            array_split.append(string_a_couper[index_debut:i + 1])         
    return array_split

def print_array(array):
    for i in array:
        print(i)


## Error handling

error_handling(sys.argv)


## Parsing

string_reçu = sys.argv[1]

string_separateur_def = " \t\n"


## Resolution

resultat = fonction_split(string_reçu, string_separateur_def)


## Display

print_array(resultat)
