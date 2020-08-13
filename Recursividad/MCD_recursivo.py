# Juan Manuel Muñoz Arias y Juan Miguel Castro Martínez

def MCD(a, b):
    c = a % b
    if c == 0:
        return b
    return MCD(b, c)

a = int(input("Dame el valor del primer número: " ))
b = int(input("Dame el valor del segundo número: " ))

print("El MCD que hay entre ", a, " y ", b, " es ", MCD(a,b))