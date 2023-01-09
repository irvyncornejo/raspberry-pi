from tkinter import *
from time import sleep

root = Tk()
root.title('Registro de usuarios')
myFrame = Frame(root, width=1200, height=600)
myFrame.pack()

scrollLateral = Scrollbar(myFrame)

#Comment
commentLabel = Label(myFrame, text='Ingresa una descripción: ').grid(row=4, column=0, sticky='e',  pady = 5)
textComment = Text(myFrame, width=30, height=10)
textComment.grid(row=4, column=1, sticky='e',  pady = 5)
textComment.config(yscrollcommand=scrollLateral.set)

#scroll
scrollLateral.config(command = textComment.yview)
scrollLateral.grid(row=4, column=2, sticky='nsew')
