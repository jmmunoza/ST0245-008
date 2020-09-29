import operator
# Dada una lista voto[0.......n-1], donde cada elemento de lista representa
# un voto en las elecciones. Suponga que cada voto se da como un número entero
# que representa el ID del candidato elegido. Desarrolle un algoritmo para
# determinar quién gana la elección. Determine la complejidad del algoritmo 

def eliminar_duplicados(lista):
    i = 0
    while i < len(lista):
        if lista.count(lista[i]) > 1:
            del(lista[i])
            if i != 0:
                i -= 1
            continue
        i += 1
    return lista

def Elecciones(voto):
    num_votos, cont, diccionario_votos = [], 1, {}
    voto.sort()
    for i in range(len(voto)):
        if i+1 == len(voto):
            num_votos.append(cont)
        elif voto[i] == voto[i+1]:
            cont += 1
        else:
            num_votos.append(cont)
            cont = 1
    eliminar_duplicados(voto)
    for i in range(len(voto)):
        diccionario_votos[voto[i]] = num_votos[i]
    return diccionario_votos

def Imprimir_resultados(voto):
    resultados = sorted(Elecciones(voto).items(), key=operator.itemgetter(1))
    resultados.reverse()
    for i in resultados:
        print("El candidato con la ID", i[0], "obtuvo", i[1], "voto(s)")
    print("")
    print("El ganador es el candidato con la ID", resultados[0][0])

