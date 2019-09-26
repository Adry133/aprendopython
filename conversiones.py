#se declara una b¿variable string, como una cadena en la que lleva digitos 
numero= "5678"
#enseguida se muestra el tipo de variable que sera de salida que en este caso seria type ()
#Ojo no es un str, es un dato type
print(type(numero))
#se convierte la cadena  a su valor equivalente int.
numero=int(numero)

#se muestra como el tipo ha cambiado, sin embargo seguimos conservando la misma variable
print(type(numero))
#se declara un str con situacion (posiciones donde iran 
#valores proporcionados usando format.
salida= "El numero utilizado es {}"
#se muestra el resultado obtenido. la meta situacion gara que donde esra 
#{} se logre colocar el valor predeterminado del numero 
print(salida.format(numero))
