from tkinter import *

root = Tk()
myFrame = Frame(root, width=1200, height=600)
myFrame.pack()

#Name
#grid posicijamiento de la reja
#sticky justificación del texto
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
textInputEmail = Entry(myFrame).grid(row=3, column=1,  pady = 5)

root.mainloop()