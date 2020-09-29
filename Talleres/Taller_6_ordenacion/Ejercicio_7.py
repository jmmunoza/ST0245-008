# Diseñe e implemente una función para encontrar todos los valores negativos dentro de
# una lista dada. Tu función debería devolver una nueva lista que contiene los valores negativos. 
# ¿Cuándo ocurre el peor de los casos y cuál es el tiempo de ejecución para ese caso?


def lista_negativos(lista):
    negativos = []
    for i in lista:
        if i < 0:
            negativos.append(i)
    return negativos

lista = [1,2,4,5,6,56,5,45,4,5,-5,3,-2,2,-2,-5,89,5,5,5,-5]
lista = lista_negativos(lista)
print(lista)

# El peor de los casos es cuando todos los elementos en la lista son negativos,
# porque aparte de crear la lista negativos, recorrer toda la lista, comparar si
# cada valor iterado es menor a cero, retornar negativos, debe tambien agregar dicho valor a la lista
# negativos. El mejor de los casos es cuando ningún elemento es negativo, por lo que hace
# todas las acciones dichas previamente, excepto la de agregar elementos a la lista negativos
#
# es por lo anterior dichamente que el tiempo de ejecución de el peor de los casos es
# de 4n + 4, donde n es el número de elementos de la lista. Mientras que en el mejor de los
# casos, el tiempo de ejecución es de 3n + 4, ya que no tiene que agregar elementos a negativos
# n veces, por lo que se resta. La complejidad cdl algoritmo en notación big O sería O(n).