'''
Mostrar un arbolito de navidad en consola. La altura debe ser definida por el usuario. 
Ejemplo: arbolito de cuatro pisos de altura más la estrella y la base.

     ++
    ****
   ======
  ********
 ==========
     ==
'''

pisos = int(input('Ingresa en número la altura del arbol: '))

for i in range(0,pisos+1):
    par =  i%2==0 
    line= i+1
    space = pisos-i
    # imprimir la estrella
    if(i == 0):
        print(' '*(pisos+line-1)+'++') 
    # si es para el piso es *
    elif(par and i != pisos):
        print(' '*space+'**'*line)
    # si se imprimieron todos los pisos imprimir la base
    elif(i == pisos):
        print(' '*(pisos)+'==')
    # imprimir los pisos impares
    else:
        print(' '*space+ '=='*line)
