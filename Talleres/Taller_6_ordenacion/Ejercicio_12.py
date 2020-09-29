# El algoritmo de RadixSort consiste en tomar los valores de la lista que se
# ingrese y tomar el último dígito de cada valor, y dependiendo de dicho dígito,
# el valor se almacenará en una nueva lista en la posición que coincida con el
# dígito. Si no queda claro, acá un ejemplo:
# 
# Ingresamos la lista [23,43,57,132,2]
# entonces el algoritmo empezará con 23, toma su último dígito, que es 3, y almacena
# el número 23 en una nueva lista en la posición que coincide con el último digito 3
# Por lo que quedaría así:
# ListaNueva = [[],[],[],[23],[],[],[],[],[],[]]
# Repetirá este proceso hasta terminar de recorrer la lista, quedando la lista nueva así:
# ListaNueva = [[],[],[132, 2],[23, 43],[],[],[],[57],[],[]] 
# Tras esto, se vaciará la lista y se agregarán los valores de la lista nueva en el orden
# en que está, quedando así:
# lista = [132, 2, 23, 43, 75]
# Se vaciará la lista nueva y se repetirá el proceso, pero ahora no con los últimos dígitos,
# si no con los penúltimos, posteriormente con los antepenúltimos y así sucesivamente hasta
# llegar al número de dígito que sea igual al número de digitos del número con más dígitos
# en la lista, por lo que si por ejemplo, en la lista el elemento 354321 es el número con más
# dígitos, el proceso de ordenamiento descrito previamente se debe repetir 6 veces, que son los
# dígitos de 354321.
#
# Abajo dejo el código que hice yo mismo.

# Nota: no sé si sea que implementé mal el algoritmo o sean limitaciones del mismo, pero me presenta 
# fallas con los números negativos.

def RadixSort(lista):
    decimales = [[],[],[],[],[],[],[],[],[],[]]
    max,div = 0, 1

    def cuantos_digitos(n):
        ind = 1
        while n > 9:
            n = n / 10
            ind = ind + 1
        return ind

    for i in lista:
        if cuantos_digitos(i) > max:
            max = cuantos_digitos(i)

    for i in range(max):
        for j in lista:
            decimales[(j//div)%10].append(j)
        lista = []
        for j in decimales:
            lista.extend(j)
        decimales = [[],[],[],[],[],[],[],[],[],[]]
        div *= 10
    return lista
            
lista = [64,56,1,54,654,654,646,546,210,20]

# El algoritmo de Binsort consiste en tomar una lista y separar sus elementos en unas "casillas".
# En estas casillas solo pueden haber números con unas condiciones únicas que varían dependiendo
# de cada casilla. Por ejemplo, en una casiila solo se guardan los números entre el 1 al 10, 
# en otra los números entre el 11 al 20, y así sucesivamente. 

# Una vez están separados los números en sus respectivas casillas, se ordenan las casillas individualmente
# con el método de ordenamiento que se prefiera, se puede utilizar burbuja, selección, inserción,
# quick, shell, mezcla, etc.

# Ya que estén ordenadas todas las casillas, estas se agregan  a la lista inicial, obviamente vaciándola para
# que no se acumulen elementos. Y ya que las casillas ordenadas se agregaron en la lista, se retorna.

# Para este ejemplo de Binsort, me basé en código externo, ya que sinceramente me dio dificultad implementar
# el método por mi propia cuenta. El método que utilicé para ordenar cada casilla fué el de inserción.

# Nota: Me ocurrió algo similar que con el RadixSort, cuando ingreso valores negativos pero me presenta 
# fallas y no ordena correctamente.

def BinSort(lista):
    def insercion(lista):
        for i in range(1, len(lista)):
            valor_a_ordenar = lista[i]
            while lista[i-1] > valor_a_ordenar and i > 0:
                lista[i], lista[i-1] = lista[i-1], lista[i]
                i -= 1
        return lista

    max_valor = max(lista)
    size = max_valor/len(lista)
    lista_nueva= []
    for i in range(len(lista)):
        lista_nueva.append([]) 

    for i in range(len(lista)):
        j = int (lista[i] / size)
        if j != len(lista):
            lista_nueva[j].append(lista[i])
        else:
            lista_nueva[len(lista)-1].append(lista[i])

    for i in range(len(lista)):
        insercion(lista_nueva[i])
            
    lista_ordenada = []
    for i in range(len (lista)):
        lista_ordenada = lista_ordenada + lista_nueva[i]
    return lista_ordenada

lista = BinSort(lista)
print(lista)