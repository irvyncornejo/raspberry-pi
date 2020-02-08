import csv 

"""TODO 
    Declarar la variable para el led que se activará al registrar a un nuevo usuario
"""

def crearUsuario(nombre, apellido, edad, contador):
    if float(edad) >= 18:
        mayorEdad = True
    else:
        mayorEdad = False

    usuario = [nombre, apellido, edad, mayorEdad]
    print(usuario)
    """
        Read    = 'r' | 'read'
        Write   = 'w' | 'write'
        Append  = 'a' | 'a+'
        Read and Write =  'r+'
    """
    with open('registro.txt', mode='w' , newline='') as registro:
        registro_usuarios = csv.writer(registro, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        registro_usuarios.writerow(usuario)

if __name__ == '__main__':
    contador = 0
    cantidadDatos = 2
    while contador < cantidadDatos:
        nombre = input('Ingresa el nombre: ')
        apellido = input('Ingresa apellido: ')
        edad = input('Ingresa la edad: ')
        contador += 1
        crearUsuario(nombre, apellido, edad, contador)