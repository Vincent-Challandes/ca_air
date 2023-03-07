## Modules and Functions 

import sys

def error_handling(arguments):
    if not len(arguments) == 2:
        print("Error!")
        sys.exit()

def once_by_time(string):
   
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            print(string[i], end = "")
    print(string[-1])

## Error handling

error_handling(sys.argv)


## Parsing

string_arg = sys.argv[1]


## Resolution 

once_by_time(string_arg)
