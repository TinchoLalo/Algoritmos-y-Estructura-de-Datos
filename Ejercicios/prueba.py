
archivo = str(input('6) Ingrese el nombre del archivo: '))
ext = 0
final = 0

for i,value in enumerate(archivo):
    #reemplazo los espacios por guiones bajos
    if (archivo[i] == ' '):
        archivo = archivo.replace(archivo[i], '_')
    #reemplazo la extension por numeros
    elif (archivo[i]== '.'):
        final = i+1
        ext = archivo[i::]
        ext = '#' * (len(ext)-1)
print("6) ",archivo[0:final]+ext)