
# 1. Crear un programa que escriba ”Hola mundo” en la pantalla.
print('Hola mundo')


''' 2. Guardar un numero entero en una variable, llamada n por ejemplo, y mostrarlo en pantalla.'''
n = 10
print(n)


''' 3. Ingrese un nombre y salude a ese nombre, con un mensaje de bienvenida.'''
name = input('3) Ingrese su nombre: ')
print('3) Hola ',name)


''' 4. Implemente un programa que lea por teclado dos numeros enteros e imprima en pantalla
los valores leidos en orden inverso. Por ejemplo, si se ingresan los numeros 4 y 8, debe
mostrar el mensaje: Se ingresaron los valores 8 y 4.'''
n4a = int(input('4) Ingrese un número entero: '))
n4b = int(input('4) Ingrese otro número entero: '))
print(f'4) Se ingresaron los valores {n4b} y {n4a}')


''' 5. Que pida un numero y muestre por pantalla la frase “Has introducido (numero ingresado)
gracias”'''
n5 = int(input('5) Ingrese un número entero: '))
print(f'5) Has introducido {n5} gracias!')


''' 6. Pedir dos valores numericos. Calcular y mostrar la suma, resta, multiplicacion y division
de ambos.'''
n6a=float(input('6) Ingrese un número: '))
n6b=float(input('6) Ingrese un número: '))

suma = n6a + n6b
resta = n6a - n6b
multiplicacion = n6a * n6b
division = n6a / n6b

print(f"Suma: {suma}\nResta: {resta}\nMultiplicación: {multiplicacion}\nDivision: {division}" )


''' 7. Mostrar en pantalla los resultados de calcular las siguientes expresiones:
a) 5a + 10b
b) b^2
c) 2n-1 / 2n+1
d) 1√n
e) 2x - y
f) x-y / x+y
'''

x=float(input('7) Ingrese un número: '))
y=float(input('7) Ingrese otro número: '))
n = float(input('7) Ingrese otro número: '))
an = float(input('7) Ingrese otro número: '))
bn = float(input('7) Ingrese otro número: '))

ejA =  5*a + 10*bn
def a():
    return 5*an + 10*bn
def b():
    return bn**2
def c():
    return 2*n-1/2*n+1
def d():
    return 1*(n**0.5)
def e():
    return 2*x -y
def f():
    return x-y/x+y

print(f' a) {a()}\n b) {b()}\n c) {c()}\n d) {d()}\n e) {e()}\n f) {f()}\n')


''' 8. Implemente un programa que lea dos numeros reales e imprima el resultado de la division
de los mismos con una precision de dos decimales. Por ejemplo, si se ingresan los valores
4,5 y 7,2,debe imprimir: El resultado de dividir 4,5 por 7,2 es 0,62 '''

n8a = 4.5
n8b = 7.2
res8= n8a/n8b
print('8) ',round(res8,2)) 


''' 9. Leer dos numeros y determinar si son iguales, en caso afirmativo mostrar el mensaje “Iguales”'''

n9a = float(input('9) Ingrese un número: '))
n9b = float(input('9) Ingrese otro número: '))

if(n9a==n9b):
    print('9) Son Iguales')
    


''' 10. Leer dos numeros y determinar cual de ellos es el mayor, mostrando por pantalla “El
valor mayor es:” y el correspondiente numero.'''

n10a= int(input("10) ingrese un número: "))
n10b= int(input("10) ingrese un número: "))
def max():
    if n10a > n10a:
        return n10a
    else:
        return n10b
print('10) El mayor es ',max())


''' 11. Realice un programa que informe el valor total en pesos de una transaccion en dolares.
Para ello, el programa debe leer el monto total en dolares de la transaccion, el valor del
dolar al dia de la fecha y el porcentaje (en pesos) de la comision que cobra el banco por
la transaccion. Por ejemplo, si la transaccion se realiza por 10 dolares, el dolar tiene un
valor 20,54 pesos y el banco cobra un 4 % de comision, entonces el programa debera informar: La transaccion sera de 213,61 pesos argentinos (resultado de multiplicar 10*20,54
y adicionarle el 4 %)'''

