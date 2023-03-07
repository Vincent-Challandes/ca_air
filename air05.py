## Modules and Functions

import sys


def error_handling(arguments):

    if not len(arguments) > 2:
        print("Error!")
        sys.exit()
    # on contrôle notre liste de nombre sans dernier élément car lui commence avec - ou +
    for i in arguments[1:-1]:
        if not i.isdigit():
            print("Error not digit!")
            sys.exit()
    # on s'occupe du dernier élément qu'il soit un nombre et commence avec - ou +
    if not arguments[-1].lstrip("-+").isdigit():
            print("Error last arg is not a number")
            sys.exit()

    elif not arguments[-1].startswith("-") and not arguments[-1].startswith("+"):
        print("Error last arg need to start with - or + and follow by a number")
        sys.exit()
    

def on_each_of_them(array, operation):
    add_sub = operation[0]
    nombre_pour_operation = operation[1:]
    for i in array:
        i = int(i)
        if add_sub == "+":
            print(i + int(nombre_pour_operation), end=" ")
        elif add_sub == "-":
            print(i - int(nombre_pour_operation), end=" ")
    print("\r")


## Error handling

error_handling(sys.argv)


## Parsing 

array_nb = sys.argv[1:-1]

operation_symb_nb = sys.argv[-1]


## Resolution

on_each_of_them(array_nb, operation_symb_nb)
