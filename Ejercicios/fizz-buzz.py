''' Trata de escribir un programa que muestre los números de 1 al 100,
sustituyendo los múltiplos de 3 por fizz, los de 5 por buzz,
y los de 3 y 5 por fizzbuzz.'''

for i in range(0,100):
    fizz = i % 3 ==0
    buzz = i % 5 ==0
    if(fizz and buzz):
        print('fizzbuzz')
    elif(fizz):
        print('fizz')
    elif(buzz):
        print('fizz')
    else:
        print(i)
        
        
