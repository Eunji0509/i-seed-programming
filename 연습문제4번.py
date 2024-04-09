from tkinter import *
window = Tk()

button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")

button1.pack(side=LEFT) 
button2.pack(side=LEFT)
button3.pack(side=LEFT)

window.mainloop()

from tkinter import *
window = Tk()

button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")

button1.pack(side=RIGHT) 
button2.pack(side=RIGHT)
button3.pack(side=RIGHT)

window.mainloop()

from tkinter import *
window = Tk()

button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")

button1.pack(side=TOP) 
button2.pack(side=TOP)
button3.pack(side=TOP)

window.mainloop()

from tkinter import *
window = Tk()

button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")

button1.pack(side=BOTTOM) 
button2.pack(side=BOTTOM)
button3.pack(side=BOTTOM)

window.mainloop()
