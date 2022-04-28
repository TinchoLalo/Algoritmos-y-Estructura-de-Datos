''' 1) Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos'''

from ast import Num


a= float(input("ingrese un número: "))
b= float(input("ingrese un número: "))
c= float(input("ingrese un número: "))
def max(a, b):
    if a > b:
        return a
    else:
        return b
print(max(a,b))

''' 2) Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.'''

def max3(a, b,c):
    if a >= b and a >=c:
        return a
    elif a <= b and c <= b:
        return b
    else:
        return c
print(max3(a,b,c))


''' 3) Definir una función que calcule la longitud de una lista o una cadena dada. '''

lista = input("Ingrese una lista: ")

#longitud de la lista con len
def longitud(lista):
    return len(lista)
print('Len: ',longitud(lista))

#longitud de la lista manualmente
def longmanual(lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont
print('Manualmente: ',longmanual(lista))


''' 4) Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.'''

ct = str(input("Ingrese un carácter: "))
ct = ct.lower() # convertir caracter a minusculas
def Vocal(ct):
    if ct == 'a' or ct == 'e' or ct == 'i' or ct =='o' or ct == 'u':
        return True
    else:
        return False
print(Vocal(ct))


''' 5) Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. '''
liste = [1,2,3,4]
def sum(liste):
    suma = 0
    for i in liste:
        suma += i
    return suma
print(sum(liste))

def multi(liste):
    mult = 1
    for i in liste:
        mult *=i
    return mult
print(multi(liste))


''' 6) Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"'''

frase = "estoy probando"
def inversa(frase):
    return frase[::-1]
print(inversa(frase))


def inversa2(frase):
    inv = ''
    cont = len(frase)
    indice = -1
    
    while cont >= 1:
        inv += frase[indice]
        indice = indice +(-1)
        cont -= 1
    return inv
print(inversa2(frase))


''' 7) Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.'''

palabra = str(input("Ingrese una palabra: "))

def es_palindromo(palabra):
    pali = palabra[::-1]
    if pali == palabra:
        return "Es palindromo"
    else:
        return "NO es palindromo"
print(es_palindromo(palabra))


''' 8) Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.'''
ls1 = input("Ingrese una lista: ")
ls2 = input("Ingrese una lista: ")
def superposicion(ls1,ls2):
    for i in ls1:
        for x in ls2:
            if i == x:
                return True
    return False
print(superposicion(ls1,ls2))


''' 9)  Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".'''

c1 = str(input("Ingrese una caracter: "))
n1 = int(input("Ingrese un número: "))

def generar_n_caracteres(c1,n1):
    return n1*c1
print(generar_n_caracteres(c1,n1))

''' 10)  Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla.'''

histo= [3,1,7]
def procedimiento(histo,c1):
    for i in histo:
       print(i *c1) 
procedimiento(histo,c1)
