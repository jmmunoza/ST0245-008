"""
    Claramente se puede ver que se está tratando con una lista enlazada, por lo que esta
    es la estructura de datos usada en este algoritmo.
"""
class Alumno:
    """
        Complejidad constructor, 3. Ya que se hacen tres declaraciones.
        En Big O sería O(1)
    """
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    """
        Este método tiene complejidad 1 ya que solo se realiza un retorno.
        En Big O sería O(1)
    """
    def __str__(self):
       return self.nombre+' - '+str(self.edad)+' años :'+str(self.nota)


class Nodo:
    """
        Complejidad constructor, 2. Ya que se hacen dos declaraciones.
        En Big O sería O(1)
    """
    def __init__(self, datos = None, siguiente = None):
        self.datos = datos
        self.siguiente = siguiente

class linked_list: 
    """
        Complejidad constructor, 1. Ya que se hace una declaración.
        En Big O sería O(1)
    """
    def __init__(self):
        self.primero = None
    
    """
        Complejidad agregar, 3. Ya que se hace una declaracion (complejidad 1) y 
        se construye un Noso (complejidad 2).
        En Big O sería O(1)
    """
    # Método para agregar elementos a la lista
    def agregar(self, datos):
        self.primero = Nodo(datos=datos, siguiente=self.primero) 

    """
        Complejidad del método de 3n + 2. Donde n es el número de nodos
        en la lista. La complejidad en Big O sería de O(n)
    """
    # Método para imprimir la lista de nodos
    def mostrar( self ):
        nodo = self.primero       # <-- una declaracion, complejidad 1
        while nodo != None:       # <-- la condicion del while se verifica n + 1 veces
            print(nodo.datos)     # <-- se imprmie n veces
            nodo = nodo.siguiente # <-- se asigna n veces

"""
    Código sin optimizar:

"""

primero = None                    # <-- declaracion primero, complejidad 1
alumno = Alumno('Alex', 30, 8.9)  # <-- asignacion (complejidad 1) y constructor Alumnos (complejidad 3)
nodo = Nodo(alumno)               # <-- asignacion (complejidad 1) y constructor Nodo (complejidad 2)
nodo.siguiente = primero          # <-- asginación (complejidad 1)

"""
    Este es el proceso que se hace en el código sin optimizar, el cual consta de 9 pasos.
    Por lo que para agregar a n cantidad de estudiantes, la complejidad será de 9n.

"""

primero = nodo               
alumno = Alumno('Pepe', 27, 3.7)
nodo = Nodo(alumno)
nodo.siguiente = primero
primero = nodo

"""
    Para el caso de este while, en donde se imprimen los estudiantes, se tendrá una 
    complejidad de 3n + 2, donde n es el numero de estudiantes.

    Agregandole la complejidad para agregar un estudiante (9n) a la de imprimir el estudiante (3n+2)
    Se tiene que la complejidad del algoritmo sin optimizar es de 12n + 2. En notación Big O es O(n).

"""
n = primero         # <-- declaracion n, complejidad 1
while n != None:    # <-- declaracion while, se realizarán n + 1 comparaciones
 print(n.datos)     # <-- el print se repite n veces
 n = n.siguiente    # <-- esta asignacion se repite n veces


"""
    Codigo optimizado:

    Acá abajo se encuentra el código mejorado en el cual  se reducen evidentemente la cantidad de lineas.
    Evaluemos la complejidad,
"""

lista = linked_list()                       # <-- asignacion (complejidad 1) y constructor Linked list (complejidad 1)
lista.agregar(Alumno('Alex', 30, 8.9))      # <-- metodo agregar (ya arriba se explicó que su complejidad es de 3) y
                                            #     se llama el constructor de Alumno (complejidad 3)
"""
    Como se ve, las 5 líneas que se requerían para agregar un estudiante se resumen en una sola. La complejidad para
    agregar ahora un estudiante consta de 6 pasos. Por lo que la complejidad para agregar n estudiantes es de 6n
"""
lista.agregar(Alumno('Pepe', 27, 3.7))    

"""
    Ahora, ya teniendo la complejidad del método mostrar (3n + 2), la complejidad de agregar estudiantes (6n) y 
    la creacion del objeto de tipo Linked list (2), se tiene que la complejidad del nuevo algoritmo es de 9n + 4. 
    Mostrando una gran ventaja frente al primer codigo donde su complejidad era de 12n + 2. En notacion big O ambos
    algoritmos serían O(n)

    Por ejemplo, si se necesitaran agregar 1000 estudiantes, el antiguo código lo lograría en 12002 pasos, mientras
    que el nuevo código optimizado lo lograría en 9004 pasos.
"""
lista.mostrar() # Imprimimos la lista       # <-- metodo mostrar (ya arriba se explicó que su complejidad es de 3n + 2)