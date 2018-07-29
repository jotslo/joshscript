# E-Script
A simple language that anyone can learn.  
 \- with operations like low-level computer programming and based  
on (a forked version of) the original idea, [JoshScript](https://github.com/JoshSCF/JoshScript), in my [branch](https://github.com/user-e/E-Script/tree/original-JoshScript).

- Installation guide: https://www.youtube.com/watch?v=VGpngPR3lUc
- Download (from here): https://github.com/user-e/E-Script/archive/master-version.zip

A *huge* thanks to derns#5715 (https://github.com/upshaw) for completely rewriting the source code  
which was published as version 1.2. He also released the language-josh package on the atom text editor!  
This allows you to get your syntax highlighted when writing code in JoshScript.

## What's new?
JoshScript 1.3 has been released and contains a new code which cubes the value.

**Release history - new in older versions:**  
JoshScript 1.2.2 release contained a few bug fixes and updated functions.  
JoshScript 1.2 included a new ability to loop! Examples and usage will be coming soon.

## Operations for usage ("codes")
 \- uses 4 characters, each from a group of 2-8 ascii (basic latin) characters.  
`eoo1` / "JOSH" increases the value by 1

`eo-1` / "josh" decreases the value by 1

`eox2` / "Josh" multiplies the value by 2

`eod2` / "josH" divides the value by 2, rounding down to the nearest integer

`eopc` / "JOsh" outputs the ascii symbol with Unicode number equal to current value

`eooi` / "JoSH" takes integers as input and sets the value to that

`eoic` / "JOsH" takes characters as input and sets the value to ascii number of char

`eooo` / "jOsh" resets the value to 0

`eoxx` / "JOSh" squares the value

`exxx` / "jOSh" cubes the value

`eoop` / "JosH" outputs the current value (aka. print/echo)

`eoom` / "joSH" moves one to the right on the tape reel of values (aka. memory)

`eo-m` / "joSh" moves one to the left on the tape reel of values (aka. memory)

`eol1` / "JoSh" starts loop if the value is not 0, else jump to matching end loop tag

`eolo` / "jOsH" ends a loop

`(` starts notation space

`)` ends notation space

## Examples
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
## Instructions
1. If _execute_script.bat_ has the text "D:\Documents\Dev\JoshScript\source\JoshScript.py",  
change it to "E-Script.py" (originally named _JoshScript.py_) - uses the relative file path  
of your downloaded folder.

2. Open a text editor, write a program using E-Script codes above, then click "Save As".

3. Change the file type to "All Files" and name your program anything  
you would like that ends in _.jsh_, for example "program1.jsh".

4. To run your program, open the text file with _execute_script.bat_.  
(find it using your file manager's "choose another app" or "browse" option)

Your E-Script code should now run successfully.  
(Note: you need Python 3.6 installed for this to work)

## About this language
In this section, there's some information about this language that could  
help to answer questions about it, or the original version called *JoshScript*,  
for example *"why was it created?"* and *"what can it be used for?"*.