dolares =float(input('11) Ingrese los dólares a cambiar: '))
valor = 20.54
comision = 4

def transaccion():
    resultado = (dolares * valor)+(dolares * valor * comision/100)
    return round(resultado,2)
print(f'11) La transacción será de {transaccion()} pesos argentinos')


''' 12. Realizar un programa que permita al usuario ingresar una palabra y muestre en pantalla
cuantos caracteres en total tiene la misma.'''
palabra = str(input('12) Ingrese una palabra: '))
long = len(palabra)
print('12) Longitud: ',long)


''' 13. Realizar un programa que lea 2 numeros enteros desde teclado e informe en pantalla cual
de los dos numeros es el mayor. Si son iguales debe informar en pantalla lo siguiente: “Los
numeros leidos son iguales”'''
n13a = int(input('13) Ingrese un número entero: '))
n13b = int(input('13) Ingrese otro número entero: '))
if (n13a > n13b):
    print('13) El mayor es ',n13a)
elif (n13b == n13a):
    print('13) Los números leídos son iguales')
else :
    print('13) El mayor es ',n13b)
    
    
''' 14. Realizar un programa que lea un numero real e imprima su valor absoluto. El valor
absoluto de un numero x, se escribe |x| y se define como: |x| = x cuando x ≥ 0 |x| = -x
cuando x < 0'''
n14 = float(input('14) Ingrese un número real: '))
def absoluto():
    if n14 >= 0:
        return n14
    else:
        return -n14
print(f'14) El valor absoluto de |{n14}|  es: {absoluto()} ')


''' 15. Realizar un programa que permita ingresar dos palabras, y determine si tienen la misma
longitud o no. Mostrar un mensaje en pantalla en cada caso. Misma longitud, una menor,
o una mayor.'''
palabra1 = str(input('15) Ingrese una palabra: '))
palabra2 = str(input('15) Ingrese otra palabra: '))
def longPalabra():
    if (len(palabra1) == len(palabra2)):
        return '15) Las palabras tienen la misma longitud'
    elif (len(palabra1) < len(palabra2)):
        return f'15) Las palabra {palabra1} tiene una longitud menor'
    else:
        return f'15) Las palabra {palabra1} tiene una longitud mayor'
print(longPalabra())


''' 16. Realizar un programa que permita al usuario ingresar un numero y determine si es positivo o negativo'''
n16 = int(input('16) Ingrese un número: '))
if (n16 >= 0):
    print('16) El número es positivo')
elif (n16 == 0):
    print('16) El número es igual a cero')
else:
     print('16) El número es negativo')
     
     
''' 17. Realizar un programa que permita al usuario ingresar dos numeros enteros, y ordenarlos de menor a mayor. Mostrarlos luego en pantalla.'''
n17a =int(input('17) Ingrese un número: '))
n17b = int(input('17) Ingrese otro número: '))
def ordenar():
    if (n17a > n17b):
        return n17b,n17a
    else:
        return n17a,n17b
print(ordenar())


''' 18. Realizar un programa que permita al usuario ingresar 3 numeros, ordenarlos y mostrarlos
luego en pantalla de menor a mayor.'''

n1 =int(input('18) Ingrese un número: '))
n2 = int(input('18) Ingrese otro número: '))
n3 = int(input('18) Ingrese otro número: '))

def ordenar3():
    if (n1 >= n2 and n1 >= n3): 
        if (n2 >= n3):
            return n3,n2,n1
        else:
            return n2,n3,n1
    elif (n2 >= n1 and n2 >= n3):
        if (n1 >= n3):
            return n3,n1,n2
        else:
            return n1,n3,n2
    else:
        if (n1 >= n2):
            return n2,n1,n3
        else:
            return n1,n2,n3
       
print(ordenar3())

''' 
otro manera de hacerlo es añadir los números a una lista y luego ordenarlos con sorted()

lista = [n1,n2,n3]
print(sorted(lista))

'''

