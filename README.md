# wasdInfo
wasdInfo displays weather you are pressing your WASD keys and/or left and right mouse buttons onto your screen through PyQt5 (Python wrapper for Qt5).

# How to use

To use this, simply run the executable (or the `cli.py` file if you are running this through Python) and boom! It works. To modify the settings look at `C:\dogesupremacy` and look for the `settings.json` file and all the settings will be available to be configured in there.

# How to build

To build this, you will need to install PyInstaller. This can be done with `pip` (apart from Python) by doing `pip install pyinstaller`. Once you have done this simply run the `build.bat` file if you are on Windows (as it is easier) or run ```pyinstaller cli.py --noconfirm --onefile --name WasdInfo --icon icon.ico --noconsole``` (add `--paths ./venv/Lib/site-packages` or your path to site-packages if you're using a venv) if you are not (or want to do it yourself).

## Automation note

The .bat build automation files are configures to use a venv. To remove the venv path remove:

```
 --paths ./venv/Lib/site-packages
```

<br>

To change it just change ` --paths ./venv/Lib/site-packages`.
