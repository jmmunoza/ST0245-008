# Dada la siguiente lista 
# [47,3,21,32.56,92]
# Después de 2 “pasadas” de un algoritmo de ordenación, la lista ha quedado dispuesto asi
# [3,21,47,32,56,92]
# ¿Qué algoritmo de ordenación se esta utilizando (selección, burbuja o inserción)?

def Seleccion(lista):
    nb = len(lista)
    cont_pasada = 0
    print()
    print("Ordenamiento por selección")
    for actual in range(0,2):    
        mas_pequeno = actual
        for j in range(actual+1,nb) :
            if lista[j] < lista[mas_pequeno] :
                mas_pequeno = j
        if min is not actual :
            lista[mas_pequeno], lista[actual] = lista[actual], lista[mas_pequeno]
        cont_pasada += 1
        print("pasada número: ", cont_pasada)
        print(lista)
        print()

def Insercion(lista_a):
    cont_pasada = 0
    print()
    print("Ordenamiento por inserción")
    for i in range(1,3):
        valor_a_ordenar =lista_a[i]
        while lista_a[i-1] > valor_a_ordenar and i >0:
            lista_a[i], lista_a[i-1]= lista_a[i-1], lista_a[i]
            i = i-1
        cont_pasada += 1
        print("pasada número: ", cont_pasada)
        print(lista_a)
        print()
    return lista_a

def ordenamientoBurbuja(unaLista):
    cont_pasada = 0
    print()
    print("Ordenamiento por burbuja")
    for numPasada in range(len(unaLista)-1,3,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                unaLista[i+1], unaLista[i] = unaLista[i], unaLista[i+1]
        cont_pasada += 1
        print("pasada número: ", cont_pasada)
        print(unaLista)
        print()
    return unaLista


# He modificado los algoritmos de modo que solo impriman las dos primeras pasadas
unaLista = [47,3,21,32,56,92]
Seleccion(unaLista)
unaLista = [47,3,21,32,56,92]
Insercion(unaLista)
unaLista = [47,3,21,32,56,92]
ordenamientoBurbuja(unaLista)
# Como podemos ver, los algoritmos de inserción y selección son los únicos que en las 2 primeras pasadas
# modifican la lista de [47,3,21,32.56,92] a [3,21,47,32,56,92] (comprobar ejecutando el código).
# 
# El único algoritmo que no hace esto es el de burbuja, porque en una sola pasada es capaz
# de ordenar la lista correctamente. Esto ocurre por la estructura del algoritmo, que en una
# pasada corre todos números mayores a la derecha haciendo constantemente intercambios.
# 
# Internamente en la lista estaría ocurriendo esto:
# 
# Pasada 1 :
#      intercambio 1: [47, 3, 21, 32, 56, 92]
#      intercambio 2: [3, 47, 21, 32, 66, 92]
#      intercambio 3: [3, 21, 47, 32, 66, 92]
#      intercambio 4: [3, 21, 32, 47, 66, 92]
#
#
# En conclusión, se puede estar usando el algoritmo de selección o el algoritmo por inserción.
#
# 