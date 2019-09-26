entrada=input()
print(type(entrada))
#la variable booleana tiende a dar el resuktado de verificar
#si lo capturado es algun digito , y si no se encuentra un punto
#en lo que se esta capturando estariamos indicando que se trata de ub 
#numero con decimales, a lo que queremos decur, float. si find retorna -1
#quiere darnos a entender que lo esta buscandi, en esre caso un punto decimal
#no se encontro. si esEntero es True, lo capturado es entero.
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if (esEntero):
    #Lineas que se ejecutan si la condicion es verdadera (true)
    print("Dato entero. ¡Muy bien!")
else: 
        #lineas  que se ejecutaran si la condicion llegara a ser falsa (false)
        print("Dato no es entero.Intentar de nuevo.")