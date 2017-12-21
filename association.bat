@echo off
title JoshScript 1.2
:: double-colon label = programming comment
:: https://en.wikipedia.org/wiki/List_of_DOS_commands#REM
:: Use relative filename (current folder) for Python file so it's easier.
py JoshScript.py %*
pause>nul
