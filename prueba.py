pisos = int(input('Ingresa en número la altura de la piramide: '))
estilo = input('Ingresa el estilo de la piramide: ')

piramide = ""

for i in range(pisos):
    line= i
    space = pisos-i
    
    piramide = " "*space + estilo*line +estilo*line  
    # imprimir los pisos
    print(piramide)
    
for i in range(pisos):
    line= i
    space = pisos-i
    
    piramide = " "*space+estilo*line 
    # imprimir los pisos
    print(piramide)