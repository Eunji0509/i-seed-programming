
from tkinter import *
import random as rd

btnList=[None]*9
fnameList=["honey.gif", "jellybean.gif", "marshmellow.gif", "oreo.gif", "robot.gif",
           "robotchoco.gif", "robotchoco_dark.gif", "rollypop.gif", "snack.gif"]

rd.shuffle(fnameList)
photoList=[None]*9
i, k = 0, 0
xPos, yPos = 0, 0
num=0

window=Tk()
window.geometry("210x210")

for i in range(0, 9):
    photoList[i]=PhotoImage(file="gif/"+fnameList[i])
    btnList[i]=Button(window, image=photoList[i])

for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].place(x=xPos, y=yPos)
        num+=1
        xPos+=70
    xPos=0
    yPos+=70

window.mainloop()
