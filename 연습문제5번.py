from tkinter import *
from time import *

fnameList=["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif",
           "jeju7.gif", "jeju8.gif", "jeju9.gif"]
num=0

window=Tk()

def clickNext():
    global num
    num+=1
    if num>=len(fnameList):
        num=0
    pLabel.configure(text=fnameList[num])

def clickPrev():
    global num
    num-=1
    if num<0:
        num=len(fnameList)-1
    pLabel.configure(text=fnameList[num])

pLabel=Label(window, text=fnameList[num])
pLabel.pack()
    
nextButton=Button(window, text="다음", command=clickNext)
prevButton=Button(window, text="이전", command=clickPrev)

nextButton.pack(side=RIGHT)
prevButton.pack(side=LEFT)
window.mainloop()

