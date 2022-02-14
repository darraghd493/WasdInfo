# wasdInfo
wasdInfo displays weather you are pressing your WASD keys and/or left and right mouse buttons onto your screen through PyQt5 (Python wrapper for Qt5).

# How to use
To use this, simply run the executable (or the `cli.py` file if you are running this through Python) and boom! It works. To modify the settings look at where the file was executed for the `settings.json` file and all of the settings will be avaliable to be configured in there.

# How to build
To build this, you will need to install PyInstaller. This can be done with `pip` (apart of Python) by doing `pip install pyinstaller`. Once you have done this simply run the `build.bat` file if you are on Windows (as it is easier) or run ```pyinstaller cli.py --noconfirm --onefile --name WasdInfo --icon icon.ico --noconsole``` if you are not (or want to do it yourself).
