# Elimine los elementos duplicados de un vector ordenado.
# ¿Cuál es la eficiencia del método?
# Compárela con la eficiencia del punto 1

# El algoritmo desprecia si la lista está ordenada o no, por lo que
# no importa si está ordenada o no, la eficiencia será igual.
# En donde se ve afectada la eficiencia es dependiendo de cuantos elementos
# duplicados hay en la lista. Por lo que, en el mejor de los casos, que es cuando
# no hay elementos repetidos, la lista tiene la siguiente complejidad:

#   1       asignación i = len(lista) - 1
#   n       comparaciones de i > 0 en el while
#   n - 1   comparaciones de lista.count(lista[i]) > 1
#   n - 1   decrementos i -= 1
#   1       return lista

#   esto da igual a una complejidad de 3n (n = numero elementos de lista) en el caso
#   que ningún elemento esté repetido (Mejor de los casos)

# En el peor de los casos, es cuando todos los elementos están duplicados, como en el caso
# de [1, 1, 1, 1, 1, 1], la lista tendrá la siguiente complejidad:

#   1       asignación i = len(lista) - 1
#   n + 1   comparaciones de i > 0 en el while
#   n       comparaciones de lista.count(lista[i]) > 1
#   n - 2   del(lista[i])
#   n - 2   i = len(lista) - 1
#   n - 2   continue
#   1       i -= 1
#   1       return lista

#   esto da igual a una complejidad de 5n - 2 (n = numero elementos de lista) en el caso
#   que todos los elementos estén repetidos (Peor de los casos)

#   Ambas complejidades en notación big O son O(n)

#   Abajo dejo el algoritmo del ejercicio 1 modificado para que tambíen cuente su complejidad
#   y puedas hacer las respectivas pruebas.

def eliminar_duplicados1(lista):
    i = len(lista) - 1
    cont = 1            # asignación i = len(lista) - 1
    while i > 0:        
        cont += 1       # comparaciones de i > 0 en el while
        cont += 1       # comparaciones de lista.count(lista[i]) > 1
        if lista.count(lista[i]) > 1:
            cont += 1   # del(lista[i])
            cont += 1   # i = len(lista) - 1
            cont += 1   # continue
            del(lista[i])
            i = len(lista) - 1
            continue
        i -= 1
        cont += 1       # i -= 1
    cont += 1           # comparacion extra de i > 0 en el while
    cont += 1           # return lista
    print(cont)
    return lista

lista = [1,1,1,1,1]

eliminar_duplicados1(lista)
print(lista)