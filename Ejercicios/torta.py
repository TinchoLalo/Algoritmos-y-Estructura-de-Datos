'''
Mostrar una torta en consola con el relleno y el piso ingresado por el usuario, 
al igual que la altura y el ancho. 
Ejemplo: torta de dos pisos de altura, diez de ancho y las velas.

    """"""""""
    ==========
    **********
    ==========

'''

piso = input('Ingrese el estilo del piso de la torta: ')
relleno = input('Ingrese el relleno de la torta: ')
altura = int(input('Ingrese la cantidad de tapas de la torta: '))
ancho = int(input('Ingrese el ancho de la torta: '))
velas = '"'

for i in range(0,altura+1):
    par = i % 2==0
    if(i==0 ):
        print(velas*ancho)
    elif(par and i != 0 and i != altura):
        print(relleno*ancho)
    else:
        print(piso*ancho)