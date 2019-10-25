from flask import Flask #De flask importa la  clase flask

app = Flask(__name__) # creamos la varible app que contendra la instancia de flask

#Creamos la primer ruta
@app.route('/')#usando el decorador se define que cada peticion al servidor llevara en primer plano a la ruta hello 
def hello():
    return 'hello world flask'