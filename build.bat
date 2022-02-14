@echo off
title WasdInfo Compiler
:::
::: \    / _  _ _|~|~ _  |` _
:::  \/\/ (_|_\(_|_|_| |~|~(_)
:::
::: Compiler - Build into multiple files (multiple directories)
:::
for /f "delims=: tokens=*" %%A in ('findstr /b ::: "%~f0"') do @echo(%%A
echo Starting build
echo.
pyinstaller cli.py ^
    --name WasdInfo --icon icon.ico --noconfirm --noconsole --workpath=./build/normal --distpath=./dist/normal --paths ./venv/Lib/site-packages
echo.
echo Finished build
echo.
pause