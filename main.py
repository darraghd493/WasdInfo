import enum
import os
import sys
import win32api
import threading
import time
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
import settingsManager

settings = settingsManager.getSettings()


class MouseButton(enum.Enum):
    Left = "LeftButton"
    Right = "RightButton"


class MouseDetector:
    def isLeftDown(self):
        return win32api.GetKeyState(0x01)&0x8000 > 0

    def isRightDown(self):
        return win32api.GetKeyState(0x02)&0x8000 > 0

    def isWhatDown(self, button):
        if button == MouseButton.Left:
            return win32api.GetKeyState(0x01)&0x8000 > 0
        else:
            return win32api.GetKeyState(0x02)&0x8000 > 0


class WASDDetector:
    @staticmethod
    def __equalCheck__(character):
        lowerCharacter = character.lower()
        upperCharacter = character.upper()

        checkResult = win32api.GetAsyncKeyState(ord(lowerCharacter))
        if not checkResult:
            checkResult = win32api.GetAsyncKeyState(ord(upperCharacter))

        return checkResult

    @staticmethod
    def __convertButtonState__(state):
        if state < 0:
            return True
        else:
            return False

    def isWDown(self):
        return self.__convertButtonState__(self.__equalCheck__('w'))

    def isADown(self):
        return self.__convertButtonState__(self.__equalCheck__('a'))

    def isSDown(self):
        return self.__convertButtonState__(self.__equalCheck__('s'))

    def isDDown(self):
        return self.__convertButtonState__(self.__equalCheck__('d'))

    def isWhatDown(self, character):
        return self.__convertButtonState__(self.__equalCheck__(character))


