# JoshScript Source *.jsh
from sys import argv
from re import *
values = [0]*64
pointer = 0
ignored = [" ", "\t", "\n", chr(13), ";", "(", ")"]

def check(cd):
    for i in findall("....?", cd):
        if i.lower() != "josh":
            return False
    return True

def error(msg):
    print("JoshScript Error // " + msg)

def removal(code):
    for i in findall(compile(".*?\((.*?)\)"),code) + ignored:
        code = code.replace(i, "")
    return code

def interpret(code):
    code = removal(code)
    if len(code) % 4 == 0 and check(code):
        for i in findall("....?", code):
            global values, pointer
            if i == "JOSH": values[pointer] += [0, 1][values[pointer] < 256]
            elif i == "josh": values[pointer] -= [0, 1][values[pointer] > 0]
            elif i == "Josh": values[pointer] *= 2
            elif i == "josH": values[pointer] = int(values[pointer] / 2)
            elif i == "JOsh": print(end = chr(values[pointer]))
            elif i == "jOsh": values[pointer] = 0
            elif i == "JOSh": values[pointer] **= 2
            elif i == "JosH": print(end = str(values[pointer]))
            elif i == "JoSH": pointer = (pointer + 1) % 64
            elif i == "joSh": pointer -= [1, -63][pointer < 1]
            elif i == "joSH":
                try:
                    value = ord(input("\nIN> "))
                except:
                    error("Input is not a valid character")
            else:
                error("Not a valid josh")
    else:
        error("Code is not 100% josh, ensure there is no unintended spacing.")

def openfile(filename):
    data = open(filename, "r").read()
    interpret(data)

def runall():
    global values, pointer
    try:
        openfile(argv[1])
    except:
        try:
            print("Something went wrong, loading interpreter...")
            while True:
                pointer = 0
                values = [0]*64
                interpret(input("\n> "))
        except:
            error("Unknown Error :(")

print(end = "JoshScript 1.1\n> ")
runall()
print()
