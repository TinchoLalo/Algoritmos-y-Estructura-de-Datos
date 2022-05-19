numero = int(input("Introduce un número en base 10: "))
numero2 = int(input("Introduce un número en base 10: "))

def suma(n1,n2): return bin(int(n1,2)+n2)
def resta(n1,n2): return bin(int(n1,2)-n2)

print(f'Suma: {suma(numero,numero2)}\nResta: {resta(numero,numero2)}')