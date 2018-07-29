from sys import argv
from re import compile,findall

memory = [0]*256 #number of cells
pointer = 0 #current cell
rem_input = "" #remaining input

ignored_chars = [
    " ",
    "\t",
    "\n",
    chr(13),
    ";"
]


def interpret_code(code):
    """ run word by word and interpret each accordingly"""

    global memory, pointer, rem_input

    # boolean assignment tables
    additive = [-255,1]
    slider = []

    valid_code = None

    #prevent recursive calls from being checked
    #they passed the first time no need to check again

    if type(code) is not list:
        valid_code = validate_code(code)
    else:
        valid_code = code
    code_length = len(valid_code)

    #to support loop handling
    after_loop = []

    if valid_code:
        for index, josh in enumerate(valid_code):
            current_value = memory[pointer]
            if josh == "JOSH":
                #if current_value is less than max possible int add 1 or wrap around to 0
                memory[pointer] += additive[current_value < 255]
            elif josh == "josh":
                #if current_value is less than max possible int subtract 1 or wrap around to 255
                memory[pointer] -= additive[current_value > 0]
            elif josh == "Josh":
                #multiply by 2 or wrap around by knocking off the ninth or (256) place

                #   0b111111110 -> 510
                #               &
                #   0b011111111 -> 255
                #   0b011111110 -> 254

                memory[pointer] = (current_value * 2) & 255
            elif josh == "josH":
                #shift all bits left
                #no wrapping needed, ending digit is dropped

                memory[pointer] >>= 1
            elif josh == "JOsh":
                #print the character associated with
                #the value in the current memory cell

                print(end = chr(memory[pointer]) )
            elif josh == "jOsh":
                #clear current memory cell
                memory[pointer] = 0
            elif josh == "JOSh":
                #raise current cell value by the power of 2
                #grab first 8 bits: Goto line 39 for reference

                memory[pointer] = (current_value ** 2) & 255
            elif josh == "jOSh":
                #same as JOSh but its cubed
                
                memory[pointer] = (current_value ** 3) & 255
            elif josh == "JosH":
                #print the number associated with
                #the value in the current memory cell

                print(end = str(current_value))
            elif josh == "JoSH":
                #read number from standard input stream
                #and store in the current cell

                new_value = int(input())

                if new_value < 0 or new_value >= 255:
                    error("Number must be in range of [0, 255]")
                    break

                memory[pointer] = new_value
            elif josh == "joSH":
                #increment pointer position within memory limits
                #grab first 8 bits: Goto line 40 for reference

                pointer = (pointer + 1) & 255
            elif josh == "joSh":
                #decrement pointer position within memory limits
                #grab first 8 bits: Goto line 40 for reference

                pointer = (pointer - 1) & 255
            elif josh == "JoSh":
                #beginning of a loop, determine the contents of the loop and execute until
                #current cell's value is 0

                #grab code from the beginning of the loop indicator to the end of list
                later_code = valid_code[index:]

                #with the sliced list count each encloser and return the corresponding one.
                contents = find_loop(later_code)

                #grab from just in front of the first indicator
                #all the way to just before the end loop indicator
                after_loop = valid_code[ (index + len(contents) + 2): ]

                #execute the contents until pointer is on an element with a value of 0
                while memory[pointer] > 0:
                    interpret_code(contents)
                break
            elif josh == "jOsH":
                #this is the end loop case
                pass
            elif josh == "JOsH":
                #this reads actual chars from input rather than ints
                if rem_input:
                    #takes remaining inputted value
                    new_value = ord(rem_input) if len(rem_input) == 1 else ord(rem_input[0])
                    if len(rem_input) > 1:
                        rem_input = rem_input[1:]
                    else:
                        rem_input = ""
                    if 0 < new_value < 255:
                        memory[pointer] = new_value
                    else:
                        error("Character's ASCII value must be in range of [0, 255]")
                else:
                    val = input()
                    new_value = ord(val) if len(val) == 1 else ord(val[0])
                    if len(val) > 1:
                        rem_input = val[1:]
                    #takes first inputted value
                    if 0 < new_value < 255:
                        memory[pointer] = new_value
                    else:
                        error("Character's ASCII value must be in range of [0, 255]")
            else:
                error("{} // Not valid .jsh code".format(josh))
        if after_loop:
            interpret_code(after_loop)
    else:
        error("Code is not 100% josh, ensure there is no unintended spacing.")


def find_loop(code):
    """ from a given list return the appropiate instructions within the loop
        count each enclosure until the matching enclosure is found.
        A loop to prevent nested loops interfering with the end enclosure
    """

    index = 0
    counter = 0
    while True:
        find = code[counter]
        if find == "JoSh":
            index+=1
        elif find == "jOsH":
            index-=1
        if index == 0:
            return code[1:counter]
        counter+=1


def remove_ignored(code):
    """remove comments and ignored characters from the inputted code"""

    regex = compile("\([^\)]*\)")
    comments = findall(regex,code)

    for findings in comments + ignored_chars:
        code = code.replace(findings, "")   #remove each findings
    return code


def validate_code(code):
    """ checks if code meets .jsh standards
        this is done by removing any comments or ignored characters
        checking if the left source is divisible by 4 using bit operations
        then manually checking if each word is a valid josh command

        if all these checks are met it will return a list of each command
    """

    #remove any ignored characters for interpretation
    code = remove_ignored(code)

    dis_by_4 = len(code) % 4

    # 00001000 -> 8
    #          &
    # 00000100 -> 3
    # 00000000 -> 0

    if dis_by_4 != 0:
        return False

    josh_list = findall("....?",code)

    #search through each 4 letter "word" to check if it valid .jsh code
    for josh in josh_list:
        if josh.lower() != "josh":
            return False
    return josh_list


def error(message):
    """custom error handler"""

    print("JoshScript Error // " + message)


def openfile(filename):
    """open then given file and run in the .jsh interpreter"""

    data = open(filename, "r")  #open in read only
    data = data.read()          #read the contents

    interpret_code(data)


def run_program():
    """ if there are no arguments passed initially then interpret
        compatible .jsh source code through the python interpreter
        otherwise try the first argument. if this is a file interpret
        it otherwise throw the given arguments
    """

    global values, pointer

    if len(argv) == 1:
        try:
            while True:
                memory = [0]*256
                pointer = 0

                interpret_code(input("\n>>> "))
        except:
            error("Unknown Error :(")
    else:
        try:
            current_file = argv[1]
            openfile(current_file)
        except:
            error("Unknown Error :(")

print(end = "JoshScript 1.3\n> ")
run_program()
