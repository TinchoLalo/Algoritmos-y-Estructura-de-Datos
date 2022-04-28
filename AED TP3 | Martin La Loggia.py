'''
1. El usuario podra ingresar nombre y apellido. El programa deberia convertir las iniciales
en mayusculas y las demas letras en minusculas.
'''
apellido = str(input("1) Ingrese su apellido: "))
nombre = str(input("Ingrese su nombre: "))

mApellido = apellido[0].upper() + apellido[1:].lower()
mNombre = nombre[0].upper() + nombre[1:].lower()

print("1) Su nombre completo es: ", mNombre, mApellido)


'''
2. Se le permitiria al usuario ingresar una frase. Se mostrarian en pantalla solamente las letras
en posiciones pares de la misma.
'''

frase = str(input("2) Ingrese una frase: "))
lista2 = []
for i, value in enumerate(frase):
    if (i % 2 == 0):
        lista2.append(frase[i])
print("2) ",lista2)



'''
3. Disenar un algoritmo en pseudocodigo que permita ingresar una frase al usuario y una
letra, y determine cuantas veces esta esa letra en dicha frase. Luego que ya tenga el
pseudocodigo, implementarlo en Python.
'''

frase3= str(input("3) Ingrese una frase: "))
letra = str(input("Ingrese una letra: "))
canLetra = 0

for i,value in enumerate(frase3):
    if (frase3[i] == letra):
        canLetra += 1
print("3) La cantidad de veces que aparece la letra en la frase: ",canLetra)


'''
4. Ingresar una frase que contenga simbolos varios, ademas de mayusculas y minusculas mezclados. Determinar la cantidad de espacios, y cada simbolo que hay en la misma.
'''

frase4= str(input("4) Ingrese una frase: "))
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z",' ']
espacios = 0
simbolos = 0

for i,value in enumerate(frase4):
    if (frase4[i] == ' '):
        espacios += 1
    elif (frase4[i] in abc):
        simbolos += 0
    else:
        simbolos += 1
print("4) La cantidad de espacios en la frase: ",espacios)
print("4) La cantidad de simbolos en la frase: ",simbolos)

'''
5) Permita al usuario ingresar una frase. Cambie las letras a por 4 y las letras e por 3.

'''

frase5 = input('5) Ingrese una frase: ')
for i,value in enumerate(frase5):
    if (frase5[i] == 'a'):
        frase5 = frase5.replace(frase5[i], '4')
    elif (frase5[i]== 'e'):
        frase5 = frase5.replace(frase5[i], '3')
print("5) ",frase5)


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
8. Se le pediria al usuario una frase. Se mostrarian en pantalla, una palabra por linea de la
misma. *no usar listas en este ejercicio
'''
frase8 = str(input("8) Ingrese una frase: "))
for i,value in enumerate(frase8):
    print("8) ",frase8[i])
    
''' 
9. Pedir el nombre al usuario, y corroborar si ese nombre existe entre los nombres de usuarios
vialidos guardados en una lista.
'''
nombre9 = str(input("9) Ingrese su nombre: "))
nombre9 = nombre9.lower()
nomValid = ['juan','pedro','maria','jose','luis','ana','sofia','santiago','jorge','martina','carlos','sara','jorge','martin']

if (nombre9 in nomValid):
    print("9) El nombre ingresado es valido")
else:
    print("9) El nombre ingresado no es valido")
    
'''otro método

for i,value in enumerate(nomValid):
    if (nombre9 == nomValid[i]):
        print("9) El nombre ingresado es valido")
        break
