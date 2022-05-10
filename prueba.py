cont = 0
def pares(a,b):
    if a <= b:
        cont = 0
        for i in range(a,b+1):
            if i % 2 == 0:
                cont += 1
        return cont
print('16) ',pares(1,10))