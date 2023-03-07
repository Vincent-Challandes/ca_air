## Modules and Functions

import sys

def error_handling(arguments):
    if not len(arguments) > 2:
        print("Error!")
        sys.exit()

def concat(array, separateur):
    string = ""
    for i in array:
        string += i + separateur
    return string


## Error handling

error_handling(sys.argv)


## Parsing

array_string = sys.argv[1:-1]

separateur = sys.argv[-1]


## Resolution

resultat = concat(array_string, separateur)


## Display

print(resultat)
