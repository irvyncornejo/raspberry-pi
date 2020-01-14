# -*- coding: utf-8 -*-

# Funcion para promediar el valor del dolar
def promedio_dolar(valores_dolar):
    # inicializamos el valor de la variable que alcenara el valor promedio del dolar
    promedio_valor_dolar = 0

    # iteracion para sumar cada uno de los elementos dentro de la lista
    for valor in valores_dolar:
        #Sumanos cada uno de los elementos obtenidos
        promedio_valor_dolar += valor
    return promedio_valor_dolar / len(valores_dolar)


# Está función define el inicio del programa
if __name__ == '__main__':
    # Valor de la lista con los valores propuestos en al ejercicio
    valores_dolar = [ 19.6113, 19.5352, 19.5717, 19.5678, 19.4707, 19.3688, 
                    19.3688,19.3688, 19.3247, 19.2302, 19.2362, 19.2362, 19.1785, 
                    19.1785, 19.1785, 19.0455, 18.9702, 18.9165, 18.9542, 18.9640, 
                    18.9640, 18.9640, 18.9133, 18.9385, 18.9385, 18.9643, 18.9445, 
                    18.9445,18.9445, 18.8452, 18.8727 ]

    promedio = promedio_dolar(valores_dolar)

    print('El valor promedio del dolar en Diciembre de 2019 fue {}'.format(promedio))