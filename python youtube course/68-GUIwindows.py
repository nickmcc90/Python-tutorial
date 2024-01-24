
# timestamp 6:12:45 boutta insert iconphoto function.

from tkinter import *

# windows = serves as a container to hold or contain these widgets.
# widgets = GUI elements: buttons, textboxes, labels, images

window = Tk() #instantiate an instance of a window
window.geometry("420x420") # width and height of window
window.title("Nick first GUI program") # changes title

icon = PhotoImage(file='star-rod.jpg') # to use photos, we need this function to convert any photo to a useable image.

window.mainloop() # this statement prints the window when you use the powershell, listens for events.