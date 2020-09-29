def Omerge(unaLista):
    print("Dividir ",unaLista)
    if len(unaLista)>1:
        mitad = len(unaLista)//2
        mitadIzquierda = unaLista[:mitad]
        mitadDerecha = unaLista[mitad:]
        ## LLamada recursiva para cada lista 
        Omerge(mitadIzquierda)
        Omerge(mitadDerecha)
        i,j,k=0,0,0
        while i < len(mitadIzquierda) and j < len(mitadDerecha):
            if mitadIzquierda[i] < mitadDerecha[j]:
                unaLista[k]=mitadIzquierda[i]
                i=i+1
            else:
                unaLista[k]=mitadDerecha[j]
                j=j+1
            k=k+1
        while i < len(mitadIzquierda):
            unaLista[k]=mitadIzquierda[i]
            i=i+1
            k=k+1

        while j < len(mitadDerecha):
            unaLista[k]=mitadDerecha[j]
            j=j+1
            k=k+1
    print("Mezclar ",unaLista)



lista =  [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40] 
Omerge(lista)

# Como se puede apreciar al correr el código, en la tercera llamada recursiva
# la lista estaría fragmentada en 8 secciones, ya que se se hacen dos llamados recursivos a la vez.

# en la pasada 0 la lista sería igual a [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]

# en la pasada 1 la lista sería igual a [21, 1, 26, 45, 29, 28, 2, 9] [16, 49, 39, 27, 43, 34, 46, 40] 

# en la pasada 2 la lista sería igual a [21, 1, 26, 45] [29, 28, 2, 9] [16, 49, 39, 27] [43, 34, 46, 40]

# en la pasada 3 la lista sería igual a [21, 1] [26, 45] [29, 28] [2, 9] [16, 49] [39, 27] [43, 34] [46, 40]


# esto ocurre ya que en el algoritmo de mezcla, primero se debe de dividir la lista  hasta que cada
# sublista tenga un solo elemento, y apartir de ahí ordenar. pero acá se puede ver que las sublistas no tienen
# longitud uno, por lo que continua en su proceso de división.