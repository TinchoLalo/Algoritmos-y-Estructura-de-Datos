import random

archivo = open('Archivos de Texto/ahorcado.txt','r')
linea = archivo.read().splitlines()
datos = [] # datos del archivo de texto
num = random.randint(0,9) # numero al azar
intentos = 10
ganar = False
letra = ""

# añadimos las palabras a una lista
for i in linea:
	datos.append(i.strip('\n'))
archivo.close()

# obtenemos la palabra al azar
print(datos)
palabra = datos[num]
desconocido = palabra[0]+'_'*(len(palabra)-1)

# mostrar la primer letra de la palabra
print(f'La palabra es: {desconocido}')


def ahorcado(letra,intentos,desconocido,palabra):
    global conocido
    conocido = conocido
    # si la letra ingresada se encuentra en la palabra
    if (letra in palabra):
        print("La letra esta en la palabra")
        # mostrar la palabra con las letras encontradas
        for i,value in enumerate(palabra):
            if letra== palabra[i]:
                conocido = conocido[:i]+letra+conocido[i+1:]
        print(conocido)
    # si la letra ingresada no se encuentra en la palabra perder un intento
    else:
        intentos -= 1
        print(f"La letra no se encuentra en la palabra \n te quedan: {intentos}")


while intentos > 1:
    letra = str(input("Ingrese una letra o la palabra: "))
    # comprobar si gano o perdio
    if intentos == 0:
        print("Perdiste🙁")
    elif letra == palabra:
        print("Ganaste!!😀")
        intentos = 0
        ganar = True
    else:
        ahorcado(letra,intentos,desconocido,palabra)



    