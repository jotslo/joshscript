# JoshScript
A language that everyone can learn.

- Installation: https://www.youtube.com/watch?v=VGpngPR3lUc
- Direct Download: http://www.joshl.io/downloads/joshscript.zip

A **huge** thanks to derns#5715 (https://github.com/upshaw) for completely rewriting the source code for me to publish as 1.2. He also released the language-josh package on the atom text editor! This allows you to get your syntax highlighted when writing code in JoshScript.

# What's New?
JoshScript 1.2.3 has been released and contains a new josh, `jOSh` which cubes the value.

# Usage
**JOSH** increases the value by 1

**josh** decreases the value by 1

**Josh** multiplies the value by 2

**josH** divides the value by 2 and rounds down to the nearest integer

**JOsh** outputs the ascii repr. of the current value

**JoSH** takes integers as input and sets the value to that

**JOsH** takes characters as input and sets the value to ascii repr. of char

**jOsh** sets the value to 0

**JOSh** squares the value

**jOSh** cubes the value

**JosH** outputs the current value

**joSH** moves one to the right on the tape reel

**joSh** moves one to the left on the tape reel

**JoSh** starts loop if the value is not 0, otherwise jump to matching jOsH tag

**jOsH** ends loop

**(** starts notation space

**)** ends notation space

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
1. Edit association.bat and change the path, D:\Documents\Dev\JoshScript\source\JoshScript.py,  to the location of JoshScript.py

2. Open notepad, write a program in JoshScript and hit 'Save As'

3. Change the file type to 'All Files' and then name your program filename.jsh, filename being whatever name you would like to name your file

4. When opening the notepad file, open the file with association.bat

Your JoshScript code should now run successfully. (Note that you must have Python 3.6 installed for this to work)
