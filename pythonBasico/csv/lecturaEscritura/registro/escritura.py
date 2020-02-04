import csv 

nombres = list()
apellidos = list()
edades = list()


with open('registro.csv', mode='w' ) as registro:
    registro_usuarios = csv.writer(registro, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    registro_usuarios.write([nombres])
    registro_usuarios.writerow([apellidos])
    registro_usuarios.writerow([edades])

if __name__ == '__main__':
    contador = 0
    cantidadDatos = 2
    while contador < cantidadDatos  :
        nombre = input('Ingresa el nombre: ')
        apellido = input('Ingresa apellido: ')
        edad = input('Ingresa la edad: ')

        nombres.append(nombre)
        apellidos.append(apellido)
        edades.append(edad)
        contador += 1

    

    print(nombres)
    print(apellidos)
    print(edades)



