#en python existren diversas librerias que estan listas para utilizar
#a estas librerias se les conoce como modulos (module)
#para lograr utilizar in modulo en un programa 
#primero debe importarse, usando la instruccion import
import random

#se define una variable float, y se le asigna un valor
numero1=float(10.5)

#en python, una funcion es un conjunto de instrucciones que 
#porcesan una tarea especifica, como una unidad de ejecucion.
#tambien se tienen que declarar con def. todo el codigo que esta posicionado a la derecha 
#de la definicion, tambien forma parte lo que es la funcion.
def miFuncion():
    #Esto se genera que se convierta en float el numero aleatorio generado por
    #random.randrange() (solo si este esta disponible y si se importa 
    #el mdoulo random)
    numero2=float(random.randrange(1,10))
    #se utiliza meta sustituciones, para mostrar resultados.
    mensaje="la suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))

    #se ejecuta la funcion
    miFuncion()