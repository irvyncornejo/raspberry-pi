from tkinter import *

#Raíz
root = Tk()
#Titulo
root.title('Ventana de prueba')
#Evitar que se redimencione o aceptar el redireccionaminto
root.resizable(True, True) #width | height
#Dimensionar la ventana de inicio
root.geometry('700x400')#width | height
#manejo de configuraciones más especificas 
root.config(bg='#f5f5f5')

root.mainloop()