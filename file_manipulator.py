import os
import sys

def reverse(input_path, output_path):
    contents = ''
    with open(input_path, 'r') as f:
        contents = f.read()
    contents = contents[::-1]
    with open(output_path, 'w') as f:
        f.write(contents)

def copy(input_path, output_path):
    contents = ''
    with open(input_path, 'r') as f:
        contents = f.read()
    with open(output_path, 'w') as f:
        f.write(contents)

def duplicate_contents(input_path, n):
    contents = ''
    with open(input_path, 'r') as f:
        contents = f.read()
    with open(input_path, 'w') as f:
        f.write(contents*int(n))
    
def replace_string(input_path, needle, new_string):
    contents = ''
    with open(input_path, 'r') as f:
        contents = f.read()
        contents = contents.replace(needle, new_string)
    with open(input_path, 'w') as f:
        f.write(contents)

def input_path_validator(input_path):
    return os.path.isfile(input_path)


COMMAND = {
    "reverse": reverse,
    "copy": copy,
    "duplicate-contents": duplicate_contents,
    "replace-string": replace_string, 
}

COMMAND_ARGS = {
    "reverse": 2,
    "copy": 2,
    "duplicate-contents": 2,
    "replace-string": 3,
}

def validator(args):
    if(not args[0] in COMMAND):
        print("This is not valid command.")
        return False
    if(len(args)-1 != COMMAND_ARGS.get(args[0])):
        print("Amount of arguments is not valid.")
        return False
    if(not input_path_validator(args[1])):
        print("Input file path is wrong. File does not exist.")
        return False
    if(args[0]=="duplicate-contents"):
        if(not args[2].isdecimal()):
            print("Duplicate-contents' second argument should be number.")
            return False
    return True


## ここから本プログラムの実行

if(validator(sys.argv[1:])):
    command = COMMAND.get(sys.argv[1])
    arg_count = COMMAND_ARGS.get(sys.argv[1])
    if(arg_count==2):
        command(sys.argv[2], sys.argv[3])
    elif(arg_count==3):
        command(sys.argv[2], sys.argv[3], sys.argv[4])
