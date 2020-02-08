import csv
import matplotlib.pyplot as plt

listaDatos = list()
"""with open ('temperatura.csv', newline = '') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        #print(row)
        print(', '.join(row))"""

with open('temperatura.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if row != 0:
            listaDatos.append(row[1])
            #print(row[1])
    listaDatos = listaDatos[1:]
    #print(len(listaDatos))
    plt.plot(listaDatos)
    #plt.plot(valorDolar , 'ro')
    #plt.axis([1, datos , 0, 21])
    plt.title('LM35')
    plt.ylabel('Temperatura')
    plt.xlabel('INtervalo')
    #print(('{}').format(datos))
    plt.show()
