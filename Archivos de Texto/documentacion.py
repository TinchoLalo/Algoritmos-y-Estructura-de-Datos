'''==================================================
    ALGORITMOS Y ESTRUCTURAS DE DATOS EN PYTHON
=================================================='''



'''==================================================
                    TIPOS DE DATOS
=================================================='''

cadena = "Hola mundo" # Cadena de caracteres, texto. Se expresa con str
entero = 10 # Número Entero. Se expresa con int
flotante = 10.5 # Número Flotante. Se expresa con float
booleano = True # Valor booleano. Se expresa con bool
lista = [1,2,3,4,5] # Lista o arreglo. Se expresa con list
tupla = (1,2,3,4,5) # Tupla. Se expresa con tuple
diccionario = {"nombre":"Juan","edad":20} # Diccionario. Se expresa con dict
conjunto = {1,2,3,4,5} # Conjunto, no permite objetos iguales. Se expresa con set


# Ejemplos:
cadena = str("Hola mundo")
entero = int(10)
booleano = bool(True)
lista = list[1,2,3,4,5]



'''==================================================
                OPERADORES ARITMETICOS
=================================================='''

suma = 10 + 5 # Suma
resta = 9 - 4 # Resta
multiplicacion = 10 * 5 # Multiplicación
division = 10 / 5 # División
potencia = 10 ** 2 # Potenciación, exponente
resta_modulo = 10 % 2 # Resto de una división


'''==================================================
                OPERADORES RELACIONALES
=================================================='''

mayor_que = 10 > 5 # Mayor que
menor_que = 10 < 5 # Menor que
igual_que = 10 == 5 # Igual que
diferente = 10 != 5 # Diferente que
mayor_igual = 10 >= 5 # Mayor o igual que
menor_igual = 10 <= 5 # Menor o igual que


'''==================================================
                OPERADORES LOGICOS
=================================================='''

y = b and a # ambos deben ser verdaderos, es decir, ambos deben coincidir o darse
o = b or a # uno debe ser verdadero
no = not a # el valor debe ser falso


'''==================================================
                OPERADORES DE ASIGNACION
=================================================='''

suma += 10 # suma = suma + 10
resta -= 10 # resta = resta - 10
multi *= 10 # multi = multi * 10
divi /= 10 # divi = divi / 10
potencia **= 10 # potencia = potencia ** 10
modulo %= 10 # modulo = modulo % 10


'''==================================================
            SALIDA Y ENTRADA DE DATOS
=================================================='''

print('Hola mundo') # Imprime una cadena de caracteres (salida)
input('Ingrese un número: ') # obtiene datos de entrada (entrada)

# Ejemplos:
nombre = input('Ingrese su nombre: ')
print(f'Hola {nombre}!')

# expecificar los datos de entrada
edad = int(input('Ingrese su edad: '))
print(f'Su edad es {edad}')



'''==================================================
                CONDICIONALES
=================================================='''

if edad > 18: # if es una condición que se cumple si la condición es verdadera (si)
    print('Eres mayor de edad')
elif edad == 18: # elif es para el caso de que se cumpla la condición anterior (entonces si)
    print('Eres igual de edad')
else : # else es para el caso de que no se cumpla ninguna condición (sino)
    print('Eres menor de edad')
    
# Ejemplo con operadores lógicos:

if edad > 18 and edad < 30: # and es para que se cumpla la condición si ambas son verdaderas
    print('Eres mayor de edad y menor de 30 años')
elif edad > 30 or edad < 18: # or es para que se cumpla la condición si alguna es verdadera
    print('Eres mayor de 30 años o menor de 18 años')
elif not edad > 20: # not es para que se cumpla la condición si es falsa
    print('No eres mayor de 20 años')


'''==================================================
                CONDICIONALES ANIDADOS
=================================================='''

if edad > 0 : # si la edad es un número positivo
    if edad > 18:
        print('Eres mayor de edad')
    else :
        print('Eres menor de edad')
else : # si la edad es un número negativo
    print('Edad inválida')
    
    
