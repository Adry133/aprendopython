for i in range (1,11):
    encabezado="tabla del {}"
    print(encabezado.format(i))
    #print sin argumentos es un salto de liena
    print ()
    #dentro de un for, puede colocarse otro
    for j in range (1,11):
        #aqui, i contiene el numero base de la tabla 
        #y j el elemento de la tabla 
        salida="{} x{} = {}"
        print(salida.format(i,j,i*j))
    else:
         #al concluir con las iteraciones indicadas
         #se podra ejecutar el codigo, que es un salto de liena.
         print()