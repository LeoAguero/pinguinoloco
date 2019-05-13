#creamos un archivo nuevo 
#guardamos en la carpeta del repositorio
#con la extencion .py 
#uso de numeros oleatorios
"""
#importamos la libreria randint
from random import randint 
aleatorio=randint(0,20) #creamos una variable y generamos un numero
#aleatorio entre 0 y 20
print(aleatorio)  #imprimimos el numero generado
"""
#ejercicio
#escribir una funcion sorteo() que reciba
#una lista de participantes, y elegir a uno de los
#participantes aleatoriamente, y retornar esa persona elegida

from random import randint 
def sorteo(lista_participantes):
    cant=len(lista_participantes)
    ganador=randint(0,cant)
return lista_participantes[ganador]
lista_participantes=["lili","gustavo","Jazmin","fernando"]
ganador=sorteo(lista_participantes)
print(ganador)
 


#Desafio: no volver a una persona ya sorteada
