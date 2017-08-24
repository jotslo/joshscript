# JoshScript Source *.jsh
from sys import argv
from re import findall
value = 0

def check(cd):
    for i in findall("....?", cd):
        if i.lower() != "josh":
            return False
    return True

def error(msg):
    print("JoshScript Error // " + msg)

def interpret(code):
    if len(code) % 4 == 0 and check(code):
        for i in findall("....?", code):
            global value
            if i == "JOSH": value += 1
            elif i == "josh": value -= [0, 1][value > 0]
            elif i == "Josh": value *= 2
            elif i == "josH": value = int(value / 2)
            elif i == "JOsh": print(end = chr(value))
            elif i == "jOsh": value = 0
            elif i == "JOSh": value = **= 2
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
    try:
        openfile(argv[1])
    except:
        error("Unknown error :(")

print(end = "JoshScript v1.01\n> ")
runall()
print()
