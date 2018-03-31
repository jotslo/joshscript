# JoshScript
A simple language that anyone can learn.

- Installation guide: https://www.youtube.com/watch?v=VGpngPR3lUc
- Direct Download: http://www.joshl.io/downloads/joshscript.zip
- Download from here: https://github.com/JoshSCF/JoshScript/archive/master.zip

A *huge* thanks to derns#5715 (https://github.com/upshaw) for completely rewriting the source code,  
so I could publish it as version 1.2. He also released the language-josh package for the atom text editor!  
This allows you to get your syntax highlighted when writing code in JoshScript.

# What's new?
JoshScript 1.2.2 has been released and contains a few bug fixes and updated functions.
JoshScript 1.2 included a new ability to loop! Examples and usage will be coming soon.

# Usage
`JOSH` increases the value by 1

`josh` decreases the value by 1

`Josh` multiplies the value by 2

`josH` divides the value by 2, rounding down to the nearest integer

`JOsh` outputs the character for the current value - ascii/Basic Latin symbols

`JoSH` takes integers as input and sets the value to that

`JOsH` takes characters as input and sets the value to ascii repr. of char

`jOsh` resets the value to 0

`JOSh` squares the value

`JosH` outputs the current value

`joSH` moves one to the right on the tape reel

`joSh` moves one to the left on the tape reel

`JoSh` starts loop if the value is not 0, otherwise jump to matching end loop tag

`jOsH` ends the current loop

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
1. Edit _association.bat_ and change the path, D:\Documents\Dev\JoshScript\source\JoshScript.py,  
to the location of your "JoshScript.py".

2. Open a text editor, write a program in JoshScript and hit "Save As".

3. Change the file type to "All Files" and then name your program  
anything you would like that ends in _.jsh_, for example "my_program.jsh".

4. To run your program, open the text file with _association.bat_.

Your JoshScript code should now run successfully. (Note: you need to have Python 3.6 installed for this to work)
