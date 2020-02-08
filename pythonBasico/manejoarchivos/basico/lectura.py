with open ('nombres.txt', 'w', newline='') as nombres:
    """for nombre in nombres:
        print(nombre)
print(nombres.readlines())"""
    datos = ['Alberto 9', 'Carlos 10']
    for dato in datos:
        nombres.write('{} '.format(dato))



