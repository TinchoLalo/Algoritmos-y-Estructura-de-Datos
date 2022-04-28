'''Implementar un programa que le permita al usuario ingresar su día y mes de nacimiento (no la fecha, solo el día, controlando que este entre 1 y 31) y el mes de nacimiento (como texto, enero, febrero, etc.) y determine de qué signo zodiacal es.'''

dia = int(input("Ingrese su día de nacimiento: "))
mes = str(input("Ingrese su mes de nacimiento: "))

meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

signos = ["Acuario","Pisis","Aries","Tauro","Geminis","Cancer","Leo","Virgo","Libra","Escorpio","Sagitario","Capricornio"]
       

if (dia >= 1 and dia <= 31):
    if (mes == "diciembre" and dia >= 21 and dia <= 31 or mes == "enero" and dia >=1 and dia <= 21):
            print("Su signo zodiacal es: Capricornio")
    else:
        for i, value in enumerate(meses):
            if (mes == meses[i] and dia >=21 and dia <=31 or mes == meses[i+1] and dia >=1 and dia <=21 ):
                print("Su signo zodiacal es: ",signos[i])



        
'''
lista = []
count = 0
# repetimos un bucle 4 veces para pedir al usuario un número y añadirlo a una lista
while(count<4):
    n = int(input("Ingrese un número: "))
    lista.append(n)
    count+=1
# mostramos la lista en pantalla
print(sorted(lista))
'''


