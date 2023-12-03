from matplotlib import pyplot
#Tuplas que contienen los valores
lenguajes = ('Python', 'C', 'Java', 'Go')
slices = (100, 130, 90, 50)
colores = ('red', 'blue', 'green', 'pink')
valores = (0.1, 0, 0, 0)#Para resaltar a Python de los demas

#Linea para evitar que la barra de herramientas salga en la parte de abajo
pyplot.rcParams['toolbar'] = 'None'

_, _, texto = pyplot.pie(slices, colors=colores, labels=lenguajes, autopct='%1.1f%%',
                         explode=valores,
                         startangle=90)
#iteración para que el color de las letras sea de color blanco
for text in texto:
    text.set_color('white')
    
pyplot.axis('equal')#Linea para hacer que la gráfica quede como un círculo perfecto
pyplot.title('Lenguajes de programación')
pyplot.show()#Para mostrar la  gráfica en la pantalla
pyplot.savefig('lenguajes.png')#Para guardar gráfica como una imagen