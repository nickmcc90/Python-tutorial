# timestamp: 7:21:20

# listbox = a listing of selectable text items within it's own container.

from tkinter import *

def submit(): # to get a current selected item of a listbox, theres a specific function to use.
  print("You have ordered: ")
  print(listbox.get(listbox.curselection()))

def add():
  listbox.insert(listbox.size(),entryBox.get()) # this retrieves an index number by calculating the size, and the information in the entry box.
  listbox.config(height=listbox.size()) # alters the height of our listbox according to how many items there are after adding

def delete():
  listbox.delete(listbox.curselection())
  listbox.config(height=listbox.size()) 

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia",35),
                  width=12, # we can make a height based on the amount of items that we have.
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,'pizza')
listbox.insert(2,'pasta')
listbox.insert(3,'garlic bread')
listbox.insert(4,'soup')
listbox.insert(5,'salad')


entryBox = Entry(window)
entryBox.pack()


submitButton = Button(window,text='submit',command=submit)
submitButton.pack()

addButton = Button(window,text='add',command=add)
addButton.pack()

deleteButton = Button(window,text='delete',command=delete)
deleteButton.pack()

window.mainloop()