# pedimos al usuario su mes y día de nacimiento
mes = str(input('Ingresa el mes de nacimiento: ')).lower()
dia = int(input('Ingresa el dia de nacimiento: '))

# definimos dos listas con los meses y los signos
meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

signos = ['acuario', 'piscis', 'aries', 'tauro', 'geminis', 'cancer', 'leo', 'virgo', 'libra', 'escorpio', 'sagitario', 'capricornio']

# comparamos el mes y el dia para saber el signo
for i, value in enumerate(meses):        
    if (mes == meses[i] and dia >= 21 and dia <= 31):
        print('Tu signo es:', signos[i])
    elif (mes == meses[i] and dia >= 1 and dia <= 20):
        print('Tu signo es:', signos[i-1])
        
        
