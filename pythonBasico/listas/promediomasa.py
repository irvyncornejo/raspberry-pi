# -*- coding: utf-8 -*-
#Zona de paquetes o dependencias

#Zona de funciones
def pedirNombre():
    nombre = input('Ingresa el nombre de la persona: ')
    nombre = nombre.lower()
    letras = list(nombre)
    letras[0] = letras[0].upper()
    nombre = ''.join(letras)
    return nombre

def pedirMasa():
    masa = float(input('Ingresa el valor de su masa: '))
    return masa

def calcularPromedio(masas):
    promedioMasas = 0
    for masa in masas:
        promedioMasas += masa
    return promedioMasas / len(masas)

def redondeoNumero(cantidadDatos):
    return round(cantidadDatos)

cantidadDatos = float(input('Ingresa la cantidad de datos que necesitas: '))

if __name__ == "__main__":
    
    #Inicializamos nuestras variables
    masas = list()
    nombres = []
    cuenta = 0;
    cantidad = redondeoNumero(cantidadDatos)
    #ciclo para la iteracion 
    while cuenta < cantidad:
        nombre = pedirNombre()
        masa = pedirMasa()
        nombres.append(nombre)
        masas.append(masa)
        cuenta += 1
        #cuenta = cuenta + 1 #contador de personas
        #Lineas para hacer pruebas
        #print('{}'.format(cuenta))
        #print(nombres)
        #print(masas)
    #Funciones a ejecutarse despues de cumplir la cantidad de datos necesarios 
    promedioMasas = calcularPromedio(masas)
    #
    print('El promedio de los datos es: {}'.format(round (promedioMasas, 3)))

    