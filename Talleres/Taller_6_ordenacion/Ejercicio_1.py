#Se desea eliminar todos los números duplicados de una lista  
#Por ejemplo 
#Si se le ingresan los valores [4,7,11,4,9,5,11,7,3,5]
#Se debe cambia a [4,7,11,9,5,3]

def eliminar_duplicados1(lista):
    i = len(lista) - 1
    while i > 0:
        if lista.count(lista[i]) > 1:
            del(lista[i])
            i = len(lista) - 1
            continue
        i -= 1
    return lista

lista = [4, 7, 11, 4, 9, 5, 11, 7, 3, 5]

eliminar_duplicados1(lista)
print(lista)