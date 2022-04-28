#=================================
# ALGORITMOS Y ESTRUCTURA DE DATOS
#=================================


# ¿Que es Python?
'''
Python, es un lenguaje de programación de alto nivel con características integradas de administración de memoria, threads, strings. Es amado por su simplicidad y su estructura de datos integrada, el hecho de que Python sea un lenguaje de programación de código abierto, también resulta ser el motivo de su fama.
Está orientado a objetos y tiene tipiado dinámico.
'''




k = "23" + str(12) 
print("result: ",k)

# Tipos de datos en Python

from asyncore import loop
from unittest import case


cadena = str('Hola Mundo') # Cadena de texto
entero = int(1) # Entero
flotante = float(1.5) # Flotante
booleano = bool(True) # Booleano
lista = list([1,2,3]) # Lista
tupla = tuple((1,2,3)) # Tupla
diccionario = dict(a=1,b=2,c=3) # Diccionario

# funciones
def suma(a,b):
    return a+b
print(suma(5,2))

# arreglos
arreglos = [1,2,3,4,5]
print(arreglos[0])

# condicionales
if(1==1):
    print('1==1')
else:
    print('1!=1')

# condicional multiple 
n1=1
n2=2
n3=3

if(n1<=n2) and (n3>n1):
    print(n1 ,' es el número más pequeño')
elif(n1>n2) and (n1>n3):
    print(n1,' es el número más grande')
else:
    print(n1,' es el número del medio')
    
# bucle mientras (while)
while(n1<=n2):
    print(n1)
    n1=n1+1 
# ⬆︎ importante siempre incrementar el valor de la variable para que el bucle no se quede infinito

# bucle while con break
while(n1<=n2):
    print(n1)
    n1=n1+1
    if(n1==n2):
        break

# bucle para (for)
for i in range(1,6):
    print(i)
    
'''
en otros lenguajes 
for i=0, i<=10, i++:
    print(i)
'''

# bucle ejemplos
for i in diccionario:
    print(i)
# valor de la clave
for i in diccionario:
    print(diccionario[i])

# casos (switch)
def operation(operador, a, b):
    if operador == 'suma':
        return a + b
    elif operador == 'resta':
        return a - b
    elif operador == 'multiplica':
        return a * b
    elif operador == 'divide':
        return a / b
    else:
        return None

'''
    en otros lenguajes
    switch(condicion) {
        case 1:
            // haz a
            break;
        case 2:
            // haz b
            break;
        case 3:
            // haz c
            break;
        default:
            // haz x
    }
'''

# separar cadenas y convertirlas en listas

cade = 'Hola Mundo'
print(cade)
cade = cade.split(' ')
print(cade)

