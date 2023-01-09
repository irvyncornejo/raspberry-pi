from tkinter import *
from time import sleep

root = Tk()
root.title('Registro de usuarios')
myFrame = Frame(root, width=1200, height=600)
myFrame.pack()

valorDeVariable = StringVar()
data = StringVar()
#Name
#grid posicijamiento de la reja
#sticky justificación del texto
#'
nameLabel = Label(myFrame, text='Ingresa tu nombre: ').grid(row=0, column=0, sticky='e', pady = 5)
textInputName = Entry(myFrame, justify='center').grid(row=0, column=1,  pady = 5)

#lastName
lastNameLabel = Label(myFrame, text='Ingresa tus apellidos: ').grid(row=1, column=0, sticky='e',  pady = 5)
textInputLastName = Entry(myFrame).grid(row=1, column=1,  pady = 5)

#Password
passwordLabel = Label(myFrame, text='Ingresa un contraseña').grid(row=2, column=0, sticky='e',  pady = 5)
textInputpassword = Entry(myFrame, show=' ').grid(row=2, column=1,  pady = 5)

#email
emailLabel = Label(myFrame, text='Ingresa tu correo electrónico').grid(row=3, column=0, sticky='e',  pady = 5)
textInputEmail = Entry(myFrame, textvariable = data).grid(row=3, column=1,  pady = 5)


scrollLateral = Scrollbar(myFrame)

#Comment
commentLabel = Label(myFrame, text='Ingresa una descripción: ').grid(row=4, column=0, sticky='e',  pady = 5)
textComment = Text(myFrame, width=30, height=10)
textComment.grid(row=4, column=1, sticky='e',  pady = 5)
textComment.config(yscrollcommand=scrollLateral.set)

#scroll
scrollLateral.config(command = textComment.yview)
scrollLateral.grid(row=4, column=2, sticky='nsew')

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