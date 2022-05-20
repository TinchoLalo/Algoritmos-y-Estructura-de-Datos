
'''
1. Supongamos tienes una lista con las alturas en cm de todos los miembros de tu familia,
por ejemplo [181.5, 72., 34.7, 171.3, 160.1]. Crear un array y mostrar sus atributos, el tipo
de datos, tanto del array como de sus elementos. Mostrar también el total de familiares
cargados en el array.
'''

lista1 = [181.5, 72., 34.7, 171.3, 160.1]
print(f'Atributos: {lista1}\nTipo de datos: {type(lista1)}\nTotal de familiares: {len(lista1)}')


'''
2. Crear un array de 3 dimensiones, que tenga 3 matrices de 2 filas por 4 columnas. Llenelo
con ceros.
'''

lista2 = [[[0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0]]] 
print('2) ',lista2)

''' 
3. Crear una matriz de (4, 6) con valores al azar que pertenecen al intervalo [0, 1).
'''
import random
matriz3 = [[random.randint(0, 1)for i in range(4)],[random.randint(0, 1)for j in range(6)]]
print('3) ',matriz3)


'''  
4. Crear un vector con un total de 25 elementos equidistantes en el intervalo [1, 6].
'''
 
vertor4 = [i for i in range(1, 6)]
print('4) ',vertor4)


'''
5. Pedirle 6 numeros enteros al usuario y guardarlos en una lista. Crear un array de una dimension en base a dicha lista.
'''
array5 = []
while(w <=6):
    n = int(input('Ingrese un número: '))
    array5.append(n)
    w+=1
print('5) ',array5)

'''
6. Crear un vector con numeros enteros al azar entre 0 y 5. Luego reemplazar los 0 con el
valor -1.
'''

vector6 = [random.randint(0, 5) for i in range(5)]
vector = []
for i in vector6:
    if i == 0:
        vector.append(int(-1))
    else:
        vector.append(int(i))
print('6) ',vector)


''' 
7. Dada una lista de 3 numeros enteros cualesquiera, y un vector con 3 numeros enteros cualesquiera. ¿Que sucede si suma la lista a si misma, lista + lista, y si hace lo mismo
con el vector? Haga la prueba y compare los resultados.
'''

vector7 = [1, 2, 3]
lista7 = list([4, 5, 6])

print('7) Suma del Vector: ',vector7 + vector7)
print('7) Suma de la Lista: ',lista7 + lista7)


'''
8. Crear una matriz de 3 x 3, con valores que van de 1 a 9.
'''
matriz8 = [[i for i in range(1, 10)],[i for i in range(1, 10)],[i for i in range(1, 10)]]
print('8) ',matriz8)


''' 
9. Crear una matriz de 16 x 20 con numeros al azar, de algun tipo que le guste, distinto al tipo de dato por defecto float64.
'''

matriz8 = [[random.randint(0, 1) for i in range(3)],[random.randint(3, 4) for i in range(3)]]
print('8) ',matriz8)


''' 
10. Crear un array de 5 filas y 6 columnas, llenarlo con valores numericos enteros, al azar entre 1 y 6. Luego, reemplazar todos los valores en la fila 5, por el valor 0.
'''

array10 = [[random.randint(1, 6) for i in range(5)] for j in range(6)]
print('10) ',array10)

''' 
11. Crear una funcion que realice la suma de dos arrays de dimension 1 y devuelva el array resultante. Sin utilizar el operador + directamente, sino creando un algoritmo que hiciese la suma lugar a lugar. (*a pulmon)
'''