@echo off
title JoshScript 1.3.0
:: double-colon = comment, https://en.wikipedia.org/wiki/List_of_DOS_commands#REM
:: Development file path shouldn't be used here, the
:: relative path of file in current folder is better.
:: py D:\Documents\Dev\JoshScript\source\JoshScript.py %*
:: Or swap colons from previous line to next in dev file.
py JoshScript.py %*
pause>nul
