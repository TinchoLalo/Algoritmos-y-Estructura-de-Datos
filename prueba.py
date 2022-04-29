pisos = int(input('Ingresa en número la altura de la piramide: '))
estilo = input('Ingresa el estilo de la piramide: ')
long = round(pisos/2,0)
long = int(long) 
piramide = ""

for i in range(pisos):
    line= i
    space = long-i
    
    piramide = " "*space + estilo*line 
    # imprimir los pisos
    print(piramide)