'''


'''
10. Implemente el programa que pide la usuario 8 nombres del algoritmo del practico anterior.
En ese ejercicio tenia que intentar disenar un algoritmo que seleccionase los nombres que
empiezan con la letra M de una serie de nombres otorgados por el usuario. Utilice para
resolverlo los tipos de datos y comandos que le parezcan mas apropiados.
'''
i = 0
nombres10 = []
nombres10m = []

while(i<=8):
    nombres10.append(str(input("10) Ingrese un nombre: ")))
    i += 1
for i,value in enumerate(nombres10):
    if (nombres10[i][0] == "M"):
        nombres10m.append(nombres10[i])
print("10) Los nombres que empiezan con la letra M son: ",nombres10m)



'''
11. Realizar un programita que le pida ingresar una frase al usuario y coloque cada palabra
de la misma como elemento de una lista.
'''

frase11 = str(input("11) Ingrese una frase: "))
palabra11 = []

for i,value in enumerate(frase11):
    if (frase11[i] == ' '):
        palabra11.append(frase11[i-1])
        palabra11.append(frase11[i+1])
print("11) ",palabra11)


'''
12. Realizar un programita que le pida ingresar una frase al usuario y coloque cada letra
como elemento de una lista.
'''
frase11 = str(input("11) Ingrese una frase: "))
palabra11 = []

for i,value in enumerate(frase11):
    palabra11.append(frase11[i])
print("11) ",palabra11)


'''
13. El usuario deberia poder ingresar varios nombres completos (ejemplo: ”Luis Perez”). El
programa deberia luego, colocar los nombres en una lista y los apellidos en otra.
'''
nombre13 = str(input("13) Ingrese su nombre completo: "))

nom13 = nombre13.split()
nomList13 = []
app13 = nom13[1::]
nomList13.append(nom13[0])
print("13) ",nomList13,app13)


'''14. Se deberian ingresar 8 notas. Se mostraria el promedio, redondeado a 2 decimales.'''
notas14 = []
while(i<=8):
    notas14.append(float(input("14) Ingrese una nota: ")))
    i += 1
prom14 = sum(notas14)/len(notas14)
print("14) El promedio es: ",round(prom14,2))

''' 
15. Pedir al usuario una frase. Determinar de al menos dos modos diferentes (con y sin listas)
la cantidad de palabras que hay en dicha frase.
'''

frase15 = str(input("15) Ingrese una frase: "))
print("15) La cantidad de palabras es: ",len(frase15.split()))


# otro modo
frase15 = str(input("15) Ingrese una frase: "))
cont15 = 1
for i,value in enumerate(frase15):
    if (frase15[i] == ' '):
        cont15 += 1
print("15) ",cont15)



''' 
16. Dada una lista de numeros, ingresada por el usuario o inventada por usted, cree otra lista
con la cantidad de digitos de cada numero de la misma.
'''

lisNum16 = [1,2,3,4,5]
lista16 = []
i =0

while(i<len(lisNum16)):
    lista16.append(int(input("16) Ingrese un numero: ")))
    i += 1
print("16) ",lista16)


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
18. Tirar ahora, 2500 veces un dado de 6 caras. Mostrar el promedio de esas tiradas. Comparar
con el promedio del ejercicio anterior. ¿Nota una diferencia sustancial habiendo cambiado
la cantidad de tiradas?
'''
i = 0
tirada = 0
dado = []
while(i<= 2500):
    tirada = random.randint(1,6)
    dado.append(tirada)
    i += 1
prom17 = sum(dado)/len(dado)
print("17) ",round(prom17,2))



'''
19. Pedirle al usuario sus 10 marcas favoritas. Mostrar una marca al azar de la lista
'''
i = 0
m = 0
marcas19 = []

while(i<=10):
    marcas19.append(str(input("19) Ingrese una marca: ")))
    m = random.randint(0,len(marcas19)-1)
    i += 1
print("19) ",marcas19[m])


'''
20. Pedirle al usuario la cantidad de notas que desea ingresar. Luego pedir cada nota, y guardarlas.
'''
nota20 = int(input("20) Ingrese la cantidad de notas: "))
notas20 = []
i =0
while(i<nota20):
    notas20.append(float(input("20) Ingrese una nota: ")))
    i += 1
print(notas20)


'''
21. Dado un n ingresado por el usuario, realizar la suma de los n primeros terminos de la
serie a continuaciion. Mostrar el resultado.
'''

n21 = int(input("21) Ingrese un numero: "))
i = 1
while(i <= n12):
    op21 = op21 + (1/i)
    i += 1
print("21) ",op21)



'''
22. Cuenta Regresiva: Se requiere un programa que permita el ingreso de un numero positivo
y muestre en pantalla la cuenta regresiva desde el numero ingresado hasta llegar a 0.
Realizar diferentes versiones del programa, utilizando en cada una, una estructura de
bucle diferente de las que tiene disponibles en Python.

'''

regresiva22 = int(input("22) Ingrese un numero: "))

