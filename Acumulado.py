#se declara las variables
acumulado=int(0)
numero=str("")

#si colocamos la variable while como condicion
# se creara un ciclo infinito que no se rompe hasta que de forma
#explicita se utilice la instruccion break
while True:
    numero=input("Dame un numero entero:")
    if numero=="":
#si el numero esta vacio, se sale despues de reportar la isntruccion
        print("Vacio, salida del programa.")
        break
    else:
# si se proporciona valor acumulado = acumulado + numero
#se realiza el calculo usando suma incluyente
        acumulado+=int(numero)
        salida="monto acumulado: {}"
        print(salida.format(acumulado))