
from utils import *

global center_x, center_y
global canvasWidth, canvasHeight
gotcolor = "white"

# windows var
intro = Tk()
root = Tk()
canv = Canvas(root)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# frame var

userColors = Frame(master=root, background="#FFFFFF")
presetColors = Frame(master=root, background="#32004f")

window_width = 1080
window_height = 1080

currentColor = "black"

# function variables

colorBtn = Button(userColors)
colorBtn2 = Button(presetColors)

colorArray = []

# preset colors
Button(presetColors, bg="#FFFFFF", width=1, height=1).pack() # white
Button(presetColors, bg="#fc0000", width=1, height=1).pack() # red
Button(presetColors, bg="#ff3300", width=1, height=1).pack() # orange
Button(presetColors, bg="#ffff66", width=1, height=1).pack() # yellow
Button(presetColors, bg="#66ff66", width=1, height=1).pack() # green
Button(presetColors, bg="#66ffcc", width=1, height=1).pack() # teal
Button(presetColors, bg="#3399ff", width=1, height=1).pack() # blue
Button(presetColors, bg="#9933ff", width=1, height=1).pack() # purple
Button(presetColors, bg="#6600ff", width=1, height=1).pack() # violet
Button(presetColors, bg="#000000", width=1, height=1).pack() # black





