'''
11. Realizar un programita que le pida ingresar una frase al usuario y coloque cada palabra de la misma como elemento de una lista.
'''
frase11 = str(input("11) Ingrese una frase: "))
palabra11 = []
palabra = ""
j = 0

for i,value in enumerate(frase11):
    if (frase11[i] == ' '):
        palabra11.append(frase11[j:i])
        j = i+1
    elif (i == len(frase11)-1):
        palabra11.append(frase11[j:i+1])
        j = i+1
print("11) ",palabra11)