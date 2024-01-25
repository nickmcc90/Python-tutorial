from tkinter import *

window = Tk()

count = 0

def click():
  global count
  count += 1
  print(count)

photo = PhotoImage(file='star-rod.png')

# be sure not to include the () in the function commnad call
button = Button(window,
                text='click me',
                command=click,
                font=('comic sans',30),
                fg='#00FF00',
                bg='color',
                activeforeground="00FF00",
                activebackground="black",
                image=photo,
                compound='bottom')
button.pack()


window.mainloop()