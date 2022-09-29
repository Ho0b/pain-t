import math
from tkinter import colorchooser
from colormap import rgb2hex
from tkinter.colorchooser import askcolor
from tkinter.filedialog import FileDialog
from utils import *
from var import *

def draw(event):
    x1, y1 = (event.x-1), (event.y-1)
    x2, y2 = (event.x+1), (event.y+1)
    canv.create_line(x1,y1,x2,y2, fill=gotcolor)
    
def createCanv(x, y):
    intro.destroy()
    
    canv.configure(width=x, height=y, bg="gray")
    canv.place(relx=.5, rely=.5, anchor=CENTER)

def selectFile():
    fileTypes = (('png files', '*.png'),('All files', '*.*'))
    fN = FileDialog.askopenfilename(title="Open a File", initialdir="/", filetypes=fileTypes)
    
    photo = PhotoImage(file = fN)
    canv.create_image(0,0, image=photo, anchor=NW)

def getcords(e):
    x = e.x
    y = e.y
    
def follorCursor():
    canv.create_oval
    
# ----meanu functions---- 
def cut():
    pass

# -----------button functions-------

def Brush():
    pass
def Eraser():
    gotcolor = "gray"
def Clear():
    canv.delete("all")
def pickColor():
    currentColor = askcolor(title="Pick a color")
    gotcolor = str(currentColor[1])
    colorArray.append(currentColor[1])
    if len(colorArray) < 10:
        gotcolor = str(currentColor[1])
        Button(userColors, bg=currentColor[1], width=1, height=1, relief=GROOVE).pack(fill=X)
    else:
        gotcolor = str(currentColor[1])
        Button(userColors, bg=currentColor[1], width=1, height=1, relief=GROOVE)   
         
def swColors():
    gotcolor = Button['bg']
    print(gotcolor)
    