lista = [2514, 2511, 2510, 2510, 2513, 2512, 2512, 2515, 2514, 2510, 2515,
         2510, 2513, 2513, 2514, 2515, 2514, 2513, 2513, 2512, 2510, 2513,
         2515, 2512, 2515, 2512, 2510, 2511, 2514, 2514, 2514, 2511, 2513,
         2513, 2513, 2511, 2514, 2512, 2512, 2512, 2512, 2515, 2514, 2511,
         2511, 2514, 2513, 2514, 2513, 2515, 2511, 2513, 2512, 2510, 2511,
         2510, 2513, 2510, 2511, 2511, 2513, 2512, 2510, 2511, 2513, 2510,
         2514, 2511, 2512, 2511, 2515, 2510, 2513, 2514, 2513, 2512, 2513,
         2510, 2513, 2510, 2510, 2511, 2512, 2513, 2510, 2511, 2514, 2513,
         2515, 2514, 2513, 2514, 2510, 2515, 2514, 2511, 2515, 2512, 2511,
         2515, 2512, 2510, 2513, 2512, 2510, 2513, 2513, 2510, 2511, 2514,
         2513, 2515, 2510, 2512, 2511, 2510, 2511, 2515, 2514, 2512, 2515,
         2513, 2512, 2514, 2515, 2510, 2512, 2514, 2511, 2512, 2515, 2512,
         2511, 2513, 2511, 2515, 2514, 2514, 2513, 2511, 2514, 2510, 2510,
         2510, 2515, 2510, 2513, 2513, 2512, 2514, 2512, 2510, 2511, 2512,
         2510, 2513, 2514, 2514, 2511, 2514, 2511, 2514, 2514, 2513, 2513,
         2510, 2511, 2512, 2511, 2515, 2515, 2513, 2514, 2515, 2513, 2515,
         2515, 2512, 2510, 2512, 2512, 2514, 2515, 2514, 2513, 2511, 2512,
         2514, 2514, 2513, 2515, 2515, 2513, 2511, 2515, 2513, 2512, 2513,
         2511, 2513, 2512, 2512, 2514, 2511, 2512, 2510, 2514, 2510, 2514,
         2515, 2511, 2515, 2514, 2515, 2511, 2512, 2511, 2514, 2513, 2512,
         2514, 2515, 2515, 2515, 2511, 2510, 2511, 2511, 2514, 2513, 2513,
         2515, 2511, 2513, 2514, 2512, 2515, 2510, 2514, 2510, 2515, 2514,
         2510, 2510, 2513, 2510, 2514, 2510, 2511, 2513, 2513, 2515, 2511,
         2512, 2515, 2510, 2511, 2513, 2510, 2510, 2513, 2514, 2513, 2513,
         2511, 2513, 2510, 2511, 2514, 2515, 2514, 2515, 2514, 2513, 2512,
         2513, 2515, 2511, 2515, 2510, 2510, 2512, 2512, 2513, 2510, 2513,
         2511, 2511, 2512, 2510, 2512, 2515, 2514, 2513, 2515, 2510, 2515,
         2512, 2514, 2512, 2513, 2514, 2510, 2511, 2511, 2511, 2511, 2511,
         2515, 2514, 2515, 2514, 2514, 2510, 2515, 2510, 2514, 2515, 2510,
         2510, 2513, 2510, 2511, 2513, 2512, 2512, 2510, 2512, 2510, 2514,
         2515, 2511, 2510, 2510, 2510, 2510, 2515, 2510, 2512, 2514, 2515,
         2512, 2511, 2512, 2510, 2514, 2511, 2513, 2513, 2515, 2515, 2511,
         2513, 2510, 2510, 2513, 2512, 2512, 2510, 2514, 2515, 2514, 2515,
         2514, 2515, 2515, 2510, 2510, 2513, 2512, 2510, 2514, 2513, 2511,
         2513, 2511, 2512, 2511, 2514, 2515, 2510, 2513, 2510, 2514, 2510,
         2510, 2514, 2514, 2513, 2513, 2511, 2515, 2514, 2513, 2513, 2511,
         2511, 2514, 2512, 2515, 2514, 2515, 2512, 2514, 2514, 2513, 2512,
         2515, 2512, 2513, 2511, 2514, 2513, 2515, 2510, 2515, 2511, 2514,
         2514, 2512, 2514, 2510, 2511, 2513, 2511, 2515, 2512, 2513, 2513,
         2515, 2511, 2511, 2513, 2513, 2510, 2515, 2510, 2510, 2510, 2514,
         2512, 2514, 2511, 2512, 2513, 2512, 2515, 2512, 2510, 2511, 2511,
         2510, 2514, 2515, 2514, 2511, 2511, 2514, 2512, 2515, 2511, 2510,
         2514, 2514, 2512, 2514, 2513, 2513, 2513, 2510, 2511, 2511, 2512,
         2510, 2510, 2512, 2511, 2511, 2514, 2512, 2510, 2512, 2510, 2513,
         2513, 2515, 2513, 2513, 2510, 2511, 2510, 2510, 2513, 2512, 2511,
         2510, 2512, 2513, 2512, 2510, 2513, 2514, 2515, 2510, 2515, 2515,
         2514, 2513, 2511, 2512, 2512, 2515, 2512, 2510, 2515, 2512, 2511,
         2513, 2514, 2511, 2511, 2515, 2512, 2515, 2512, 2513, 2513, 2514,
         2515, 2513, 2514, 2513, 2514, 2512, 2510, 2513, 2514, 2510, 2512,
         2513, 2510, 2510, 2511, 2511, 2512, 2515, 2511, 2510, 2510, 2514,
         2512, 2515, 2514, 2515, 2511, 2510, 2514, 2513, 2511, 2513, 2515,
         2510, 2515, 2512, 2514, 2512, 2515, 2513, 2510, 2512, 2514, 2515, 
         2510, 2511, 2511, 2513, 2510, 2513, 2513, 2512, 2515, 2514, 2510,
         2511, 2515, 2514, 2514, 2512, 2510, 2514, 2511, 2511, 2512, 2513, 
         2511, 2514, 2510, 2513, 2513, 2515, 2510, 2515, 2511, 2515, 2510,
         2515, 2511, 2514, 2514, 2515, 2515, 2511, 2515, 2515, 2514, 2512, 
         2514, 2510, 2514, 2511, 2510, 2510, 2514, 2515, 2511, 2513, 2512, 
         2510, 2515, 2514, 2512, 2510, 2511, 2511, 2513, 2513, 2513, 2513, 
         2511, 2513, 2510, 2511, 2510, 2511, 2513, 2515, 2512, 2513, 2515, 
         2513, 2510, 2512, 2513, 2514, 2515, 2511, 2510, 2514, 2510, 2512, 
         2515, 2510, 2512, 2510, 2515, 2514, 2511, 2515, 2513, 2513, 2512, 
         2511, 2513, 2512, 2510, 2513, 2515, 2513, 2514, 2511, 2512, 2510,
         2514, 2510, 2510, 2510, 2515, 2512, 2515, 2513, 2512, 2514, 2510,
         2512, 2510, 2511, 2514, 2512, 2511, 2512, 2511, 2510, 2515, 2512,
         2513, 2510, 2510, 2513, 2515, 2513, 2511, 2514, 2512, 2511, 2515,
         2510, 2513, 2514, 2513, 2513, 2512, 2511, 2512, 2512, 2515, 2511,
         2512, 2513, 2510, 2510, 2515, 2513, 2513, 2512, 2510, 2512, 2510,
         2510, 2515, 2510, 2510, 2510, 2515, 2514, 2512, 2511, 2512, 2514,
         2510, 2515, 2511, 2511, 2514, 2513, 2515, 2511, 2513, 2515, 2510, 
         2514, 2510, 2510, 2510, 2513, 2512, 2513, 2513, 2513, 2514, 2515]


