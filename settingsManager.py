import os
import json

defaultSettings = {'Body': {
    "X": 75,
    "Y": 75
}, 'Buttons': {
    "W": {
        "Style": "background-color: rgb(22, 22, 22);",
        "TextStyle": "color: rgb(225, 225, 225);font-size:18px;",
        "Text": "W",
        "Opacity": 0.6,
        "OpacityActive": 0.9
    },
    "A": {
        "Style": "background-color: rgb(22, 22, 22);",
        "TextStyle": "color: rgb(225, 225, 225);font-size:18px;",
        "Text": "A",
        "Opacity": 0.6,
        "OpacityActive": 0.9
    },
    "S": {
        "Style": "background-color: rgb(22, 22, 22);",
        "TextStyle": "color: rgb(225, 225, 225);font-size:18px;",
        "Text": "S",
        "Opacity": 0.6,
        "OpacityActive": 0.9
    },
    "D": {
        "Style": "background-color: rgb(22, 22, 22);",
        "TextStyle": "color: rgb(225, 225, 225);font-size:18px;",
        "Text": "D",
        "Opacity": 0.6,
        "OpacityActive": 0.9
    },
    "LeftButton": {
        "Style": "background-color: rgb(44, 44, 44);",
        "TextStyle": "color: rgb(225, 225, 225);font-size:18px;",
        "Text": "LB",
        "Opacity": 0.6,
        "OpacityActive": 0.9
    },
    "RightButton": {
        "Style": "background-color: rgb(44, 44, 44);",
        "TextStyle": "color: rgb(225, 225, 225);font-size:18px;",
        "Text": "RB",
        "Opacity": 0.6,
        "OpacityActive": 0.9
    },
    "Exit": {
        "Style": "background-color: rgb(22, 22, 22);border: none;",
        "ButtonStyle": "background-color: rgb(44, 44, 44);color: rgb(215, 215, 215);border: none;padding: 3px;",
        "Opacity": 0.7,
        "Keybind": "G",
        "TopMost": True
    }
}}

settingsFilePath = "./settings.json"


def writeDefaultSettings():
    if os.path.isfile(settingsFilePath):
        os.remove(settingsFilePath)
    with open(settingsFilePath, "w") as settingsFile:
        settingsFile.write(json.dumps(defaultSettings))


def getSettings():
    if os.path.isfile(settingsFilePath):
        try:
            with open(settingsFilePath, "r") as settingsFile:
                json.loads(settingsFile.read())
        except BaseException:
            writeDefaultSettings()
            return defaultSettings
    else:
        writeDefaultSettings()
        return defaultSettings
    return defaultSettings


settings = getSettings()


def getXOffset(num):
    return num + settings['Body']['X']


def getYOffset(num):
    return num + settings['Body']['X']
