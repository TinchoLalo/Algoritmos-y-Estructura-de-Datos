'''
Trata de escribir un programa que de una lista del 1 al 10,
sustituya los múltiplos de 2 por fizz, los de 5 por buzz,
y los de 2 y 5 por fizzbuzz.
'''

lista =[1,2,3,4,5,6,7,8,9,10]

for index, value in enumerate(lista):
    fizz = value% 2==0
    buzz = value % 5 ==0
    if(fizz and buzz):
        lista[index]='fizzbuzz'
    elif(fizz):
        lista[index]='fizz'
    elif(buzz):
        lista[index]='buzz'
print(lista) # imprimir lista por de este modo: [1,2,3,4]
print('\n'.join(map(str, lista))) # imprimir lista por línea