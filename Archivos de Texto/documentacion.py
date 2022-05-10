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