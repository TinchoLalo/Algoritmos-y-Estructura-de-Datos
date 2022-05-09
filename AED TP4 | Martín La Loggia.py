#Practico 4 - Modularizacion

''' 
1. Crear una funcion que tome un argumento numerico y devuelva ese numero elevado al cuadrado. Luego de haber creado la funcion, pedirle al usuario 5 numeros, de a uno, e ir mostrando cada numero elevado al cuadrado (utilizando dicha funcion)
'''
i = 0

def cuadrados(numero):
    return numero**2

'''destructuracion 
def cuadrados2(numero): return numero**2
'''


while(i<5):
    numero = int(input("1) Ingrese un numero: "))
    print(cuadrados(numero))
    i+=1
    
    
''' 
2. Crear una funcion llamada es positivo que tome un numero como argumento y devuelva verdadero o falso, como valores logicos, si el numero es positivo o no.
'''
num2 = int(input("2) Ingrese un numero: "))
def es_positivo(numero):
    if numero > 0:
        return True
    else:
        return False
print(es_positivo(num2))


''' 
3. Crear una funcion llamada iguales, que tome dos palabras como parametros, y determine si son iguales o no. Devolviendo verdadero (true) si lo son, o falso (false) en caso contrario.
'''

def iguales(palabra1, palabra2):
    if palabra1 == palabra2:
        return True
    else:
        return False
print('3) ',iguales("hola", "hola"))

'''
4. Crear una funcion llamada signo, que tome un numero y devuelva 1 si este es positivo y
-1 si este es negativo.
'''
num4 = int(input("4) Ingrese un numero: "))
def signo(numero):
    if numero > 0:
        return 1
    else:
        return -1
print(signo(num4))


'''
5. Crear una funcion llamada escalon, que tome un numero y devuelva 1 si este es positivo y 0 si este es negativo.
'''
num5 = int(input("5) Ingrese un numero: "))
def escalon(numero):
    if numero > 0:
        return 1
    else:
        return 0
print(escalon(num5))


'''
6. Crear una funcion llamada delta de dirac que tome dos numeros enteros y devuelva 1 si ambos numeros son iguales, y 0 sino.
'''

def delta_diract(numero1, numero2):
    if numero1 == numero2:
        return 1
    else:
        return 0
print('6) ',delta_diract(2, 2))


''' 
7. Crear una funcion llamada raiz uno, que tome tres parametros: a, b, c. Y calcule solo la primera raiz de la funcion cuadratica. ¿La funcion deberia devolver un valor numerico
entero o con decimales?
'''

def raiz_uno(a,b,c):
    return (-b + (b**2 - 4*a*c)**(1/2))/(2*a)
print('7) ',raiz_uno(1,2,3))



'''
8. Crear una funcion que tome tres numeros como parametros n, a, b, y devuelva verdadero o falso, segun n pertenece o no al intervalo cerrado [a, b]
'''

def intevalo(n,a,b):
    if n >= a and n <= b:
        return True
    else:
        return False
print('8) ',intevalo(3,1,5))



'''
9. Crear una funcion que tome una palabra y devuelva la cantidad de vocales que tiene.Por ejemplo, si se le da el siguiente argumento a la funcion: ’hola’ la funcion deberia devolver
2.
'''

cont = 0
palabra9 = str(input("9) Ingrese una palabra: "))
vocal = ['a', 'e', 'i', 'o', 'u']
def vocales(palabra,cont):
    for i,value in enumerate(palabra):
        if palabra[i] in vocal:
            cont += 1
    return cont
print('9) ',vocales(palabra9,cont))



'''   
10. Crear una funcion que convierta una temperatura en Fahrenheit, en su temperatura equivalente, en grados Celsius. Recordar que la relacion entre ambas cantidades es: Tc = ( 59)(Tf - 32)
Pedirle luego, al usuario temperaturas en Fahrenheit, unas 10 e ir mostrandole su conversion a grados centigrados.
'''

e = 0

def celicius(temperatura):
    return (5*(temperatura-32))/9

while(e<10):
    temperatura = int(input("10) Ingrese una temperatura en Fahrenheit: "))
    print("10) ",celicius(temperatura))
    e += 1
    
    
    
''' 
11. Crear una funcion que tome dos palabras como parametros, y devuelva el texto resultante de concatenar ambas palabras.
'''

def concatenar(palabra1, palabra2):
    return palabra1 + palabra2
print('11) ',concatenar("hola", "mundo"))


''' 
12. Crear ahora una segunda funcion, que tome un tercer argumento extra, y haga lo mismo que la funcion del punto anterior, pero esta vez, utilizando el tercer argumento para saber si debe agregar o no un espacio entre medio de las dos palabras a concatenar. ¿Que tipo
de dato utilizaria para ese tercer argumento?
'''


p1= input("12) Ingrese una palabra: ")
p2 = input("12) Ingrese otra palabra: ")
space= input("12) Ingresar un espacio? (si) o (no): ").lower()
def concatenar3(p1,p2,space):
    if space == 'si':
        return p1 + " " + p2
    else:
        return p1 + p2
print('12) ',concatenar3(p1,p2, space))


''' 
13. Crear una funcion que tome como argumentos una frase y una letra, y determine cuantas veces esta esa letra en dicha frase
'''
    
def letra_frase(frase,letra,count):
    for i,value in enumerate(frase):
        if letra == frase[i]:
            count += 1
    return count
print('13) ',letra_frase("hola mundo", "o", 0))


''' 
14. Crear una funcion llamada capitalizar que tome una palabra como argumento y devuelva una palabra con la primer letra en mayusculas, y resto de las letras en minusculas, de la palabra original.
'''

def mayusculas(palabra):
    palabra[0] = palabra[0].upper()
print('14) ',mayusculas("hola"))

''' 
15. Crear una funcion que tome una lista de valores numericos como argumento, de dos elementos nada mas, y devuelva la lista ordenada. En el caso de Python, ¿Necesito utilizar una segunda lista, auxiliar para modificarla, o pudo devolver la lista original, el argumento
que recibio, modificado y ordenado?
'''

n1 = int(input("15) Ingrese un numero: "))
n2 = int(input("15) Ingrese otro numero: "))
lista = [n1,n2]

def ordenar(lista):
    return sorted(lista)
print('15) ',ordenar(lista))


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