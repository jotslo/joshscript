#!/bin/bash
# exec_script.linux.sh / exec_script.mac.command : converted to a bash (shell) script
# from the file "execute_script.bat" for use on the (GNU/)Linux OS or Mac OS, if this
# file has "mac" in its name (to update that file, copy the one for Linux into it
# then edit it for Mac OS using <https://stackoverflow.com/a/52651033/3787376>).

#@echo off
#.bat file:# title JoshScript 1.3.0
[add title bash equivalent here] JoshScript 1.3.0

#:: double-colon = comment, https://en.wikipedia.org/wiki/List_of_DOS_commands#REM
#:: Development file path shouldn't be used here, the relative
#:: path of file in current folder is better. Or swap colons from
#:: the next line to one after in non-Github version of this file.
#:: py D:\Documents\Dev\JoshScript\source\JoshScript.py %*
#.bat file:# py JoshScript.py %*
python3 JoshScript.py [add something here for Unix input args (a filename)]
#pause>nul
