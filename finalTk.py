from tkinter import *
import random
import time
import requests, json, sys, pprint, contextlib

#text Definitions
text1 = '''Welcome to Heroes Online, an interactive game where you get to create your own
character based on one of four types of super powers: fire, air, water, and earth.
What is your name?'''

#function definitions
def myClick():
    top.set('''Thanks, ''' + e.get() + '''. What type of character would you like to create?
Fire (f), water (w), earth (e) or air (a)?''')
    e.delete(0, END)


root = Tk()
root.title("Hi Alex I love you")
width = root.winfo_screenwidth() // 2
height = root.winfo_screenheight() // 2
x = width - (height // 2)
y = height - (width // 2)
#edit height and width to change size of window
root.geometry('{}x{}+{}+{}'.format(width,height, x, y))

#this variable is the text string at the top of the screen
top = StringVar()
Label(root, textvariable=top).pack()
top.set(text1)

#this is the entry form for information choices
e = Entry(root, width=35,borderwidth=5)
e.pack()

buttonLabel = StringVar()
Button(root, textvariable = buttonLabel, command = myClick).pack()
#myButton = Button(root, text ='Enter your name!', command = myClick, fg = 'blue', bg = 'red')
buttonLabel.set("Enter")
#myButton.pack()

name=e.get()
print(name)

#start = Label(root, text=text1, font= 'Helvetica')
#start.pack()



root.mainloop()


