# importing whole module
from tkinter import *


# importing strftime function to retrieve system's time
from time import strftime

# creating tkinter window
root = Tk()
root.title('Tkinter Clock')
root.geometry("300x300")
frame=Frame(root,relief="groove",
              bd = 20, bg = 'skyblue')
frame.pack()
# This function is used to display time on the label
def time():
	string = strftime('%I:%M:%S %p')
	lbl.config(text = string)
	lbl.after(1000, time)

# Styling the label widget so that clock  will look more attractive
lbl = Label(frame,font = ('Timesnewroman', 20, 'bold'),
			background = 'pink',
			foreground = 'green',
                         width=45,height=10)

# Placing clock at the centre of the tkinter window
lbl.pack(anchor = 'center')
time()

mainloop()
