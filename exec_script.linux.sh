#!/bin/bash
# exec_script.linux.sh / exec_script.mac.command : converted to a bash (shell) script from
# the file "execute_script.bat", for (Microsoft) Windows, to be used on the (GNU/)Linux OS
# or MacOS, if this file has "mac" in its name (to update that file, copy the one for Linux
# into it then edit it for MacOS using <https://stackoverflow.com/a/52651033/3787376>).
# How to convert the .bat file into this one:
# - On the blank line after this, add a new line, paste .bat file code, add two new lines.
# - Edit the new code, adding "# " at the start of .bat commands and "::" lines.
# - Then after each (commented out) .bat command, add a new line and the
#   equivalent bash script command - it could be copied from the older code.
# - Then delete that older code and two new lines above it.

# @echo off
# title JoshScript 1.3.0
PS1_old="$(echo $PS1 | sed -En 's/(.+)\\e](.+)/\1\\\\e]\2/g; s/(.+ )(.+)/\1\\n\2/p')";
_PS1='\[\e]0;$WTITLE: \w\a\]';_PS1+="$PS1_old ";export PS1=$_PS1;
export WTITLE="JoshScript 1.3.0"
# - from <https://superuser.com/a/1366261/736409>.

# :: double-colon = comment, https://en.wikipedia.org/wiki/List_of_DOS_commands#REM
# :: Development file path shouldn't be used here, the relative
# :: path of file in current folder is better. Or swap colons from
# :: the next line to one after in non-Github version of this file.
# :: py D:\Documents\Dev\JoshScript\source\JoshScript.py %*
# py JoshScript.py %*

if [ -e "$1" ]
then
    python3 JoshScript.py "$1"
    # - from <https://stackoverflow.com/a/3534315/3787376>.
else
    python3 JoshScript.py
fi
# Use input for script if filename argument is not a file.
# - based on <https://stackoverflow.com/a/40082454/3787376>.

# pause>nul
