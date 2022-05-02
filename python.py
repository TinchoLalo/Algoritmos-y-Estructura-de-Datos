
# Imprimir "hola mundo" en consola
print('Hola Mundo')

'''
7. Permitir ingresar al usuario un numero de un digito. Controlando se haya ingresado dicho
numero de no mas de 1 digito de longitud, pasarlo a letras y mostrarlo en pantalla.
(Ejemplo: Si ingresa 3, se veria como resultado ”tres”).
'''
digito = int(input("7) Ingrese un numero de un digito: "))
numLetras = ['cero','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve']

if (digito <= 9 and digito >= 0):
    print("7) ",numLetras[digito])
else:
    print("El numero ingresado no es valido")
    
    
'''
12. Realizar un programita que le pida ingresar una frase al usuario y coloque cada letra
como elemento de una lista.
'''
frase11 = str(input("12) Ingrese una frase: "))
palabra11 = []

for i,value in enumerate(frase11):
    palabra11.append(frase11[i])
print("12) ",palabra11)






''' 17. Tirar 20 veces un dado de 6 caras. Mostrar el promedio de esas 20 tiradas. '''
import random
i = 0
tirada = 0
dado = []
while(i<= 20):
    tirada = random.randint(1,6)
    dado.append(tirada)
    i += 1
prom17 = sum(dado)/len(dado)
print("17) ",round(prom17,2))

'''
6) Permita al usuario ingresar el nombre de un archivo, genere un nuevo nombre donde los
espacios sean reemplazados por guion bajo y la extension por numerales.

'''

archivo = str(input('6) Ingrese el nombre del archivo: '))
ext = 0
final = 0

for i,value in enumerate(archivo):
    #reemplazo los espacios por guiones bajos
    if (archivo[i] == ' '):
        archivo = archivo.replace(archivo[i], '_')
    #reemplazo la extension por numeros
    elif (archivo[i]== '.'):
        final = i+1
        ext = archivo[i::]
        ext = '#' * (len(ext)-1)
print("6) ",archivo[0:final]+ext)


''' 
29. El problema es el siguiente, el usuario deberia poder ingresar la longitud de la base de
una piramide y el algoritmo deberia imprimir en pantalla una piriamide de numerales. 
'''

pisos = int(input('Ingresa en número la altura de la piramide: '))
estilo = input('Ingresa el estilo de la piramide: ')

piramide = ""

for i in range(pisos):
    line= i
    space = pisos-i
    
    piramide = " "*space + estilo*line +estilo*line 
    # imprimir los pisos
    print(piramide)
    
''' 
for i in range(pisos):
    line= i
    space = pisos-i
    
    piramide = " "*space+estilo*line 
    # imprimir los pisos
    print(piramide)
'''
    



''' 
16. Realizar una funcion que tome dos numeros: a, b y devuelva la cantidad de numeros pares
que hay en el intervalo cerrado [a, b]. Controlar que a <= b.
'''
cont = 0
def pares(a,b):
    if a <= b:
        cont = 0
        for i in range(a,b+1):
            if i % 2 == 0:
                cont += 1
        return cont
print('16) ',pares(1,10))