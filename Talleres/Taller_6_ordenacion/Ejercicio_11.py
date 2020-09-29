#se tiene una lista A de 100 elementos A[ a1……a100  ] 
#                   B de 60 elementos    B[ b1……b60  ]  
#Se desean resolver las siguientes tareas
#a.)	Ordenar cada lista aplicando el método Quicksort
#b.)	Crear un lista C que sea la unión de la lista A y B
#c.)	Ordenar la lista C y visualizarla

def QuickSort(lista):
    izq, der, centro = [], [], []
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista)-1]
    for i in lista:
        if i < pivote:
            izq.append(i)
        elif i > pivote:
            der.append(i)
        else:
            centro.append(i)
    return QuickSort(izq) + centro + QuickSort(der)

# Declarando las listas

A = [3,5,6,7,4,6,4,6,2,97,12,54,67,85,34,13,64,97,23,67,76,23,756,
     345,12,45,43,345,34534,535,35,34,54,1,7,34,1,98,5,55,12,54,65,
     76,76,43,34,234,23,2365,7,767,6,666,645,464,654,6451,22,223,89,
     11,541,15,12,5,54,21,2,156,4698,464,121,45,45,454,54,21,21,21,
     54,32,34,35,58,74,8532,2,321,4,1,2,5,9,54,321,68,87,21,1]

B = [5,43,6,45,64,2,5,7,65,2,12,4,7657,987,2,872,567,5567,234,5,4,
     32,45,3,6,7,657,3,2,3,56,7345,235,87038,1,27,62,83,83,3,83,38,
     27,26,251,1,62,67,8,75753,345,3,56,54,75,56,34,64,456,4]

# a.)	Ordenar cada lista aplicando el método Quicksort

A = QuickSort(A)
B = QuickSort(B)

# b.)	Crear un lista C que sea la unión de la lista A y B

C = []
C.extend(A); C.extend(B)

# c.)	Ordenar la lista C y visualizarla

C = QuickSort(C)

print("Lista C: ", C)