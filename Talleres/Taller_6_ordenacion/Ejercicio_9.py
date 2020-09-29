"""
La clase Set construye funciones que son demasiados útiles a la 
hora de administrar listas para poner en marcha los algoritmos de ordenamiento o de búsqueda. Entre
dichas funciones podemos encontrar la longitud de un algoritmo, si tiene un determinado valor, iterar
elementos, etc.
"""

class Set:

    """
    Este método es el constructor de la clase, inicializa la variable theElements y
    le asigna una lista vacía. Su complejidad es de 1. En notación big O es O(1).
    """
    def __init__(self):
        self._theElements = list()

    """
    Este método retorna el número de elementos que posee la lista theElements. Su complejidad
    es de 1. En notación big O es O(1).
    """
    def __len__(self):
        return len(self._theElements)

    """
    Este método recibe por parámetros una variable element  e inicializa una variable ndx a la cual
    se le asigna la posición de element en theElements si este se encuentra en el mismo. Posteriormente
    retorna un valor booleano en donde, en pocas palabras, si element se encuentra en theElements, se
    retorna True, en caso contrario se retorna un False.
    La complejidad de este método aumenta un poco, vamos:

        1           asignación ndx
        1           comparación ndx < len(next)
        1           comparación self._theElements[ndx] == element
        1           return booleano

    Se ve que tiene una complejidad de 4, pero sigue siendo constante. Es por esto que en notación big O sería
    O(1).
    """
    def __contains__(self, element):
        ndx = self._findPosition(element)
        return ndx < len(next) and self._theElements[ndx] == element
    
    """
    Este método se encarga de agregar elementos que no se encuentren en theElements a la cola del mismo.
    Primero pregunta en el if si element no se encuentra en theElements. Si no se encuentra, inicializa
    un nodo ndx con la última posición de la lista. Y finalmente agrega el elemento en theElements
    en la última posición.

    Ya que contamos con un if, hay dos posibilidades de complejidad. La complejidad menor será cuando el 
    elemento si se encuentre en la lista, porque solo haría una comparación. Por ende tiene una complejidad de 1.
    En el peor de los casos será cuando el elemento no se encuentre, por lo que aparte de hacer la comparación, 
    hará una asignacón y una insercióm. Por ende su complejidad es 3. Ambas en notación big O son O(1).
    """
    def add(self, element):
        if element not in self:
            ndx = self._findPosition(element)
            self._theElements.insert(ndx, element)

    """
    Este método ingresa por parámetros un elemento, si el elemento está en la lista, asignará un nodo ndx que contenga
    la posición del elemento a borrar, y llamará la función pop en el valor de ndx, borrando así el elemento. Por el contrario,
    lanzará este mensaje de error "The element must be in the set.". Podemos ver este assert "element in self" como un if,
    por lo que este método tiene dos complejidades. El mejor de los casos en cuanto a complejidad es cuando el elemento
    no está en la lista, ya que se activará la línea de assert y parará el programa, teniendo así la complejidad de 1.
    Si el elemento si se encuentra, entonces aparte de asegurarse de que el elemento si se encuentre, debe de realizar la
    asignación de ndx y llamar la función pop(). Por lo que tiene una complejidad de 3. En notación big O tienen O(1).
    """
    def remove(self, element):
        assert element in self, "The element must be in the set."
        ndx = self._findPositon(element)
        self._theElements.pop(ndx)

    """
    Este método entra por parámetros una sublista, y se encarga de preguntar si todos los elementos que se encuentran en theElements
    se encuentran en la sublista, si es así, se retorna True. De lo contrario, retorna False. En este método tenemos tres casos.
    El mejor de los casos es cuando se encuentra un elememento en theELements que no se encuentra en la sublista antes de que se termine 
    de recorrer todo el for. Su complejidad será de 4 < 3n + 1. Recordar que n es el número de elementos de theElements. 
    
    En el peor de los casos es cuando el elemento en theElements no se encuentra en la sublista pero en la última
    posición de la lista, o cuando si es sublista de theElements. En ambos casos existe una complejida de 3n + 3. 
    """
    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True

    """
    Este método funciona retornar un apuntador de theElements, el cual sirve para recorrer la lista, entre muchas más opciones. 
    Su complejidad es de 1, y su notación en big O es de O(1).
    """
    def __iter__(self):
        return _SetIterator(self._theElements)

    """
    Este método recibe por parámetros un elemento y, si este se encuentra en theElements, retornará la posición en que se encuentra.
    Si se analiza correctamente el código, es basícamente una implementación de búsqueda binaria, por lo que su complejidad será 
    de log(n). En notación big O será O(log(n)).
    """
    def _findPosition(self, element):
        low = 0
        high = len(theList) - 1
        while low <= high:
            mid = (high + low)/2
            if theList[mid] == target:
                return mid
            elif target < theList[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low