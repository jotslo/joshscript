@echo off
title JoshScript 1.3.0

:: double-colon = comment, https://en.wikipedia.org/wiki/List_of_DOS_commands#REM
:: Development file path shouldn't be used here, the relative
:: path of file in current folder is better. Or swap colons from
:: the next line to one after in non-Github version of this file.
:: py D:\Documents\Dev\JoshScript\source\JoshScript.py %*
py JoshScript.py %*

pause>nul
