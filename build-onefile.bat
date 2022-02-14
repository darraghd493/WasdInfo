@echo off
title WasdInfo Compiler
:::
::: \    / _  _ _|~|~ _  |` _
:::  \/\/ (_|_\(_|_|_| |~|~(_)
:::
::: Compiler - Build into a single file
:::
for /f "delims=: tokens=*" %%A in ('findstr /b ::: "%~f0"') do @echo(%%A
echo Starting build
echo.
pyinstaller cli.py ^
    --name WasdInfo --icon icon.ico --noconfirm --noconsole --workspace=./build/onefile --distpath=./dist/onefile --onefile
echo.
echo Finished build
echo.
pause