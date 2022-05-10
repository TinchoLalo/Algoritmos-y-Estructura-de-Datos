'''
1) Crear un procedimiento llamado cuadrado que tome un numero como parametro e imprima en pantalla dicho numero al cuadrado
'''

def cuadrado(numero):
    resultado = numero**2
    print('1) ',resultado)
    #print('1) ',resultado, locals())
cuadrado(5) 


'''
2) Crear una variable llamada n, que sera global, en el codigo del ejercicio anterior y asignarle un valor inventado. Realizar las siguientes acciones:
'''

def cuadrado():
    print(n**2, locals())
cuadrado() 


'''
3) ¿Que imprimira en pantalla el siguiente codigo? ¿Cual es el alcance de la variable frase?

frase = "Hola"
def f():
    frase = "Es un lindo dia"
    print(frase)
    
    
    Imprimirá en pantalla: "Es un lindo dia", ya que la variable frase que definimos fuera de la función f(), queda sustituida por la variable frase que definimos dentro de la función f().
'''


'''
4) ¿Que imprimiria en pantalla el siguiente codigo? Determine el alcance de cada variable.




'''
# 6)
file = open ("numeros.txt",'w')
text =["1","2","3","4","5","6","7","8","9","10"]
for i in range(0,10) :
    file.write( textlil+ os. lineseo)
file.close()



# 7)
archivo = open('archivo.txt','r')
lineas = archivo.readlines()
total = 0
for i in lineas:
    print(i)
    total += 1
print('Total de lineas: ',total)
archivo.close()

''' 
Salida:

Hola 
mundo 
esto
es
un
archivo
de 
texto

Total de lineas:  8

'''




# 9)
import os
file = open("numeros.txt", "r").readlines()
promedio=0
suma=0

for i in file:
    n = int(i)
    suma = suma +n
promedio = suma/len(file)

print(f'Suma: {suma}\nPromedio: {promedio}')
file.close()

# salida: Suma: 55   Promedio: 5.5


# 10)
import random
nombre = str(input("Introduce el nombre del archivo: "))
file = open(nombre+".txt",'w')

for i in range(0,250):
    num = str(random.randint(0,100))
    file.write(num+", ")
    
file.close()



# 11) 
import os,random
nombre = str(input("Introduce el nombre del archivo: "))
a = int(input("Introduce un número: "))
b = int(input("Introduce otro número: "))

    
file = open(nombre+".txt",'w')

for i in range(0,250):
    if a >b:
        num = str(random.randint(b,a))
    else:
        num = str(random.randint(a,b))
        
    file.write(num+", ")
    
file.close()




# 12)
longitud = int(input("Introduce la longitud del rectangulo: "))
estilo = str(input("Introduce el estilo del rectangulo: "))

# vertical
for i in range(0,longitud):
    if (i == 0 or i == longitud-1):
        print(estilo*4)
    else:
        print(estilo+" "*2+estilo)
''' salida:
####
#  #
#  #
#  #
####
'''

# horizontal
for i in range(0,4):
    if (i == 0 or i == 3):
        print(estilo*longitud)
    else:
        print(estilo+" "*(longitud-2)+estilo)
''' salida:
##########
#        #
#        #
##########
'''



# 14) 
numero = int(input("Introduce un número en base 10: ")) # entrada 33
base = int(input("Introduce la base: ")) # entrada 8

def binario(numero,base):
    bit = ''
    while numero !=0:
        bit = str(numero % base) + bit
        numero = numero // base
    return str(numero) + bit
if (numero > 0):
    print(binario(numero,base)) # salida: 041
    
    
# 15)

numero = str(input("Introduce un número en base 2: ")) # entrada  0101011
def decimal(numero): return int(numero,2)
print(decimal(numero)) # salida: 43
