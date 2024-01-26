from tkinter import *

def submit():
  print("The temperature is: "+ str(scale.get()) + " degrees C")


window = Tk()

hotImage = PhotoImage(file='star-rod.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()


scale = Scale(window,from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font=('Consolas',20),
              tickinterval=10, # adds numeric indicators for value
              resolution=5, #increment of slide
              troughcolor = '#69EAFF' #color of the slider area)
)

scale.set(((scale['from']-scale['to'])/2)+scale['to']) # this sets the slider in the middle of the scale no matter what.

scale.pack()


button = Button(window,
                text='submit',
                command=submit,
                )
button.pack()


# coldImage = PhotoImage(file='cold.png')
# coldLabel = Label(image=coldImage)
# coldLabel.pack()

window.mainloop()