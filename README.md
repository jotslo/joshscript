# E-Script
A simple language that anyone can learn.  
 \- based on the original idea, [JoshScript](https://github.com/JoshSCF/JoshScript).

- Installation guide: https://www.youtube.com/watch?v=VGpngPR3lUc
- Download: https://github.com/user-e/E-Script/archive/master-version.zip

A huge thanks to derns#5715 (https://github.com/upshaw) for completely rewriting the source code  
which was published as version 1.2. He also released the language-josh package on the atom text editor!  
This allows you to get your syntax highlighted when writing code in JoshScript.

## What's new?
JoshScript 1.2.2 has been released and contains a few bug fixes and updated functions.  
JoshScript 1.2 included a new ability to loop! Examples and usage will be coming soon.

## Operations (usage)
 \- uses 2-3 characters from ascii/basic latin.

`e+` _"JOSH"_ increases the value by 1

`e-` _"josh"_ decreases the value by 1

`e2x` _"Josh"_ multiplies the value by 2

`e2d` _"josH"_ divides the value by 2, rounding down to the nearest integer

`ep` _"JOsh"_ outputs the ascii symbol with Unicode number equal to current value

`e=` _"JoSH"_ takes integers as input and sets the value to that

`ec=` _"JOsH"_ takes characters as input and sets the value to ascii number of char

`e0` _"jOsh"_ resets the value to 0

`exx` _"JOSh"_ squares the value

`ep=` _"JosH"_ outputs the current value (print/echo)

`et+` _"joSH"_ moves one to the right on the tape reel of values

`et-` _"joSh"_ moves one to the left on the tape reel of values

`el` _"JoSh"_ starts loop if the value is not 0, else jump to matching end loop tag

`eL` _"jOsH"_ ends a loop

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
1. Edit _association.bat_ and change the path, D:\Documents\Dev\JoshScript\source\JoshScript.py,  
to the file path of your downloaded "E-Script.py" file _(named JoshScript.py previously)_.

2. Open a text editor, write a program using operations above, then click "Save As".

3. Change the file type to "All Files" and name your program anything  
you would like that ends in _.jsh_, for example "my_program.jsh".

4. To run your program, open the text file with _association.bat_.  
 (find it using your file manager's "choose another app" or "browse" option)

Your E-Script code should now run successfully.  
(Note: you need Python 3.6 installed for this to work)
