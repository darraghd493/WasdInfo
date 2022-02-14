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


class MouseDetector:
    def __init__(self):
        self.leftDown = win32api.GetKeyState(0x01)
        self.rightDown = win32api.GetKeyState(0x02)
        self.thread = threading.Thread(target=self.__updateLoop__)
        self.threadStarted = False

    @staticmethod
    def __convertButtonState__(state):
        if state < 0:
            return True
        else:
            return False

    def __update__(self):
        leftState = win32api.GetKeyState(0x01)
        rightState = win32api.GetKeyState(0x02)

        if not leftState == self.leftDown:
            self.leftDown = leftState

        if not rightState == self.rightDown:
            self.rightDown = rightState

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

    def isLeftDown(self):
        if self.threadStarted:
            return self.__convertButtonState__(self.leftDown)
        else:
            return self.__convertButtonState__(win32api.GetKeyState(0x01))

    def isRightDown(self):
        if self.threadStarted:
            return self.__convertButtonState__(self.rightDown)
        else:
            return self.__convertButtonState__(win32api.GetKeyState(0x02))


class WASDDetector:
    def __init__(self):
        self.wDown = False
        self.aDown = False
        self.sDown = False
        self.dDown = False
        self.thread = threading.Thread(target=self.__updateLoop__)
        self.threadStarted = False

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

    def __update__(self):
        wState = self.__equalCheck__('w')
        aState = self.__equalCheck__('a')
        sState = self.__equalCheck__('s')
        dState = self.__equalCheck__('d')

        if not wState == self.wDown:
            self.wDown = wState

        if not aState == self.aDown:
            self.aDown = aState

        if not sState == self.sDown:
            self.sDown = sState

        if not dState == self.dDown:
            self.dDown = dState

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

    def isWDown(self):
        if self.threadStarted:
            return self.__convertButtonState__(self.wDown)
        else:
            return self.__convertButtonState__(self.__equalCheck__('w'))

    def isADown(self):
        if self.threadStarted:
            return self.__convertButtonState__(self.aDown)
        else:
            return self.__convertButtonState__(self.__equalCheck__('a'))

    def isSDown(self):
        if self.threadStarted:
            return self.__convertButtonState__(self.sDown)
        else:
            return self.__convertButtonState__(self.__equalCheck__('s'))

    def isDDown(self):
        if self.threadStarted:
            return self.__convertButtonState__(self.dDown)
        else:
            return self.__convertButtonState__(self.__equalCheck__('d'))

    def isWhatDown(self, character):
        return self.__convertButtonState__(self.__equalCheck__(character))


