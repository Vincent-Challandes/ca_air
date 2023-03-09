## Modules and Functions and Globals variables

import sys
import os
import subprocess


def error_handling(array):
    for i in array:
        if not script_exist(i):
            print(f"Error {i} not found")


def script_exist(fichier_script):
    exist = ""
    if os.path.exists(fichier_script):
        exist = True
    else:
        exist = False
    return exist


def test(array):
    nombre_success = 0
    nombre_test = 0
    programme = ""
    num_test = ""

    for i in range(len(array)):
        #print(array[i])
        programme = array[i]
        num_test = i

        # test air00.py
        if num_test == 0:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "Bonjour les gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Bonjour\n" "les\n" "gars\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error!\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air01.py
        elif num_test == 1:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "Crevette magique dans la mer des étoiles", "la"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Crevette magique dans \n" " mer des étoiles\n":
                count_success += 1
                print(f"{programme} ({count_test}/3) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/3) : \033[31m" + "failure" + "\033[0m")

        
            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error!\n":
                count_success += 1
                print(f"{programme} ({count_test}/3) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/3) : \033[31m" + "failure" + "\033[0m")


            # test3
            result = subprocess.run(["python3", programme, "1", "2"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "1\n":
                count_success += 1
                print(f"{programme} ({count_test}/3) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/3) : \033[31m" + "failure" + "\033[0m")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air02.py
        elif num_test == 2:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "Bonjour les gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error!\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Bonjourgarslesgars\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air03.py
        elif num_test == 3:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "Bonjour les gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error!\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

            # test2
            result = subprocess.run(["python3", programme, "1", "2", "3", "4", "5", "4", "3", "2", "1"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "5 \n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air04.py
        elif num_test == 4:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "Hello milady,  bien ou quoi ??"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Helo milady, bien ou quoi ?\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error!\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air05.py
        elif num_test == 5:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "1", "2", "3", "4", "5", "+2"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "3 4 5 6 7 \n":
                count_success += 1
                print(f"{programme} ({count_test}/3) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/3) : \033[31m" + "failure" + "\033[0m")

            # test2
            result = subprocess.run(["python3", programme, "10", "11", "12", "20", "-5"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "5 6 7 15 \n":
                count_success += 1
                print(f"{programme} ({count_test}/3) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/3) : \033[31m" + "failure" + "\033[0m")

            # test3
            result = subprocess.run(["python3", programme, "2", "3", "1"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error last arg need to start with - or + and follow by a number\n":
                count_success += 1
                print(f"{programme} ({count_test}/3) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/3) : \033[31m" + "failure" + "\033[0m")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air06.py
        elif num_test == 6:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "Michel", "Albert", "Thérèse", "Benoit", "t"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Michel\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

            # test2
            result = subprocess.run(["python3", programme, "Michel", "Albert", "Thérèse", "Benoit", "a"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Michel, Thérèse, Benoit\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air07.py
        elif num_test == 7:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "1", "3", "4", "2"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "1 2 3 4 \n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

            # test2
            result = subprocess.run(["python3", programme, "10", "20", "30", "40", "50", "60", "70", "90", "33"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "10 20 30 33 40 50 60 70 90 \n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air08.py
        elif num_test == 8:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "10", "20", "30", "fusion", "15", "25", "35"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "10 15 20 25 30 35 \n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error need word \"fusion\"\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air09.py
        elif num_test == 9:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "Michel", "Albert", "Thérèse", "Benoit"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Albert, Thérèse, Benoit, Michel\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "les, gars, Bonjour\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air10.py
        elif num_test == 10:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "essay.txt"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Salut les gars \n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error!\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air11.py
        elif num_test == 11:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "Bonjour les gars", "455"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error first arg need only 1 caractere\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

            # test2
            result = subprocess.run(["python3", programme, "B", "les"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error second arg have to be number!\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air12.py
        elif num_test == 12:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "6", "5", "4", "3", "2", "1"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "1 2 3 4 5 6 \n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error not digit!\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : \033[32m" + "success" + "\033[0m")
            else:
                print(f"{programme} ({count_test}/2) : \033[31m" + "failure" + "\033[0m")

        
            nombre_success += count_success
            nombre_test += count_test


    print(f"Total success : ({nombre_success}/{nombre_test})")    


array_my_script = ["air00.py", "air01.py", "air02.py", "air03.py", "air04.py", "air05.py", "air06.py", "air07.py", "air08.py", "air09.py", "air10.py", "air11.py", "air12.py"]



## Error handling

error_handling(array_my_script)


## Resolution

test(array_my_script)
