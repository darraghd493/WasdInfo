import os
import json

defaultSettings = {"Body": {
    "X": 75,
    "Y": 75
}, "Buttons": {
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

settingsBaseFolderPath = "C:/dogesupremacy/"
settingsFolderPath = settingsBaseFolderPath + "WasdInfo/"
settingsFilePath = settingsFolderPath + "/settings.json"


def writeDefaultSettings():
    if not os.path.isdir(settingsBaseFolderPath):
        os.mkdir(settingsBaseFolderPath)
    if not os.path.isdir(settingsFolderPath):
        os.mkdir(settingsFolderPath)
    if os.path.isfile(settingsFilePath):
        os.remove(settingsFilePath)
    with open(settingsFilePath, "w") as settingsFile:
        settingsFile.write(json.dumps(defaultSettings, indent=4))

def getSettings():
    if os.path.isdir(settingsBaseFolderPath):
        if os.path.isdir(settingsFolderPath):
            if os.path.isfile(settingsFilePath):
                try:
                    with open(settingsFilePath, "r") as settingsFile:
                        return json.loads(settingsFile.read())
                except FileNotFoundError:
                    writeDefaultSettings()
                    return defaultSettings
            else:
                writeDefaultSettings()
                return defaultSettings
        else:
            writeDefaultSettings()
            return defaultSettings
    else:
        writeDefaultSettings()
        return defaultSettings


settings = getSettings()


def getXOffset(num):
    return num + settings['Body']['X']


def getYOffset(num):
    return num + settings['Body']['X']