'''==================================================
                OPERADOR CONDICIONAL TERNARIO
=================================================='''
p1 = "Hola"
p2 = "Mundo"
espacio = "si"
print(p1 + " " + p2 if espacio == 'si' else p1 + p2) 
# salida: Hola Mundo




'''==================================================
                CICLOS O BUCLES
=================================================='''

# bucle while
# while es un ciclo que se cumple mientras la condición sea verdadera
time = 10
while time >= 0: 
    print(time) #mensaje a mostrar en terminal
    time -= 1 # contador


while tarea != 'salir': 
    tarea = input('Ingrese una tarea: ')
    print(f'Tarea: {tarea}')



# bucle for 
# for es un ciclo que se repite de forma determinada,es decir le pasamos la cantidad de repeticiones
for i in range(0,10): 
    print(i)            


frase = "Hola mundo"
for i,value in enumerate(frase): 
    print(frase[i])




'''==================================================
                    FUNCIONES
=================================================='''

def suma(a,b): # definimos una función
    return a + b # retornamos el resultado de la suma
suma(10,5) # llamamos a la función



# destructuración 
def resta(a,b): return a - b 
print(resta(10,5))

# lambda 
def multi(a,b): lambda a,b: a * b


# ejemplo
def escalon(numero):
    if numero > 0:
        return 1
    else:
        return 0
print(escalon(5))


def max3(a, b,c):
    if a >= b and a >=c:
        return a
    elif a <= b and c <= b:
        return b
    else:
        return c
print(max3(3,5,2))



'''==================================================
                    CONVENCIONES
=================================================='''
''' Se utiliza para llevar un orden en tu código, para que sea más fácil de comprender.
Son formas de definir variables, funciones, clases, etc. '''

mi_nombre = "SNAKE" # SNAKE CASE 
miNombre = "CAMEL" # CAMEL CASE
MiNombre = "PASCAL" # PASCAL CASE




'''==================================================
                    IMPORTACIONES
=================================================='''


import math # importa la librería math
import math as m # importa la librería math y la renombra
import math as m, random as r # importa la librería math y la renombra
import paquete.modulo  # importa un módulo que está dentro de un paquete

from paquete.modulo1 import * # importa todos los módulos que están dentro de un paquete





'''==================================================
            Métodos de las listas (arrays)
=================================================='''


lista = [1,2,3,4,5] # definimos una lista

lista.append(6) # agregamos un elemento a la lista
# lista = [1,2,3,4,5,6]

lista.clear() # limpiamos la lista 
# salida: []

l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2) # agregamos la lista l2 a la lista l1
# l1 = [1,2,3,4,5,6]

lista.count(2) # cuenta la cantidad de veces que se repite un elemento en la lista
# salida: 1

lista.index(3) # devuelve el índice (posición) de un elemento en la lista
# salida: 2

lista.insert(2, "hola") # inserta un elemento en una posición específica de la lista
# salida: [1, 2, 'hola', 3, 4, 5]

lista.pop() # elimina el último elemento de la lista
# salida: 5

lista.remove(4) # elimina el primer elemento que coincida con el valor especificado
# salida: [1, 2, 3, 5]

lista.reverse() # invierte el orden de los elementos de la lista
# salida: [5, 4, 3, 2, 1]

deslist = lista.reverse()
deslist.sort() # ordena la lista
# salida: [1, 2, 3, 4, 5]
lista.sort(reverse=True) # ordena la lista de forma descendente





'''==================================================
                    CLASES
=================================================='''


class Persona:
    def __init__(self, nombre, edad): # inicializamos los atributos
        self.nombre = nombre # asignamos el valor del parámetro a un atributo
        self.edad = edad
        
    def saludar(self): # definimos un método
        print(f'Hola, me llamo {self.nombre} y tengo {self.edad} años')



martin = Persona('Martin', 19) # creamos un objeto
print(martin.nombre) # accedemos a un atributo
martin.saludar() # accedemos a un método
martin.nombre = 'Juan' # cambiamos el valor de un atributo