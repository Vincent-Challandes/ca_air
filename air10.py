## Modules and Functions 

import sys 
import os

def error_handling(arguments):
    if not len(arguments) == 2:
        print("Error!")
        sys.exit()

def afficher_contenu(nom_fichier):
    # on contrôle que le fichier existe avec path.exists du module os 
    if os.path.exists(nom_fichier):
        # on ouvre le fichier pour le lecture "r"
        fichier = open(nom_fichier, "r")
        # on va lire et printer ce qui se trouve dans le fichier
        print(fichier.read())
        # on referme le fichier
        fichier.close()
    else:
        print("Error file no found!")
        sys.exit()


## Error handling

error_handling(sys.argv)


## Parsing 

fichier_arg = sys.argv[1]


## Resolution

afficher_contenu(fichier_arg)
