import pyautogui #you should install it
import time
from tkinter import *  #you should install it

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

root = Tk()
root.title("Pipetka")
rgbstr = StringVar()
rgbstr.set("smt")
hex = StringVar()
hex.set("smt")
pos = StringVar()
pos.set("smt")

rad = 50


rgb = Label(root, width=30, bg="blue", textvariable=rgbstr)
rgb.pack()

hexl = Label(root, width=30, bg="blue", textvariable=hex)
hexl.pack()

posl = Label(root, width=30, bg="blue", textvariable=pos)
posl.pack()

canvas = Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="blue")
canvas.pack()

while True:
    x, y = pyautogui.position()
    r, g, b = pyautogui.pixel(x, y)

    rgbstr.set(str(r) + " " + str(g) + " " + str(b) + " ")
    hex.set(rgb_to_hex((r, g, b)))
    pos.set(str(x) + " " + str(y))

    canvas.create_oval(100 - rad, 100 - rad, 100 + rad, 100 + rad, fill=rgb_to_hex((r, g, b)))

    root.update()
    time.sleep(0.1)