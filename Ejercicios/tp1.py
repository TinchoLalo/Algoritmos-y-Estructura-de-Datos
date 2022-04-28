# 1

nombre = input('1) Ingrese su nombre: ')
edad = input('Ingrese su edad: ')
print(f'Hola {nombre}, tu edad es {edad}')
print('hola '+nombre)

# 2
n = 3
print(n)

#3 
a = 2.5
b = 3.5
print('3) Division: ',a/b)

#4
c = float(input('4) Ingrese un número: '))
print(f'Has introducido el número {c} gracias')


#5
n1 = float(input('5) Ingrese un número: '))
n2 = float(input('Ingrese otro número: '))

def suma():
    return n1+n2

def resta():
    return n1-n2

def multiplicacion():
    return n1*n2

def division():
    return n1/n2

print(f'Suma: {suma()}, Resta: {resta()}, Multiplicación: {multiplicacion()}, Division: {division()}')

#6

e = int(input('Ingrese un número: '))
elevado = e**2
print(elevado)

