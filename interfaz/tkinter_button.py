from tkinter import *
from time import sleep

root = Tk()
root.title('Registro de usuarios')
myFrame = Frame(root, width=1200, height=600)
myFrame.pack()


valorDeVariable = StringVar()
data = StringVar()

textInputEmail = Entry(myFrame, textvariable = data).grid(row=3, column=1,  pady = 5)

def funcion():  
    dato = (data.get()).lower()
    valorDeVariable.set(dato)
    print(dato)
    data.set('')

    
#Button
button = Button(myFrame, text= 'Enviar', command= funcion).grid(row=5, column=1)
textVariable = Entry(myFrame, textvariable = valorDeVariable).grid(row=6, column=1,  pady = 5)
variableLabel = Label(myFrame, textvariable = valorDeVariable).grid(row=7, column=1, sticky='e',  pady = 5)

if __name__ == '__main__':

    root.mainloop()
    