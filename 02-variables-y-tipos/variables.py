"""
una variable es un contenedor
de infromacios que dentro guardara un 
dato,se pueden crear muchas variables
y que cada una tenga datos  distintos

"""
# creacion de variables y asignacion de valor

text = "ubaldo cervantes aprende python"
text2 = "ubaldo sigue aprendiendo"
numero = 10
decimal = 28.33



#mostrar variables por consola

print(text)
print(text2) 
print(numero)  
print(decimal) 

print("--------------------------------")

# cambiar valor de las variables
numero = 35
decimal = 54.72

print(numero)  
print(decimal) 


#concatenacion de variables

nombre = "ubaldo"
apellidos = "cervantes"
web =  "ubaldo web"

print(nombre + " " + apellidos + " " + web)
print(f"{nombre} {apellidos} - {web}")
print ("hola my nombre es {} {} y my web es: {}".format(nombre, apellidos, web))

