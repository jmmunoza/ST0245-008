# Se cuenta con una lista de tuplas 

futbolistasTup = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"), (14, "Xabi Alonso"),
                  (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"), (6, "Iniesta"), (7, "Villa")]

futbolistasTup.sort(key=lambda futbolista: futbolista[0])
print(futbolistasTup)

# a)	Que resultado se obtiene al aplicar el método .sort

# La lista se ordena de forma que que el valor numérico de cada tupla quede de mayor a menor:

# [(1, 'Casillas'), (3, 'Pique'), (5, 'Puyol'), (6, 'Iniesta'), (7, 'Villa'), (8, 'Xavi Hernandez'),
#  (11, 'Capdevila'), (14, 'Xabi Alonso'), (15, 'Ramos'), (16, 'Busquets'), (18, 'Pedrito')]


# b)	Que se esta especificando en los parámetro (key=lambda futbolista: futbolista[0])

# Se está indicando que a la hora de ordenar las tuplas, se tomará en cuenta solamente el primer
# elemento de cada tupla, que en este caso son los números que identifican a los jugadores.

# c)	Aplique este metodo a las listas de los punto 1,3, 4. Que conclusión puede obtener

listaPuntoUno = [4,7,11,4,9,5,11,7,3,5]
listaPuntoUno.sort(key=lambda futbolista: futbolista[0])
listaPuntoTres = [47,3,21,32.56,92]
listaPuntoTres.sort(key=lambda futbolista: futbolista[0]) 
listaPuntoCuatro = [8, 43, 17, 6, 40, 16, 18, 97, 11, 7] 
listaPuntoCuatro.sort(key=lambda futbolista: futbolista[0])

# Esto produce un error, que en palabras de python es que un elemento entero no es subscriptable.
# Esto ocurre porque al utilizar el metodo sort con key=lamba, python interpreta que los elementos
# de la lista son por así decirlo "contenedores" de otras listas, diccionarios, arreglo, etc. Y como
# los elementos de la lista son enteros, esto produce un error. A diferencia de lo que ocurre con el 
# arreglo de tuplas de futbolistas, que cada elemento es un "contenedor".

# d)	Por favor según  opinión realice una tupla con  los mejores inventos del 2019 . 
# Donde usted califica el que mas le gusta o le parece importante. 
# Anotación la escala con la que usted cuenta es de 1 a 100 ( no tiene que asignar ninguno de los extremos si no lo desea)  

TopInventos2019y2020 = [(70,"PC que incluye una PS4 Y Xbox"), (85,"RTX 3090"), (90,"Xbox Series X"), (88,"PlayStation 5"),
                        (73,"HTC Vive Pro Eye"), (92,"Xbox Series S"), (70,"CareOS "), (100,"RTX 3070"),
                        (84,"Dr. CaRo"), (81,"Valorant"), (73,"Televisor 8K de LG"), (77,"OrCam MyEye2"), (95,"Hydraloop")]
TopInventos2019y2020.sort(key=lambda inventos: inventos[0])
print(TopInventos2019y2020)