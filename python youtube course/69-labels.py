from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='star-rod.png')

label = Label(window,text="Hello World",font=('Arial',
                                              40,'bold'),
                                              fg='#00FF00',
                                              bg='black',
                                              relief=RAISED,
                                              bd=10,
                                              padx=20,
                                              pady=20,
                                              image=photo,
                                              compound='bottom') 
#this alone doesn't place the text, you need the label.pack(). font arial sized 40 and bold. fg means foreground which is 
# just the font color. bg is background of the text area. relief is a border appearance property. bd is border width
# padx and pady are padding. image=photo adds the image to our label. compound bottom sets image on bottom



label.pack()
#label.place(x=0,y=0) this places the stuff at a certain spot.

window.mainloop()