class KeyFrame(QWidget):
    def __init__(self, x, y, letter):
        letter = letter.upper()
        self.letter = letter
        self.wasdDetector = WASDDetector()

        QWidget.__init__(self)

        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint |
            QtCore.Qt.ToolTip
        )
        self.setWindowOpacity(settings['Buttons'][letter]['Opacity'])
        self.setStyleSheet(settings['Buttons'][letter]['Style'])
        self.setGeometry(x, y, 75, 75)
        self.setDisabled(True)
        self.setMode(False)

        self.label = QLabel(settings['Buttons'][letter]['Text'], self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet(settings['Buttons'][letter]['TextStyle'])
        self.layout = QGridLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.thread = threading.Thread(target=self.__updateLoop__)
        self.threadStarted = False

    def __update__(self):
        self.setMode(self.wasdDetector.isWhatDown(self.letter))

    def __updateLoop__(self):
        while True:
            self.__update__()
            time.sleep(0.001)

    def startThread(self):
        self.thread = threading.Thread(target=self.__updateLoop__)
        self.thread.start()
        self.threadStarted = True

    def stopThread(self):
        self.thread.join()
        self.threadStarted = False

    def setMode(self, mode):
        if mode:
            self.setWindowOpacity(settings['Buttons'][self.letter]['OpacityActive'])
        else:
            self.setWindowOpacity(settings['Buttons'][self.letter]['Opacity'])
        self.show()


class ButtonFrame(QWidget):
    def __init__(self, x, y, button):
        button = button.value
        self.button = button
        self.mouseDetector = MouseDetector()

        QWidget.__init__(self)

        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint |
            QtCore.Qt.ToolTip
        )
        self.setWindowOpacity(settings['Buttons'][button]['Opacity'])
        self.setStyleSheet(settings['Buttons'][button]['Style'])
        self.setGeometry(x, y, 115, 50)
        self.setDisabled(True)
        self.setMode(False)

        self.label = QLabel(settings['Buttons'][button]['Text'], self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet(settings['Buttons'][button]['TextStyle'])
        self.layout = QGridLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.thread = threading.Thread(target=self.__updateLoop__)
        self.threadStarted = False

    def __update__(self):
        if self.button == MouseButton.Left.value:
            self.setMode(self.mouseDetector.isLeftDown())
        else:
            self.setMode(self.mouseDetector.isRightDown())

    def __updateLoop__(self):
        while True:
            self.__update__()
            time.sleep(0.001)

    def startThread(self):
        self.thread = threading.Thread(target=self.__updateLoop__)
        self.thread.start()
        self.threadStarted = True

    def stopThread(self):
        self.thread.join()
        self.threadStarted = False

    def setMode(self, mode):
        if mode:
            self.setWindowOpacity(settings['Buttons'][self.button]['OpacityActive'])
        else:
            self.setWindowOpacity(settings['Buttons'][self.button]['Opacity'])
        self.show()


class ExitButton(QWidget):
    def __init__(self):
        self.wasdDetector = WASDDetector()
        QWidget.__init__(self)

        if settings['Buttons']['Exit']['TopMost']:
            self.setWindowFlags(
                QtCore.Qt.WindowStaysOnTopHint |
                QtCore.Qt.FramelessWindowHint |
                QtCore.Qt.X11BypassWindowManagerHint
            )
        else:
            self.setWindowFlags(
                QtCore.Qt.FramelessWindowHint |
                QtCore.Qt.X11BypassWindowManagerHint
            )

        self.setWindowOpacity(settings['Buttons']['Exit']['Opacity'])
        self.setStyleSheet(settings['Buttons']['Exit']['Style'])
        self.setGeometry(0, 0, 180, 50)
        self.setDisabled(False)

        self.button = QPushButton('Exit WASDInfo', self)
        self.button.setToolTip('Kills python.exe to exit WASDInfo')
        self.button.setStyleSheet(settings['Buttons']['Exit']['ButtonStyle'])
        self.button.clicked.connect(self.onClick)
        self.layout = QGridLayout()
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.thread = threading.Thread(target=self.__updateLoop__)
        self.threadStarted = False
        self.keyPressed = False

    def __toggle__(self):
        if self.isHidden():
            self.show()
        else:
            self.hide()

    def __update__(self):
        if self.wasdDetector.isWhatDown(settings['Buttons']['Exit']['Keybind']):
            if not self.keyPressed:
                self.__toggle__()
                self.keyPressed = True
        else:
            self.keyPressed = False

    def __updateLoop__(self):
        while True:
            self.__update__()
            time.sleep(0.001)

    def startThread(self):
        self.thread = threading.Thread(target=self.__updateLoop__)
        self.thread.start()
        self.threadStarted = True

    def stopThread(self):
        self.thread.join()
        self.threadStarted = False

    def setMode(self, mode):
        if mode:
            self.setWindowOpacity(settings['Buttons']['D']['OpacityActive'])
        else:
            self.setWindowOpacity(settings['Buttons']['D']['Opacity'])
        self.show()

    @pyqtSlot()
    def onClick(self):
        os.system(f"taskkill /f /im \"{__file__}\"")
        os.system(f"taskkill /f /im \"{os.getpid()}\"")
        os.system(f"taskkill /f /im \"{os.getppid()}\"")
        os.system("taskkill /f /im \"python.exe\"")


def main():
    keyX = 75 + 5
    keyY = 75 + 5
    buttonX = 115 + 5
    buttonY = 75 + 5

    app = QApplication(sys.argv)
    wPart = KeyFrame(settingsManager.getXOffset(keyX * 2), settingsManager.getYOffset(keyY), 'w')
    aPart = KeyFrame(settingsManager.getXOffset(keyX), settingsManager.getYOffset(keyY * 2), 'a')
    sPart = KeyFrame(settingsManager.getXOffset(keyX * 2), settingsManager.getYOffset(keyY * 2), 's')
    dPart = KeyFrame(settingsManager.getXOffset(keyX * 3), settingsManager.getYOffset(keyY * 2), 'd')
    lbPart = ButtonFrame(settingsManager.getXOffset(buttonX - (buttonX - keyX)),
                         settingsManager.getYOffset(buttonY * 3), MouseButton.Left)
    rbPart = ButtonFrame(settingsManager.getXOffset((buttonX * 2) - (buttonX - keyX)),
                         settingsManager.getYOffset(buttonY * 3), MouseButton.Right)
    exitButton = ExitButton()

    wPart.show()
    wPart.startThread()
    aPart.show()
    aPart.startThread()
    sPart.show()
    sPart.startThread()
    dPart.show()
    dPart.startThread()
    lbPart.show()
    lbPart.startThread()
    rbPart.show()
    rbPart.startThread()
    exitButton.startThread()
    exitButton.show()
    exitButton.hide()

    app.exec_()


if __name__ == '__main__':
    main()
