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
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error! \n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

        
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
                print(f"{programme} ({count_test}/3) : success")
            else:
                print(f"{programme} ({count_test}/3) : failure")

        
            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error!\n":
                count_success += 1
                print(f"{programme} ({count_test}/3) : success")
            else:
                print(f"{programme} ({count_test}/3) : failure")


            # test3
            result = subprocess.run(["python3", programme, "1", "2"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "1\n":
                count_success += 1
                print(f"{programme} ({count_test}/3) : success")
            else:
                print(f"{programme} ({count_test}/3) : failure")

        
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
            if result.stdout == "Bonjour\n" "les\n" "gars\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error! \n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

        
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
            if result.stdout == "Bonjour\n" "les\n" "gars\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error! \n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air04.py
        elif num_test == 4:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "Bonjour les gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Bonjour\n" "les\n" "gars\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error! \n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air05.py
        elif num_test == 5:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "Bonjour les gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Bonjour\n" "les\n" "gars\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error! \n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air06.py
        elif num_test == 6:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "Bonjour les gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Bonjour\n" "les\n" "gars\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error! \n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air07.py
        elif num_test == 7:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "Bonjour les gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Bonjour\n" "les\n" "gars\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error! \n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air08.py
        elif num_test == 8:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "Bonjour les gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Bonjour\n" "les\n" "gars\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error! \n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air09.py
        elif num_test == 9:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "Bonjour les gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Bonjour\n" "les\n" "gars\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error! \n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air10.py
        elif num_test == 10:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "Bonjour les gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Bonjour\n" "les\n" "gars\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error! \n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air11.py
        elif num_test == 11:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "Bonjour les gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Bonjour\n" "les\n" "gars\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error! \n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

        
            nombre_success += count_success
            nombre_test += count_test

        # test air12.py
        elif num_test == 12:
            count_success = 0
            count_test = 0

            # test1
            result = subprocess.run(["python3", programme, "Bonjour les gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Bonjour\n" "les\n" "gars\n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

            # test2
            result = subprocess.run(["python3", programme, "Bonjour", "les", "gars"], capture_output=True, text=True)
            count_test += 1
            # ATTENTION pas oublié les retour à la ligne "\n"
            if result.stdout == "Error! \n":
                count_success += 1
                print(f"{programme} ({count_test}/2) : success")
            else:
                print(f"{programme} ({count_test}/2) : failure")

        
            nombre_success += count_success
            nombre_test += count_test


    print(f"Total success : ({nombre_success}/{nombre_test})")    


array_my_script = ["air00.py", "air01.py", "air02.py", "air03.py", "air04.py", "air05.py", "air06.py", "air07.py", "air08.py", "air09.py", "air10.py", "air11.py", "air12.py"]



## Error handling

error_handling(array_my_script)


## Resolution

test(array_my_script)
