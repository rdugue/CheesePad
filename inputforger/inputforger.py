import ctypes
import time
from .sendkeys_hack import *

KEY_MAP = {
    'up': 0xC8,
    'down': 0xD0,
    'left': 0xCB,
    'right': 0xCD
}


def PressKey(key):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, KEY_MAP[key], 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(key):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, KEY_MAP[key], 0x0008 | 0x0002,
                        0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def KeyTap(key):
    time.sleep(.5)
    PressKey(key)  # press Q
    time.sleep(.05)
    ReleaseKey(key)  # release Q
