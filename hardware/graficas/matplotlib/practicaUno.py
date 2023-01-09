import matplotlib.pyplot as plt

valorDolar = [ 19.6113, 19.5352, 19.5717, 19.5678, 19.4707,
               19.3688, 19.3688,19.3688, 19.3247, 19.2302,
               19.2362, 19.2362, 19.1785, 19.1785, 19.1785,
               19.0455, 18.9702, 18.9165, 18.9542, 18.9640,
               18.9640, 18.9640, 18.9133, 18.9385, 18.9385,
               18.9643, 18.9445, 18.9445,18.9445, 18.8452,
               18.8727, 20.000 ]
#datos = len(valorDolar)
plt.plot(valorDolar)
#plt.plot(valorDolar , 'ro')
#plt.axis([1, datos , 0, 21])
plt.title('Valor del dolar')
plt.ylabel('Valor del dolar')
plt.xlabel('Días de Diciembre')
#print(('{}').format(datos))
plt.show()