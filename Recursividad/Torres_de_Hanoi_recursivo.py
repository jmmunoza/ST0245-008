# Juan Manuel Muñoz Arias y Juan Miguel Castro Martínez

def Hanoi(m):
    def exponente_dos(n):
        if n == 0:
           return 1
        return 2 * exponente_dos(n-1)
    return exponente_dos(m)-1

n = int(input("Dame el número de discos que vas a implementar: "))
print("Con ", n, " disco(s), es necesario ", Hanoi(n), " paso(s)")
