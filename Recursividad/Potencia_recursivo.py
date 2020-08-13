# Juan Manuel Muñoz Arias y Juan Miguel Castro Martínez

def Potencia(x, n):
    if(n == 0):
        return 1
    return x * Potencia(x, n-1)

x = int(input("Dame el valor de la base x: "))
n = int(input("Dame el valor del exponente n: "))
print(n, " elevado a ", x, " es igual a ", Potencia(x, n))