# timestamp: 6:45:47


from tkinter import *

window = Tk()

def display():
  if(x.get()==1):
    print("You agreed")
  else:
    print("You don't agree :(")


x = IntVar() # accepts a 1 or 0 value


check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=("Arial"),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00',
                           activebackground='black')

check_button.pack()


window.mainloop()