## Modules and Functions

import sys

def error_handling(arguments):
    if not len(arguments) == 3:
        print("Error!")
        sys.exit()
    elif not len(sys.argv[1]) == 1:
        print("Error first arg need only 1 caractere")
        sys.exit()
    elif not arguments[2].isdigit():
        print("Error second arg have to be number!")
        sys.exit()

def pyramide(caractere, nb_etage):
    space = " "
    nb_space = nb_etage -1
    nb_caractere = 1
    for i in range(nb_etage):
        print(f"{nb_space * space}{nb_caractere * caractere}")
        nb_space -= 1
        nb_caractere += 2


## Error handling

error_handling(sys.argv)


## Parsing 

arg1_caractère, arg2_nb_etage = sys.argv[1], int(sys.argv[2])


## Resolution

pyramide(arg1_caractère, arg2_nb_etage)
