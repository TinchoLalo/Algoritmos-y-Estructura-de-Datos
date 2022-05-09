base = int(input('Ingresa en número la longitud de la base de la piramide: '))
estilo = str(input('Ingresa el estilo de la piramide: '))
pisos = round(base/2)
piramide = []
for i in range(pisos):
    piramide.append(' '*i + estilo*(base-2*i))
for i in reversed(piramide):
    print(i)
    
    
# otro método
pisos = int(input('Ingresa en número la altura de la piramide: '))
pisos = round(pisos/2)

for i in range(0,pisos):
    line= i+1
    space = pisos-i
    # imprimir los pisos
    print(' '*space+'#'*line+'#'*line)