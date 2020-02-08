import csv

with open('lenguajes.csv', newline='') as lenguajes:
    lenguajes_lectura = csv.reader(lenguajes, delimiter=',', quotechar='"')
    for row in lenguajes_lectura:
            print(row)
            print(', '.join(row))
