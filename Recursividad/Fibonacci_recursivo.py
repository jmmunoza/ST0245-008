# Juan Manuel Muñoz Arias y Juan Miguel Castro Martínez

def Fibonacci(n):
    if n <= 1:
        return 1    
    return Fibonacci(n-2)+Fibonacci(n-1)

n = int(input("Dame un número para determinar en la serie Fibonacci: "))
print("La posición ", n, " equivale a el número ", Fibonacci(n), " en la suceción Fibonacci")