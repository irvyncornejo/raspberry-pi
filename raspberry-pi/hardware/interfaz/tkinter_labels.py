from tkinter import *

root = Tk()

myFrame = Frame(root, width ='800', height= '500')

myFrame.pack()

title = Label(myFrame, text='Divisas', fg='#2f3848', font=('Roboto', 20)).place(x='370')

imageFrame = PhotoImage(file='documentar.png')

Label(myFrame, image=imageFrame).place(x=370)

root.mainloop()