import win32api
import time
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

class Keylogger(object):
    VKEY = {
        'VK_BACK': 0x8, # Backspace
        'VK_TAB': 0x9, # Tab
        'VK_RETURN': 0xD, # Enter, Numpad Enter
        'VK_PAUSE': 0x13, # Pause Break
        'VK_CAPITAL': 0x14, # Caps Lock
        'VK_HANGUL': 0x15, # Hangul
        'VK_HANJA': 0x19, # Hanja
        'VK_ESCAPE': 0x1B, # Esc
        'VK_SPACE': 0x20, # Space Bar
        'VK_PRIOR': 0x21, # Page Up
        'VK_NEXT': 0x22, # Page Down
        'VK_END': 0x23, # End
        'VK_HOME': 0x24, # Home
        'VK_LEFT': 0x25, # LEFT Arrow
        'VK_UP': 0x26, # UP Arrow
        'VK_RIGHT': 0x27, # RIGHT Arrow
        'VK_DOWN': 0x28, # DOWN Arrow
        'VK_SNAPSHOT': 0x2C, # Print Screen
        'VK_INSERT': 0x2D, # Insert
        'VK_DELETE': 0x2E, # Delete
        '0': 0x30,
        '1': 0x31,
        '2': 0x32,
        '3': 0x33,
        '4': 0x34,
        '5': 0x35,
        '6': 0x36,
        '7': 0x37,
        '8': 0x38,
        '9': 0x39,
        'A': 0x41,
        'B': 0x42,
        'C': 0x43,
        'D': 0x44,
        'E': 0x45,
        'F': 0x46,
        'G': 0x47,
        'H': 0x48,
        'I': 0x49,
        'J': 0x4A,
        'K': 0x4B,
        'L': 0x4C,
        'M': 0x4D,
        'N': 0x4E,
        'O': 0x4F,
        'P': 0x50,
        'Q': 0x51,
        'R': 0x52,
        'S': 0x53,
        'T': 0x54,
        'U': 0x55,
        'V': 0x56,
        'W': 0x57,
        'X': 0x58,
        'Y': 0x59,
        'Z': 0x5A,
        'VK_LWIN': 0x5B, # Left Windows
        'VK_RWIN': 0x5C, # Right Windows
        'VK_APPS': 0x5D, # Applications
        'VK_NUMPAD0': 0x60,
        'VK_NUMPAD1': 0x61,
        'VK_NUMPAD2': 0x62,
        'VK_NUMPAD3': 0x63,
        'VK_NUMPAD4': 0x64,
        'VK_NUMPAD5': 0x65,
        'VK_NUMPAD6': 0x66,
        'VK_NUMPAD7': 0x67,
        'VK_NUMPAD8': 0x68,
        'VK_NUMPAD9': 0x69,
        'VK_MULTIPLY': 0x6A, # Numpad *
        'VK_ADD': 0x6B, # Numpad +
        'VK_SUBTRACT': 0x6D, # Numpad -
        'VK_DECIMAL': 0x6E, # Numpad .
        'VK_DIVIDE': 0x6F, # Numpad /
        'VK_F1': 0x70,
        'VK_F2': 0x71,
        'VK_F3': 0x72,
        'VK_F4': 0x73,
        'VK_F5': 0x74,
        'VK_F6': 0x75,
        'VK_F7': 0x76,
        'VK_F8': 0x77,
        'VK_F9': 0x78,
        'VK_F10': 0x79,
        'VK_F11': 0x7A,
        'VK_F12': 0x7B,
        'VK_NUMLOCK': 0x90, # Num Lock
        'VK_SCROLL': 0x91, # Scroll Lock
        'VK_LSHIFT': 0xA0, # Left Shift
        'VK_RSHIFT': 0xA1, # Right Shift
        'VK_LCONTROL': 0xA2, # Left Ctrl
        'VK_RCONTROL': 0xA3, # Right Ctrl
        'VK_LMENU': 0xA4, # Left Alt
        'VK_RMENU': 0xA5, # Right Alt
        'VK_OEM_1': 0xBA, # ;
        'VK_OEM_PLUS': 0xBB, # +
        'VK_OEM_COMMA': 0xBC, # ,
        'VK_OEM_MINUS': 0xBD, # -
        'VK_OEM_PERIOD': 0xBE, # .
        'VK_OEM_2': 0xBF, # /
        'VK_OEM_3': 0xC0, # `
        'VK_OEM_4': 0xDB, # [
        'VK_OEM_5': 0xDC, # \
        'VK_OEM_6': 0xDD, # ]
        'VK_OEM_7': 0xDE # '
        }

    def __init__(self):
        self.swapKeyCode = dict((value, key) for key, value in Keylogger.VKEY.items()) # Swap key, value --> value, key
        # self.pressCount = [0 for x in range(223)]
        # self.isPressed = [False for x in range(223)]
        self.pressCount = dict((key, 0) for key in Keylogger.VKEY.keys())
        self.__isPressed = dict((key, False) for key in Keylogger.VKEY.keys())

    def main(self):
        while True:
            for i in range(8, 223): # Virtual Key Codes 8 ~ 222
                if i not in self.swapKeyCode.keys():
                    continue
                if win32api.GetAsyncKeyState(i) & 0x8000 and not self.__isPressed[self.swapKeyCode[i]]:
                    self.__isPressed[self.swapKeyCode[i]] = True
                    print(self.swapKeyCode[i])
                    self.pressCount[self.swapKeyCode[i]] += 1
                    if i == 0x23:
                        return self.pressCount
                elif win32api.GetAsyncKeyState(i) == 0:
                    self.__isPressed[self.swapKeyCode[i]] = False
            time.sleep(0.01)

class Graph(object):
    def __init__(self):
        font_name = font_manager.FontProperties(fname="C:/Users/SEAN/AppData/Local/Microsoft/Windows/Fonts/NanumBarunGothic.ttf").get_name()
        rc('font', family=font_name)

        plt.xlabel('주요 키')
        plt.ylabel('빈도수')
        plt.grid(True)

    def main(self, keyInfo):
        self.Sorted_Dict_Values = sorted(keyInfo.values(), reverse=True)
        self.Sorted_Dict_Keys = sorted(keyInfo, key=keyInfo.get, reverse=True)

        plt.bar(range(len(keyInfo)), self.Sorted_Dict_Values, align='center')
        plt.xticks(range(len(keyInfo)), list(self.Sorted_Dict_Keys), rotation='70')

        plt.show()

if __name__ == "__main__":
    myClass = Keylogger()
    myClass2 = Graph()
    myClass2.main(myClass.main())
