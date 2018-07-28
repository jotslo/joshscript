@echo off
title JoshScript 1.2.3
:: double-colon label = programming comment
:: https://en.wikipedia.org/wiki/List_of_DOS_commands#REM
:: Development file path shouldn't be used here, the
:: relative path of file in current folder is better.
py JoshScript.py %*
pause>nul
