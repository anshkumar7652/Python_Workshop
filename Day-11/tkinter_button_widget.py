from tkinter import*
def display():
    print('button clicked')
root=Tk()
root.title('my first gui')
root.geometry('300x300+100+50')

btn=Button(root,text='click me',command=display)


#when clicked ,the console displays:
btn=Button(root,
        text='submit',
        fg='white',
        bg='blue',
        width=15,
        height=2)
btn.pack()
root.mainloop()