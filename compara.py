numero1=input("numero1:")
numero2=input("numero2:")
salida= "numeros proporcionados: {} y {}.{}."
if(numero==numero2):
    #entra aqui si los numeros son capturados son iguales
    print(salida.format(numero1, numero2, "los numeros son iguales"))
else:
    #condicionales anidadas, if dentro de otro if
    #  si los numeros no son iguales    
    if numero1>numero2:
    #reporta si el primer numero es mayor que el segundo
   print(salida.format(numero1, numero2,"el mayor es el primero"))
else:
    # o de lo contrario, si el primer numero no es mayor al segundo
    print(salida.format(numero1 ,numero2,"el mayor es el segundo"))