while(regresiva22 >= 0):
    print(regresiva22)
    regresiva22 -= 1
    

'''
23. Suma de Numeros Positivos y Negativos: Se requiere un programa que permita el ingreso
de 10 numeros y al finalizar muestre en pantalla la cantidad numeros positivos y por otra
parte la cantidad de numeros negativos que fueron ingresados.
'''

i = 1
positivos23 = 0
negativos23 = 0
while(i<=10):
    numero23 = int(input("23) Ingrese un numero: "))
    if(numero23 > 0):
        positivos23 += 1
    else:
        negativos23 += 1
    i += 1
print(f"23) Positiovos: {positivos23}, Negativos: {negativos23}")


''' 24. Permitir ingresar numeros enteros hasta que se ingrese la opcion ”s”de salir. Plantee
primero el diseño en pseudociodigo del algoritmo e implemente luego dos versiones.
a) La primer implementaciion funcionaria en cualquier lenguaje.
b) La segunda implementaciion deberia aprovechar que Python es un lenguaje diniamicamente tipado. '''

numero24 = ''
lista24 = []
while(numero24 != "s"):
    numero24 = input("24) Ingrese un numero: ")
    if(numero24 != "s"):
        lista24.append(int(numero24))
print(lista24)


''' 
25. Disenar e implementar un algoritmo que permita ingresar una serie de numeros, sumar
todos los pares y al terminar la serie mostrar dicha suma. Si se ingreso algun impar,
mostrar un mensaje Se ingresaron impares. Para finalizar el ingreso, indicar la cantidad
de numeros a ingresar al principio del programa, o interrumpir la carga cuando se ingrese
el numero 99.
'''
ingresados25 = int(input("25) Ingrese la cantidad de numeros a ingresar: "))

par = []
impar = 0
i = 0
while(i<ingresados25):
    numer25 = float(input("25) Ingrese la cantidad de numeros: "))
    if (numer25 % 2 == 0):
        par.append(numer25)
    else:
        impar += 1
    i += 1
prom25 = sum(par)/len(par)
print("25) Suma de los número pares: ",round(prom25,2))
print("25) Cantidad de números impares: ",impar)



'''
26. Permitir ingresar 10 numeros al usuario. Determinar y mostrar el menor y el mayor.'''
i = 0
lista26 =[]
while(i<10):
    lista26.append(int(input("26) Ingrese un numero: ")))
    i += 1
listaOrdenada=sorted(lista26)
print("26) El mayor es: ",listaOrdenada[9])
print("26) El menor es: ",listaOrdenada[0])



''' 
27. Numero Invertido: Se requiere mostrar en pantalla un numero invertido de 6 cifras, al
que fuera ingresado por teclado. (Ejemplo: en pantalla se veria: “El numero ingresado es
140975, invertido es: 579041”)
'''
num27 =input("27) Ingrese un numero: ")
print("27) El numero invertido es: ",num27[::-1])


'''
28. Pedirle al usuario dos numeros positivos, a y b. Controlar que a < b. Mostrar en pantalla
los numeros del intervalo cerrado [a, b] La computadora deberia ahora seleccionar al azar
un numero de ese intervalo. Y el usuario debera adivinar cual numero ha sido seleccionado
por la computadora, obteniendo un mensaje de exito en caso de acertar. El usuario solo
tendra 10 vidas (numero de intentos) y en caso de no acertar, debera obtener un mensaje
de pucha.
'''
a28 = int(input("28) Ingrese un número: "))
b28 = int(input("28) Ingrese otro número: "))

if (a28<b28):
    for i in range(a28,b28):
        print(i)

azar = random.randint(a28,b28)

adivinar = int(input("28) Adivine el número: "))

if (adivinar == azar):
    print("28) Felicidades adivinaste el número")
else:
    print("28) Erraste")
    
    
    
''' 
29. El problema es el siguiente, el usuario deberia poder ingresar la longitud de la base de
una piramide y el algoritmo deberia imprimir en pantalla una piriamide de numerales. Por
ejemplo, si se ingresa 7, se deberia ver en pantalla:
'''

pisos = int(input('Ingresa en número la altura de la piramide: '))

for i in range(0,pisos+1):
    par =  i%2==0 
    line= i+1
    space = pisos-i
    # imprimir los pisos
    print(' '*space+'#'*line)
    
    


