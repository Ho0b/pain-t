
from cProfile import label
from cgitb import text
from re import A
from turtle import left
from utils import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter.colorchooser import askcolor
from colormap import rgb2hex
from PIL import ImageTk, Image
from var import *
from funct import *

# -------------intro SCREEN----------

introScreenWidth,introScreenHeight = intro.winfo_screenwidth(), intro.winfo_screenheight()
introWindowWidth, introWindowHeight = 500, 500
center_x_intro = int(introScreenWidth/2 - introWindowWidth / 2)
center_y_intro = int(introScreenHeight/2 - introWindowHeight / 2)

intro.geometry(f"{introWindowWidth}x{introWindowHeight}+{center_x_intro}+{center_y_intro}")
intro.resizable(False,False)
intro.configure(background="#3a015c")
intro.overrideredirect(True)
intro.attributes("-topmost", 1)
ttk.Label(text="Width").place(x=125, y=250)
ttk.Label(text="height").place(x=125, y=300)

canvasWidth = Entry(background="gray",fg="white").place(x=300, y=250)
canvasHeight = Entry(background="gray",fg="white").place(x=300, y=300)

ttk.Button(intro, text="cancel", command=intro.destroy).place(x=125, y=450)
ttk.Button(intro, text="create", command=lambda:createCanv(canvasWidth,canvasHeight)).place(x=300, y=450)

# -------------main WINDOW-----------

root.title("pain't")

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False,False)
root.overrideredirect(True)
root.configure(background="#11001c")

# ------------FRAME SECT------------
toolFrame = Frame(root, width=1280 , height=100, bg="#32004f")
toolFrame.place(x=140, y=0)
toolFrame.configure(relief=GROOVE)
toolFrame.pack_propagate(False)

userColors.configure(width=70)
userColors.pack(side=LEFT, fill=Y)
userColors.pack_propagate(False)
Label(userColors,text="your colors", width=50, bg="#FFFFFF").pack()
Label(presetColors, text="default colors", width=50 , bg="#FFFFFF").pack()
presetColors.configure(width=70)
presetColors.pack(side=LEFT, fill=Y)
presetColors.pack_propagate(False)


canv.bind('<B1-Motion>', draw)
canv.bind('<Motion>', getcords)

colorBtn.configure(command=swColors)
colorBtn2.configure(command=swColors)

# ----------------menubar--------------
mainMenu = Menu(root)
mainMenu.config(background='#32004f', fg='white')
root.config(menu=mainMenu)

fMenu = Menu(mainMenu, tearoff="off")
mainMenu.add_cascade(label="File", menu=fMenu)
fMenu.add_command(label="New", command=selectFile)
fMenu.add_command(label="Exit", command=root.destroy)


# eMenu = Menu(mainMenu)
# mainMenu.add_cascade(label="Edit", menu=eMenu)
# eMenu.add_command(label="Cut", command=)
# eMenu.add_separator()
# eMenu.add_command(label="Copy", command=)
# eMenu.add_separator()
# eMenu.add_command(label="Paste", command=)

# ----------------buttons------------------
ttk.Button(toolFrame, text="Exit", command=root.destroy).pack(side=LEFT)
ttk.Button(toolFrame, text="Brush", command=Brush).pack(side=LEFT)
ttk.Button(toolFrame, text="Eraser", command=Eraser).pack(side=LEFT)
ttk.Button(toolFrame, text="Clear", command=Clear).pack(side=LEFT)
ttk.Button(toolFrame, text="Pick Color", command=pickColor).pack(side=LEFT)



intro.mainloop()