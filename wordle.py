# Importamos el modulo random que, en este caso, nos permite pedir un numero random
import random
# Importamos el modulo que permite hacer un contador
import time

# Abrimos el archivo "Lista.txt" en forma de lectura ("r"), para poder tomar los datos
f = open("Lista.txt", "r")

# Creo un array para guardar las palabras y guardo los datos de "f" con la funcion ".readlines()"
palabras = []
palabras = f.readlines()
f.close()

for i in range (len(palabras)):
    palabras[i] = palabras[i].replace("\n", "")
    palabras[i] = palabras[i].lower()

# Cantidad de jugadores
cant_jugadores = input("Ingresar cantidad de jugadores: ")
cant_jugadores = int(cant_jugadores)
jugadores = []
for i in range(cant_jugadores):
    jugador = input("Nombre del jugador" + str(i + 1) + ": ")
    jugadores.append(jugador)


# Selección de dificultad
dificultad = input("Eliga una dificultad:\n 1: Facil (Sin tiempo límite)\n 2: Medio(120 segundos)\n 3: Dificil(60 segundos)\n")
dificultad = int(dificultad)
tiempo_limite = 0.0
if dificultad == 1:
    pass
elif dificultad == 2:
    tiempo_limite = 120.0
elif dificultad == 3:
    tiempo_limite = 60.0

# Hacemos un bucle que se repita mientras la respuesta del usuario sea diferente de la correcta
estadisticas = []
for i in range(cant_jugadores):
    # Elegimos una palabra aleatoria de la lista y la guardamos en la variable "palabra_definitiva"
    respuesta = random.choice(palabras)
    respuesta_usuario = ""
    intentos = 0
    # Tiempo en segundos desde el inicio del programa hasta que se cargaron los datos
    start = time.perf_counter()
    while respuesta_usuario != respuesta:
        intentos += 1
        respuesta_usuario = input(jugadores[i] + ", ingrese una palabra: ")
        respuesta_usuario = respuesta_usuario.lower()
        if respuesta_usuario != respuesta:
            guiones = ""
            for l in range (len(respuesta_usuario)):
                if respuesta_usuario[l] in respuesta:
                    #Poner un "=" bajo cada letra que estñe en la posición correcta
                    if respuesta_usuario[l] == respuesta[l]:
                        guiones += "="
                    #Poner un "-" bajo cada letra que esté dentro de la palabra
                    else:
                        guiones += "-"
                #No poner nada bajo cada letra incorrecta
                else:
                    guiones += " "
            print(respuesta_usuario)
            print(guiones)
        end = time.perf_counter()
        tiempo = end - start
        print("Llevas ", tiempo, " segundos")
        # Agregamos un if para verificar que no se haya pasado del tiempo limite
        if dificultad != 1 and tiempo >= tiempo_limite:
            print("Llegaste al límite de tiempo, la palabra era:", respuesta)
            respuesta_usuario = respuesta
    # Tiempo en segundos desde el inicio del programa hasta el final de su ejecución
    end = time.perf_counter()
    tiempo_final = end - start
    estadisticas.append([jugadores[i], "tiempo: " + str(tiempo_final), "intentos: " + str(intentos)])

print(estadisticas)
