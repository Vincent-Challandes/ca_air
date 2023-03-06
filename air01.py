## Modules and Functions

import sys

def error_handling(arguments):
    if not len(arguments) == 3:
        print("Error!")
        sys.exit()

def fonction_split_en_fonction(string_a_couper, separateur):
    array_split = []
    index = 0
    for i in range(len(string_a_couper)):
        if string_a_couper[i: i + len(separateur)] == separateur:
            array_split.append(string_a_couper[index:i])
            index = i + len(separateur) 
        elif i == len(string_a_couper) - 1:
            array_split.append(string_a_couper[index:i + 1])
    return array_split
    
def print_array(array):
    for i in array:
        print(i)


## Error handling 

error_handling(sys.argv)


## Parsing

string, separateur = sys.argv[1], sys.argv[2]


## Resolution

resultat = fonction_split_en_fonction(string, separateur)


## Display

print_array(resultat)
