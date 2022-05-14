import random

archivo = open('Archivos de Texto/ahorcado.txt','r')
linea = archivo.read().splitlines()
datos = [] # datos del archivo de texto
num = random.randint(0,9) # numero al azar
letra = ""

# añadimos las palabras a una lista
for i in linea:
	datos.append(i.strip('\n'))
archivo.close()

# obtenemos la palabra al azar
print(''' BIENVENIDO AL JUEGO DEL AHORCADO
    |===
    |   '
    |   o
    |  -|- 
    |  / \ 
    |
   === 
      ''')
intentos = int(input('¿Cuantos intentos quieres?: '))
palabra = datos[num]
desconocido = palabra[0]+'_'*(len(palabra)-1)
conocido = desconocido
ganar = False
# mostrar la primer letra de la palabra
print(f'La palabra es: {desconocido}')



def ahorcado(letra,desconocido,palabra):
    global conocido
    global ganar
    global intentos
    conocido = conocido
    
    # si la letra ingresada se encuentra en la palabra
    if (letra in palabra):
        print("La letra esta en la palabra:")
        # mostrar la palabra con las letras encontradas
        for i,value in enumerate(palabra):
            if letra== palabra[i]:
                conocido = conocido[:i]+letra+conocido[i+1:]
        print(conocido)
        if conocido == palabra:
            print("Ganaste!!😀")
            ganar = True
    # si la letra ingresada no se encuentra en la palabra perder un intento
    else:
        intentos -= 1
        print(f"La letra no se encuentra en la palabra \nte quedan: {intentos} intentos")
        pista = input("¿Quieres una pista? (si/no) esto te restará un intento: ").lower()
        
        # si perdio un intento y quiere una pista
        if (pista == 'si'):
            intentos -= 1
            print(f"Te quedan: {intentos} intentos")
            # obtener una posición random de la palabra
            p = random.randint(0,len(palabra))
            terminar = False
            while(terminar == False):
                # comprobar que la letra no haya sido descubierta
                if (palabra[p] in conocido):
                    p = random.randint(0,len(palabra))
                else:
                    conocido = conocido[:p]+palabra[p]+conocido[p+1:]
                    print(f"Pista: {conocido}")
                    terminar = True
        # si perdio todos los intentos
        if (intentos == 0):
            print("Perdiste🙁")
            print(f"La palabra era: {palabra}")
            ganar = True


# pedir una letra y llamar a la funcion ahorcado

while ganar == False:
    letra = str(input("Ingrese una letra o la palabra: "))
    # comprobar si gano o perdio
    if letra == palabra:
        print("Ganaste!!😀")
        ganar = True
    else:
        ahorcado(letra,desconocido,palabra)

