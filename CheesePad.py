import os, sys, inspect
from tkinter import *
import time
import pyautogui

class KeySim:
    def left_key_down():
        #PressKey(VK_LEFT)
        pyautogui.keyDown('left')

    def left_key_up():
        #ReleaseKey(VK_LEFT)
        pyautogui.keyUp('left')

    def right_key_down():
        #PressKey(VK_RIGHT)
        pyautogui.keyDown('right')

    def right_key_up():
        #ReleaseKey(VK_RIGHT)
        pyautogui.keyUp('right')

    def up_key_down():
        #PressKey(VK_UP)
        pyautogui.keyDown('up')

    def up_key_up():
        #ReleaseKey(VK_UP)
        pyautogui.keyUp('up')

    def down_key_down():
        #PressKey(VK_DOWN)
        pyautogui.keyDown('down')

    def down_key_up():
        #ReleaseKey(VK_DOWN)
        pyautogui.keyUp('down')

class App:
    up_string = '\u21D1'
    down_string = '\u21D3'
    left_string = '\u21D0'
    right_string = '\u21D2'
    up_right_string = '\u21D7'
    up_left_string = '\u21D6'
    down_right_string = '\u21D8'
    down_left_string = '\u21D9'

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.up = Button(frame, text=self.up_string, command=self.key_press, height='5', width='10')
        self.up.grid(row=0, column=1)
        self.left = Button(frame, text=self.left_string, command=self.key_press, height='5', width='10')
        self.left.grid(row=1, column=0)
        self.right = Button(frame, text=self.right_string, command=self.key_press, height='5', width='10')
        self.right.grid(row=1, column=2)
        self.down = Button(frame, text=self.down_string, command=self.key_press, height='5', width='10')
        self.down.grid(row=2, column=1)
        self.top_left = Button(frame, text=self.up_left_string, command=self.key_press, height='5', width='10')
        self.top_left.grid(row=0, column=0)
        self.down_left = Button(frame, text=self.down_left_string, command=self.key_press, height='5', width='10')
        self.down_left.grid(row=2, column=0)
        self.top_right = Button(frame, text=self.up_right_string, command=self.key_press, height='5', width='10')
        self.top_right.grid(row=0, column=2)
        self.down_right = Button(frame, text=self.down_right_string, command=self.key_press, height='5', width='10')
        self.down_right.grid(row=2, column=2)

        self.up.bind('<Enter>', self.key_hover)
        self.up.bind('<Leave>', self.key_leave_hover)

        self.left.bind('<Enter>', self.key_hover)
        self.left.bind('<Leave>', self.key_leave_hover)

        self.right.bind('<Enter>', self.key_hover)
        self.right.bind('<Leave>', self.key_leave_hover)

        self.down.bind('<Enter>', self.key_hover)
        self.down.bind('<Leave>', self.key_leave_hover)

        self.top_left.bind('<Enter>', self.key_hover)
        self.top_left.bind('<Leave>', self.key_leave_hover)

        self.down_left.bind('<Enter>', self.key_hover)
        self.down_left.bind('<Leave>', self.key_leave_hover)

        self.top_right.bind('<Enter>', self.key_hover)
        self.top_right.bind('<Leave>', self.key_leave_hover)

        self.down_right.bind('<Enter>', self.key_hover)
        self.down_right.bind('<Leave>', self.key_leave_hover)

    def parse_keys_down(self, widget):
        if widget.cget('text') == self.up_string:
            KeySim.up_key_down()
        elif widget.cget('text') == self.down_string:
            KeySim.down_key_down()
        elif widget.cget('text') == self.left_string:
            KeySim.left_key_down()
        elif widget.cget('text') == self.right_string:
            KeySim.right_key_down()
        elif widget.cget('text') == self.up_left_string:
            KeySim.left_key_down()
            KeySim.up_key_down()
        elif widget.cget('text') == self.up_right_string:
            KeySim.right_key_down()
            KeySim.up_key_down()
        elif widget.cget('text') == self.down_left_string:
            KeySim.left_key_down()
            KeySim.down_key_down()
        elif widget.cget('text') == self.down_right_string:
            KeySim.right_key_down()
            KeySim.down_key_down()

    def parse_keys_up(self, widget):
        if widget.cget('text') == self.up_string:
            KeySim.up_key_up()
        elif widget.cget('text') == self.down_string:
            KeySim.down_key_up()
        elif widget.cget('text') == self.left_string:
            KeySim.left_key_up()
        elif widget.cget('text') == self.right_string:
            KeySim.right_key_up()
        elif widget.cget('text') == self.up_left_string:
            KeySim.left_key_up()
            KeySim.up_key_down()
        elif widget.cget('text') == self.up_right_string:
            KeySim.right_key_up()
            KeySim.up_key_up()
        elif widget.cget('text') == self.down_left_string:
            KeySim.left_key_up()
            KeySim.down_key_up()
        elif widget.cget('text') == self.down_right_string:
            KeySim.right_key_up()
            KeySim.down_key_up()

    def key_press(self):
        print ("Test")

    def key_hover(self, event):
        event.widget.config(bg='green')
        self.parse_keys_down(event.widget)
        print ("Hover Test")

    def key_leave_hover(self, event):
        event.widget.config(bg='gray')
        self.parse_keys_up(event.widget)
        print ("Leave Hover Test")

    def key_double_press(self, event):
        print ("Double Click Test")

root = Tk()
root.title("CheesePad")
app = App(root)
root.attributes('-alpha', 0.3)
root.wm_attributes('-topmost', 1)
root.resizable(width=FALSE, height=FALSE)
root.mainloop()
root.destroy()
