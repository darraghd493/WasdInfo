@echo off
title WasdInfo Compiler
:::
::: \    / _  _ _|~|~ _  |` _
:::  \/\/ (_|_\(_|_|_| |~|~(_)
:::
::: Compiler - Build into multiple files (one directory)
:::
for /f "delims=: tokens=*" %%A in ('findstr /b ::: "%~f0"') do @echo(%%A
echo Starting build
echo.
pyinstaller cli.py ^
    --name WasdInfo --icon icon.ico --noconfirm --noconsole --onedir
echo.
echo Finished build
echo.
pause