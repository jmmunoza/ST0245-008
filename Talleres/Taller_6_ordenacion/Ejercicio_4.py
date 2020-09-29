# Utilizar el algoritmo de ordenación SHELL, encuentre las pasadas e
# intercambios que se realizan para  la ordenación de la siguiente lista
# [8, 43, 17, 6, 40, 16, 18, 97, 11, 7] 

# He modificado el algoritmo de shell_sort para que imprima tanto las pasadas
# como los intercambios que realiza. Abajo dejo los resultados que se obtuvieron.
# Obviamente coinciden con la premisa del algoritmo, que es subdivir la lista en
# en pequeños intervalos que cada vez se hacen más pequeños.

def shell_short1(lista):
    sublista = len(lista)//2
    cont, cont1 = 0, 0
    while sublista > 0:
        cont += 1
        print("Pasada número ", cont)
        print(lista)
        print()
        for i in range(len(lista)):
            for j in range(i+sublista, len(lista), sublista):
                actual = lista[j]
                posicion = j
                while posicion >= sublista and lista[posicion-sublista] > actual:
                    lista[posicion] = lista[posicion-sublista]
                    posicion = posicion - sublista
                    cont1 += 1
                    print("         Intercambio número ", cont1)
                    print("         ",lista)
                    print()
                lista[posicion] = actual
        sublista = sublista//2
    cont += 1
    print("Pasada número ", cont)
    print(lista)
    print()
    
""" 
    Pasada número  1
    [8, 43, 17, 6, 40, 16, 18, 97, 11, 7] 

            Intercambio número  1
            [8, 43, 17, 6, 40, 16, 43, 97, 11, 7] 

            Intercambio número  2
            [8, 18, 17, 6, 40, 16, 43, 97, 11, 40]

    Pasada número  2
    [8, 18, 17, 6, 7, 16, 43, 97, 11, 40] 

            Intercambio número  3
            [8, 18, 17, 6, 17, 16, 43, 97, 11, 40]

            Intercambio número  4
            [8, 18, 8, 6, 17, 16, 43, 97, 11, 40]

            Intercambio número  5
            [7, 18, 8, 6, 17, 16, 43, 97, 43, 40]

            Intercambio número  6
            [7, 18, 8, 6, 17, 16, 17, 97, 43, 40]

            Intercambio número  7
            [7, 18, 8, 18, 11, 16, 17, 97, 43, 40]

            Intercambio número  8
            [7, 6, 8, 18, 11, 18, 17, 97, 43, 40]

            Intercambio número  9
            [7, 6, 8, 16, 11, 18, 17, 97, 43, 97]

    Pasada número  3
    [7, 6, 8, 16, 11, 18, 17, 40, 43, 97]

            Intercambio número  10
            [7, 7, 8, 16, 11, 18, 17, 40, 43, 97]

            Intercambio número  11
            [6, 7, 8, 16, 16, 18, 17, 40, 43, 97]

            Intercambio número  12
            [6, 7, 8, 11, 16, 18, 18, 40, 43, 97]

    Pasada número  4
    [6, 7, 8, 11, 16, 17, 18, 40, 43, 97]
 """

lista = [8, 43, 17, 6, 40, 16, 18, 97, 11, 7] 
shell_short1(lista)