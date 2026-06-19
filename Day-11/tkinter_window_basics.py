#GUI-->first file
#creating a simple window
from tkinter import*
root=Tk()
root.title('my first gui: ')
#root.geometry('300x200')
root.geometry('300x300+100+50')
root.mainloop()
#without mainloop(), the window will appear and disappear immediately