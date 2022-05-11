# imprimir hola mundo en python en terminal
print('Hola Python')


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
12. Realizar un programita que le pida ingresar una frase al usuario y coloque cada letra como elemento de una lista.
'''
frase11 = str(input("11) Ingrese una frase: "))
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
una piramide y el algoritmo deberia imprimir en pantalla una piriamide de numerales. Por
ejemplo, si se ingresa 7, se deberia ver en pantalla:
'''

pisos = int(input('Ingresa en número la altura de la piramide: '))
pisos = round(pisos/2)

for i in range(0,pisos):
    line= i+1
    space = pisos-i
    # imprimir los pisos
    print(' '*space+'#'*line+'#'*line)
    
    

''' 
16. Realizar una funcion que tome dos numeros: a, b y devuelva la cantidad de numeros pares que hay en el intervalo cerrado [a, b]. Controlar que a <= b.
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



''' 
12. Crear ahora una segunda funcion, que tome un tercer argumento extra, y haga lo mismo que la funcion del punto anterior, pero esta vez, utilizando el tercer argumento para saber si debe agregar o no un espacio entre medio de las dos palabras a concatenar. ¿Que tipo
de dato utilizaria para ese tercer argumento?
'''


p1= input("12) Ingrese una palabra: ")
p2 = input("12) Ingrese otra palabra: ")
space= input("12) Ingresar un espacio? (si) o (no): ").lower()
def concatenar3(p1,p2,space):
    return p1 + " " + p2 if space == 'si' else p1 + p2 # ternario
    '''
    if space == 'si':
        return p1 + " " + p2
    else:
        return p1 + p2
    '''
print('12) ',concatenar3(p1,p2, space))