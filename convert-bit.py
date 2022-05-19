
numero = int(input("Introduce un número en base 10: ")) 
base = int(input("Introduce la base: ")) 

def binario(numero,base):
    bit = ''
    while numero !=0:
        bit = str(numero % base) + bit
        numero = numero // base
    if (len(bit)!=8):
        bit2 = "0"*(8-len(bit)-1)+bit
    return str(numero) + bit2
if (numero > 0):
    print("Bin: ",binario(numero,base)) 
    binari =str(binario(numero,base)) 
    


def complemento(binari):
    c1 = ''
    for i,value in enumerate(binari):
        if (binari[i] == "0"):
            c1 += "1"
        else:
            c1+= "0"
    return c1

if (base == 2):
    print("C1: ",complemento(binari))
    print("C2: ",bin(int(complemento(binari),2)+1))
    
# sumarle uno a c2
