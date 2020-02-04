import csv #Importamos el modelo de para archivos csv
#        (nombre del archivo, modo escritura) y los renombramos
with open('lenguajes.csv', mode='w' ) as lenguajes:
    #Declaramos la variable que contendrá el objeto; lenguaje_writer
    """método para escribir csv.write(nombrearchivo, delimitador(separador de los campos),
    caracter que rodeará el contenido de los campos, escribirá los campos solo si
    contienen el delimitador o el quotechar)"""
    lenguaje_writer = csv.writer(lenguajes, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #writerow: Escribira cada uno de los elementos separados por columnas
    lenguaje_writer.writerow(['Lenguaje', 'Año', 'Aplicación'])
    lenguaje_writer.writerow(['C++', 1979, 'Microcontroladores'])
    lenguaje_writer.writerow(['Python', 1991, 'Data Science'])
    lenguaje_writer.writerow(['Javascript', 1995, 'WEB'])
