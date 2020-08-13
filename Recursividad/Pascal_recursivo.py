# Juan Manuel Muñoz Arias y Juan Miguel Castro Martínez

def Pascal(n, i = 0, j = 0): 
    def combinatoria(n, m):
        if m == 0 or m == n:
            return 1
        return combinatoria(n-1, m-1) + combinatoria(n-1, m)
    
    if i == n:
        return ""
    if j == i:
        print(combinatoria(i, j))
        return Pascal(n, i+1, 0)
    print(combinatoria(i, j), end="  ")
    return Pascal(n, i, j+1)
    
n = int(input("Cuantas filas deseas imprimir del Triángulo de Pascal: "))
Pascal(n)