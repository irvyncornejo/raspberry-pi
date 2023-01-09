from tkinter import *

#Raíz
root = Tk()
#Titulo
root.title('Frame test')
#Evitar que se redimencione o aceptar el redireccionaminto
root.resizable(True, True) #width | height
#Dimensionar la ventana de inicio
#root.geometry('700x400')#width | height
#manejo de configuraciones más especificas 
root.config(bg='#f5f5f5')

#Frame

myFrame = Frame()
#empaquetamos el frame en la raíz para no tener elementos separados
#Dentro del método pack podemos colocar los valores para definir que el frame se autoajuste a que se alinie según sea el caso
myFrame.pack(fill='both', expand=True)

#myFrame.config()
myFrame.config(bg='#2f3848', width='650', height='300', cursor='hand2')
root.mainloop()