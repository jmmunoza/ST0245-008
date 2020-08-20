#Ejercicio 8 Tarjeta de Identidad
#Se puede ingresar tu TI completa ;)

def Punto_8(n):
    if n % 100 == 0:
        return 0
    print(n % 100)
    return Punto_8(n - 1)

n = int(input("Dame tu TI: "))
Punto_8(n)
