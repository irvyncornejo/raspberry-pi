from tkinter import *

root = Tk()
#Titulo
root.title('Ventana de prueba')
#Evitar que se redimencione o aceptar el redireccionaminto
root.resizable(True, True) #width | height
#Dimensionar la ventana de inicio
root.geometry('700x400')#width | height
#manejo de configuraciones más especificas
#background
root.config(bg='#f5f5f5')
root.mainloop()