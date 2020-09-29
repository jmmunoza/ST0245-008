# Construya un algoritmo para encontrar un valor específico en una matriz de valores ordenada por filas y columna. 
# El algoritmo toma como entrada una matriz de valores donde cada fila y cada columna están en orden, junto con 
# un valor para ubicar en esa matriz.  Devuelve si ese elemento existe en la matriz.
# Por ejemplo, dado la siguiente matriz y buscar el 7, el algoritmo daría como resultado sí     
# Pero si se pide encontrar el número 0, el algoritmo daría como resultado no

# He hecho dos implementaciones, el primero "buscar_matriz" tiene la ventaja de que puedes buscar elementos
# en la matriz sin la necesidad de que esta esté ordenada, su principal desventaja es su largo tiempo de ejecución
# ya que recorre la matriz entre, tanto columnas como filas.

def buscar_matriz(matriz, valor_a_buscar):
    encontrado = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_a_buscar:
                encontrado = True
                return encontrado, i, j
    return encontrado

# La segunda implementacion "buscar_matriz_binario" es una modificacion de la búsqueda binaria, esta realiza la
# búsqueda binaria en cada fila de la matriz, por lo que su mayor virtud es su corto tiempo de ejecución.
# Su mayor desventaja es que obligatoriamente la matriz debe de estar ordenada para funcionar correctamente.

def buscar_matriz_binario(matriz, valor_a_buscar):
    encontrado = False
    for i in range(len(matriz)):
        izquierda = 0
        derecha = len(matriz[i])-1
        while izquierda <= derecha and not encontrado:
            medio = (izquierda+derecha)//2
            if matriz[i][medio] == valor_a_buscar:
                encontrado = True
                return encontrado, i, medio
            elif matriz[i][medio] > valor_a_buscar:
                derecha = medio - 1
            else:
                izquierda = medio + 1
    return encontrado

matriz = [[1,2,2,2,3,4],
          [1,2,3,3,4,5],
          [3,4,4,4,4,6],
          [4,5,6,7,8,9]]
print(buscar_matriz(matriz, 8))
print(buscar_matriz_binario(matriz, 8))



