@echo off
title JoshScript 1.2.3
:: double-colon label = programming comment
:: https://en.wikipedia.org/wiki/List_of_DOS_commands#REM
:: Don't add development file path, a relative filename
:: uses the Python file in current folder which is better.
py JoshScript.py %*
pause>nul
