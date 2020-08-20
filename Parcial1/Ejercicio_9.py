#Ejercicio 9 Pascal

def triangulo(n_filas, i = 0, j = 0):
    def  pascal(row, column):
        if row < 0 and column < 0:
            return 0
        elif column == 0 or column == row:
            return 1
        return pascal(row - 1, column-1) + pascal(row-1, column)

    if i == n_filas:
        return ""
    if j == i:
        print(pascal(i, j))
        return triangulo(n_filas, i+1, 0)
    print(pascal(i, j), end="  ")
    return triangulo(n_filas, i, j+1)

n = int(input("Cuantas filas deseas imprimir del Triángulo de Pascal: "))
triangulo(n)