class WKeyFrame(QWidget):
    def __init__(self, x, y, wasdDetector):
        QWidget.__init__(self)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint |
            QtCore.Qt.ToolTip
        )
        self.setWindowOpacity(settings['Buttons']['W']['Opacity'])
        self.setStyleSheet(settings['Buttons']['W']['Style'])
        self.setGeometry(x, y, 75, 75)
        self.setDisabled(True)
        self.setMode(False)

        self.label = QLabel(settings['Buttons']['W']['Text'], self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet(settings['Buttons']['W']['TextStyle'])
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.setLayout(self.layout)

        self.wasdDetector = wasdDetector

        self.thread = threading.Thread(target=self.__updateLoop__)
        self.threadStarted = False

    def __update__(self):
        self.setMode(self.wasdDetector.isWDown())

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
            self.setWindowOpacity(settings['Buttons']['W']['OpacityActive'])
        else:
            self.setWindowOpacity(settings['Buttons']['W']['Opacity'])
        self.show()


class AKeyFrame(QWidget):
    def __init__(self, x, y, wasdDetector):
        QWidget.__init__(self)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint |
            QtCore.Qt.ToolTip
        )
        self.setWindowOpacity(settings['Buttons']['A']['Opacity'])
        self.setStyleSheet(settings['Buttons']['A']['Style'])
        self.setGeometry(x, y, 75, 75)
        self.setDisabled(True)
        self.setMode(False)

        self.label = QLabel(settings['Buttons']['A']['Text'], self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet(settings['Buttons']['A']['TextStyle'])
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.setLayout(self.layout)

        self.wasdDetector = wasdDetector

        self.thread = threading.Thread(target=self.__updateLoop__)
        self.threadStarted = False

    def __update__(self):
        self.setMode(self.wasdDetector.isADown())

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
            self.setWindowOpacity(settings['Buttons']['A']['OpacityActive'])
        else:
            self.setWindowOpacity(settings['Buttons']['A']['Opacity'])
        self.show()


class SKeyFrame(QWidget):
    def __init__(self, x, y, wasdDetector):
        QWidget.__init__(self)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint |
            QtCore.Qt.ToolTip
        )
        self.setWindowOpacity(settings['Buttons']['S']['Opacity'])
        self.setStyleSheet(settings['Buttons']['S']['Style'])
        self.setGeometry(x, y, 75, 75)
        self.setDisabled(True)
        self.setMode(False)

        self.label = QLabel(settings['Buttons']['S']['Text'], self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet(settings['Buttons']['S']['TextStyle'])
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.setLayout(self.layout)

        self.wasdDetector = wasdDetector

        self.thread = threading.Thread(target=self.__updateLoop__)
        self.threadStarted = False

    def __update__(self):
        self.setMode(self.wasdDetector.isSDown())

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
            self.setWindowOpacity(settings['Buttons']['S']['OpacityActive'])
        else:
            self.setWindowOpacity(settings['Buttons']['S']['Opacity'])
        self.show()


class DKeyFrame(QWidget):
    def __init__(self, x, y, wasdDetector):
        QWidget.__init__(self)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint |
            QtCore.Qt.ToolTip
        )
        self.setWindowOpacity(settings['Buttons']['D']['Opacity'])
        self.setStyleSheet(settings['Buttons']['D']['Style'])
        self.setGeometry(x, y, 75, 75)
        self.setDisabled(True)
        self.setMode(False)

        self.label = QLabel(settings['Buttons']['D']['Text'], self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet(settings['Buttons']['D']['TextStyle'])
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.setLayout(self.layout)

        self.wasdDetector = wasdDetector

        self.thread = threading.Thread(target=self.__updateLoop__)
        self.threadStarted = False

    def __update__(self):
        self.setMode(self.wasdDetector.isDDown())

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


class LeftButtonFrame(QWidget):
    def __init__(self, x, y, mouseDetector):
        QWidget.__init__(self)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint |
            QtCore.Qt.ToolTip
        )
        self.setWindowOpacity(settings['Buttons']['LeftButton']['Opacity'])
        self.setStyleSheet(settings['Buttons']['LeftButton']['Style'])
        self.setGeometry(x, y, 115, 50)
        self.setDisabled(True)
        self.setMode(False)

        self.label = QLabel(settings['Buttons']['LeftButton']['Text'], self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet(settings['Buttons']['LeftButton']['TextStyle'])
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.setLayout(self.layout)

        self.mouseDetector = mouseDetector

        self.thread = threading.Thread(target=self.__updateLoop__)
        self.threadStarted = False

    def __update__(self):
        self.setMode(self.mouseDetector.isLeftDown())

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
            self.setWindowOpacity(settings['Buttons']['LeftButton']['OpacityActive'])
        else:
            self.setWindowOpacity(settings['Buttons']['LeftButton']['Opacity'])
        self.show()


class RightButtonFrame(QWidget):
    def __init__(self, x, y, mouseDetector):
        QWidget.__init__(self)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint |
            QtCore.Qt.ToolTip
        )
        self.setWindowOpacity(settings['Buttons']['RightButton']['Opacity'])
        self.setStyleSheet(settings['Buttons']['RightButton']['Style'])
        self.setGeometry(x, y, 115, 50)
        self.setDisabled(True)
        self.setMode(False)

        self.label = QLabel(settings['Buttons']['RightButton']['Text'], self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet(settings['Buttons']['RightButton']['TextStyle'])
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.setLayout(self.layout)

        self.mouseDetector = mouseDetector

        self.thread = threading.Thread(target=self.__updateLoop__)
        self.threadStarted = False

    def __update__(self):
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
            self.setWindowOpacity(settings['Buttons']['RightButton']['OpacityActive'])
        else:
            self.setWindowOpacity(settings['Buttons']['RightButton']['Opacity'])
        self.show()


class ExitButton(QWidget):
    def __init__(self, wasdDetector):
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

        self.wasdDetector = wasdDetector

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
        print(f"taskkill /f /im \"{__file__}\"")
        os.system(f"taskkill /f /im \"{__file__}\"")
        print(f"taskkill /f /im \"{os.getpid()}\"")
        os.system(f"taskkill /f /im \"{os.getpid()}\"")
        print(f"taskkill /f /im \"{os.getppid()}\"")
        os.system(f"taskkill /f /im \"{os.getppid()}\"")
        print("taskkill /f /im \"python.exe\"")
        os.system("taskkill /f /im \"python.exe\"")

def main():
    keyX = 75 + 5
    keyY = 75 + 5
    buttonX = 115 + 5
    buttonY = 75 + 5

    app = QApplication(sys.argv)
    wPart = WKeyFrame(settingsManager.getXOffset(keyX * 2), settingsManager.getYOffset(keyY), WASDDetector())
    aPart = AKeyFrame(settingsManager.getXOffset(keyX), settingsManager.getYOffset(keyY * 2), WASDDetector())
    sPart = SKeyFrame(settingsManager.getXOffset(keyX * 2), settingsManager.getYOffset(keyY * 2), WASDDetector())
    dPart = DKeyFrame(settingsManager.getXOffset(keyX * 3), settingsManager.getYOffset(keyY * 2), WASDDetector())
    lbPart = LeftButtonFrame(settingsManager.getXOffset(buttonX - (buttonX - keyX)), settingsManager.getYOffset(buttonY * 3),
                             MouseDetector())
    rbPart = RightButtonFrame(settingsManager.getXOffset((buttonX * 2) - (buttonX - keyX)),
                              settingsManager.getYOffset(buttonY * 3), MouseDetector())
    exitButton = ExitButton(WASDDetector())

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