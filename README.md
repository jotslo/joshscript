# JoshScript
A simple language that anyone can learn.

- Installation guide: https://www.youtube.com/watch?v=VGpngPR3lUc
- Website download: http://www.joshl.io/downloads/joshscript.zip
- Download from here: https://github.com/JoshSCF/JoshScript/archive/master.zip

A *huge* thanks to derns#5715 (https://github.com/upshaw) for completely rewriting the source code  
which was published as version 1.2. He also released the language-josh package on the atom text editor!  
This allows you to get your syntax highlighted when writing code in JoshScript.

# What's new?
JoshScript 1.2.3 has been released and contains a new josh, `jOSh` which cubes the value.

**Release history - new in older versions:**  
JoshScript 1.2.2 release contained a few bug fixes and updated functions.  
JoshScript 1.2 included a new ability to loop! Examples and usage will be coming soon.

# Usage codes
`JOSH` increases the value by 1

`josh` decreases the value by 1

`Josh` multiplies the value by 2

`josH` divides the value by 2, rounding down to the nearest integer

`JOsh` outputs the ascii symbol with Unicode number equal to current value

`JoSH` takes integers as input and sets the value to that

`JOsH` takes characters as input and sets the value to ascii number of char

`jOsh` resets the value to 0

`JOSh` squares the value

`jOSh` cubes the value

`JosH` outputs the current value

`joSH` moves one to the right on the tape reel of values

`joSh` moves one to the left on the tape reel of values

`JoSh` starts loop if the value is not 0, else jump to matching end loop tag

`jOsH` ends a loop

`(` starts notation space

`)` ends notation space

# Examples
```
JOSHJoshJoshJoshJoshJoshJoshJOSHJOsh
```
`> A`

```
JOSHJoshJoshJosh (hiya)JoshJoshJoshJOSHJOsh
```
`> A`

```
JOSHJOSHJOSHJoshJoshJoshJoshJOshJOSHJOshJOSHJOshJOSHJOshJOSHJOshJOSHJOshJOSHJOshJOSHJOshJOSHJOshJOSHJOshJOSH
```
`> 0123456789`

```
JOSHJoshJoshJoshJoshJoshJoshJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOshjoshjoshjoshjoshjoshjoshjoshjoshjoshjoshjoshjoshjoshjoshjoshjoshjoshjoshjoshjoshjoshjoshJoshJOSHJOshJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOshJOshJOSHJOSHJOSHJOshjosHjoshjoshjoshjoshjoshjoshjoshjoshjoshjoshjoshJOshjosHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOshjoshjoshjoshjoshjoshjoshjoshjoshjoshjoshJoshJoshjoshJOshJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOshJOSHJOSHJOSHJOshjoshjoshjoshjoshjoshjoshJOshjoshjoshjoshjoshjoshjoshjoshjoshJOshjosHjosHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOSHJOsh
```
`> Hello, World!`
# Instructions
1. If _execute_script.bat_ has the text "D:\Documents\Dev\JoshScript\source\JoshScript.py",  
change it to "JoshScript.py" (uses the relative file path of your downloaded folder).

2. Open a text editor, write a program using JoshScript codes above, then click "Save As".

3. Change the file type to "All Files" and name your program anything  
you would like that ends in _.jsh_, for example "program1.jsh".

4. To run your program, open the text file with _execute_script.bat_.  
(find it using your file manager's "choose another app" or "browse" option)

Your JoshScript code should now run successfully.  
(Note: you need Python 3.6 installed for this to work)

//Note: I should now check preview, add commit title and description from notes, remove this line, then save changes.
