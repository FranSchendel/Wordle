# Importamos el modulo random, que, en este caso, nos permite pedir un numero random
import random

# Abrimos el archivo "Lista.txt" en forma de lectura ("r"), para poder tomar los datos
f = open("Lista.txt", "r")

# Creo un array para guardar las palabras y guardo los datos de "f" con la funcion ".readlines()"
palabras = []
palabras = f.readlines()

# Elegimos una palabra aleatoria de la lista y la guardamos en la variable "palabra_definitiva"
respuesta = random.choice(palabras)
palabra_usuario = ""
print("palabra definitiva: {respuesta}")
while palabra_usuario != respuesta:
    palabra_usuario = input("ingrese una palabra: ")
    if palabra_usuario != respuesta:
        guiones = ""
        for i in range (len(palabra_usuario)):
            if palabra_usuario[i] in respuesta:
                #Poner un "=" bajo cada letra que estñe en la posición correcta
                if palabra_usuario[i] == respuesta[i]:
                    guiones += "="
                #Poner un "-" bajo cada letra que esté dentro de la palabra
                else:
                    guiones += "-"
            #No poner nada bajo cada letra incorrecta
            else:
                guiones += " "
        print(palabra_usuario)
        print(guiones)