Imprimir_resultados(lista)


"""
Como se puede ver, la complejidad de este algoritmo es algo alta. Es por esto
que analizaremos tanto el mejor como el peor de los casos.
El mejor caso para este algoritmo es cuando todos los votos son iguales, por lo
que van dirigidos a la misma persona. El peor de los casos es cuando todos los votos
van dirigitos a distintas personas.

Analicemos primero la complejidad del mejor de los casos, para eso veremos la complejidad de los 3
métodos por separado:

Como vimos en ejercicios anteriores, la complejidad de "eliminar_duplicados(lista)" tiene dos casos.
En esta situación que es que todos los votos van a la misma persona, vemos que todos los elementos están
repetidos, por lo que la complejidad en este caso es de 5n - 2.

Complejidad de "Elecciones(voto)":
    1               asignación num_votos

    1               asignación cont

    1               asingación diccionario_votos

    1               voto.sort()

    2n + 2          declaración de un for

    n               comparaciones if i+1 == len(voto)

    n - 1           comparaciones elif voto[i] == voto[i+1]

    n - 1           suma cont += 1

    1               num_votos.append(cont)

    1               llamado eliminar_duplicados(voto)

    4               declaración de un for que solo hará
                    el recorrido una sola vez. Debido a 
                    que eliminamos los duplicados de votos
                    y por ende la longitud de votos queda de
                    1. La primera acción es la asignación de
                    i, el segundo es la comparación de i < len(votos),
                    el tercero es el incremento i+=1, y el cuarto
                    la comparación extra que realiza el for.

    1               se realiza una sola vez la acción "diccionario_votos[voto[i]] = num_votos[i]"   

    1               return diccionario_votos

Sumamos todo esto, y tenemos que la complejidad de Elecciones es igual a 5n + 14. Y si le sumamos la complejidad de
eliminar_duplicados(voto), queda (5n + 12) + (5n - 2) = 10n + 10, donde n es la cantidad de votos.

Podemos despreciar a Imprimir_resultados(voto), debido a que solo imprime los datos y no influye en el funcionamiento
de algoritmos de una forma trascendente.

Ahora debemos ver el peor caso, en que todos los votos son para distintas personas. 

Como ya vimos, la complejidad de "eliminar_duplicados(lista)" tiene dos casos.
En esta situación que es que todos los votos van a distintas personas, vemos que todos los elementos son distintos,
por lo que la complejidad en este caso es de 3n. 

Complejidad de Elecciones(voto):
    1               asignación num_votos

    1               asignación cont

    1               asingación diccionario_votos

    1               voto.sort()

    2n + 2          declaración de un for

    n               comparaciones if i+1 == len(voto)

    n - 1           comparaciones elif voto[i] == voto[i+1]

    n - 1           num_votos.append(cont) del else

    n - 1           cont = 1 del else

    1               num_votos.append(cont) del primer if

    1               llamado eliminar_duplicados(voto)

    2n + 2          declaración de un for       

    n               diccionario_votos[voto[i]] = num_votos[i]

    1               return diccionario_votos    

Sumamos todo esto, y tenemos que la complejidad de Elecciones es igual a 9n +8. Y si le sumamos la complejidad de
eliminar_duplicados(voto), queda (9n + 8) + (3n) = 12n + 8, donde n es la cantidad de votos.

Como se dijo previamente, se puede despreciar Imprimir resultados porque no influye en el funcionamiento.

En conclusión, este algoritmo en el mejor de los casos (Todos votan por la misma persona) es de 10n + 10. Mientras
que en el peor de los casos (Todos votan por distintos candidatos) es de 12n + 8. Ambas complejidades en notación 
big O se denotan O(n).

Podemos comprobar que estas dos complejidades coinciden con el algoritmo porque siempre que hay un elemento, debe de
dar el mismo resultado, comprobemos.

Mejor caso:

    10n + 10 = 10(1) + 10
             = 10 + 10
             = 20

Peor caso:

    12n + 8 = 12(1) + 8
            = 12 + 8
            = 20
  
"""