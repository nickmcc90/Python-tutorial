from tkinter import *

# entry widget = textbox that accepts a single line of user input.

def submit():
  username = entry.get()
  print("Hello "+username)
  entry.config(state="disabled") # disables the button after one use

def delete():
  entry.delete(0,END)

def backspace():
  entry.delete(len(entry.get())-1,END) # gets the length of the input, then removes the index 2nd to last


window = Tk()

entry = Entry(window,
              font=('Arial',50),
              fg="#00FF00",
              bg='black',
              show='*') # this gives us an entry box to put input into.
# show='*' displays only asteriks when user inputs stuff.

#entry.insert(0,"spongebob") already inserts text into the area


entry.pack(side=LEFT) # you can determine the side that the entry text appears on in the GUI

submit_button = Button(window,text='submit',command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text='delete',command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text='backspace',command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()