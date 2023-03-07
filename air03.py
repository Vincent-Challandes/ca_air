## Modules and Functions

import sys

def error_handling(arguments):
    if not len(arguments) > 3:
        print("Error!")
        sys.exit()

def chercher_intru(array):
    no_pair = ""
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] == array[j]:
                break
        # or i == j permet dans le cas ou le dernier mot n'a pas de pair d'être ajouter a no_pair
        # car la seul foi ou, i == j à la fin des deux boucle, ca sera en dernière position 
        # donc si égaux signifie qu'il compart le même élément donc pas de pair on ajout a no_pair
        if array[i] != array[j] or i == j:
            no_pair += f"{array[i]} "
    return no_pair


## Error handling

error_handling(sys.argv)


## Parsing

array_arg = sys.argv[1:]


## Resolution

resultat = chercher_intru(array_arg)


## Display

print(resultat)
