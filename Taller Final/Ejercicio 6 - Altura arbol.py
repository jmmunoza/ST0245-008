class Nodo():
    def __init__(self, dato, padre):
        self.dato = dato
        self.izq = None
        self.der = None
        self.padre = padre
    
    def setDato(self, dato):
        self.dato = dato
    
    def setPadre(self, padre):
        self.padre = padre

class Arbol():
    def __init__(self):
        self.root = None

    def insertar(self, elemento):
        self.root = self._insertar(self.root, elemento, None)

    def _insertar(self, raiz, dato, padre):
        if raiz == None:
            raiz = Nodo(dato, padre)
        else:
            if dato < raiz.dato:
                raiz.izq = self._insertar(raiz.izq, dato, raiz)
            else:
                raiz.der = self._insertar(raiz.der, dato, raiz)
        return raiz

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, raiz):
        if raiz == None:
            return None
        else:
            self._inorder(raiz.izq)
            print(raiz.dato, end= " ")
            self._inorder(raiz.der)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, raiz):
        if raiz == None:
            return None
        else:
            self._postorder(raiz.izq)
            self._postorder(raiz.der)
            print(raiz.dato, end=" ")

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, raiz):
        if raiz == None:
            return None
        else:
            print(raiz.dato, end=" ")
            self._preorder(raiz.izq)
            self._preorder(raiz.der)

    def buscar(self, elemento):
        return self._buscar(elemento, self.root)

    def _buscar(self, elemento, raiz, altura=1):
        if raiz == None:
            print("el elemento", elemento, "no se encuentra")
            return False
        else:
            if elemento == raiz.dato:
                print("el elemento", elemento, "se encuentra en la altura ", altura)
                return True
            elif elemento < raiz.dato:
                return self._buscar(elemento, raiz.izq, altura+1)
            else:
                return self._buscar(elemento, raiz.der, altura+1)

    def eliminar(self, elemento):
        self.root = self._eliminar(elemento, self.root)

    def _eliminar(self, elemento, raiz):
        if raiz == None:
            return None
        
        elif elemento < raiz.dato:
                iz = self._eliminar(elemento, raiz.izq)
                raiz.izq = iz
        elif elemento > raiz.dato:
                de = self._eliminar(elemento, raiz.der)
                raiz.der = de 
        else:
            aux = raiz
            if aux.izq == None:
                raiz = aux.izq
            elif aux.der == None:
                raiz = aux.der
            else:
                aux = self.cambiar(aux)
            aux = None
        return raiz

    def cambiar(self, aux):
        nodo1 = aux
        nodo2 = aux.izq
        while nodo2.der is not None:
            nodo1 = nodo2
            nodo2 = nodo2.der
        aux.dato = nodo2.dato
        if nodo1 == aux:
            nodo1.izq = nodo2.izq
        else:
            nodo1.der = nodo2.der
        return nodo2

    """
        Este es el método que calcula la profundidad (Altura)
        del arbol binario.
                                                                
    """

    def num_profundidad(self):
        return self._num_profundidad(self.root)

    def _num_profundidad(self, raiz, num=0, lista=[]): # <--------------------- método del ejercicio 6
        if raiz == None:
            return 0
        else:
            self._num_profundidad(raiz.izq)
            lista.append(raiz.dato)
            self._num_profundidad(raiz.der)
        profundidad = 0
        profundidad_aux = 0
        for i in lista:
            profundidad = self.buscar_nivel(i, self.root)
            if profundidad > profundidad_aux:
                profundidad_aux = profundidad
        return profundidad_aux


    def buscar_nivel(self, elemento, raiz, altura=1):
        if raiz == None:
            return 0
        else:
            if elemento == raiz.dato:
                return altura
            elif elemento < raiz.dato:
                return self.buscar_nivel(elemento, raiz.izq, altura+1)
            else:
                return self.buscar_nivel(elemento, raiz.der, altura+1)

    def getMax(self):
        return self._getMax(self.root)

    def _getMax(self, raiz):
        if raiz == None:
            return None
        else:
            while raiz.der is not None:
                raiz = raiz.der
        return raiz.dato

    def getMin(self):
        return self._getMin(self.root)

    def _getMin(self, raiz):
        if raiz == None:
            return None
        else:
            while raiz.izq is not None:
                raiz = raiz.izq
        return raiz.dato

#   Declaramos el arbol
el_Arbol = Arbol()

#   Insertamos los nodos
el_Arbol.insertar(50)
el_Arbol.insertar(15)
el_Arbol.insertar(10)
el_Arbol.insertar(4)
el_Arbol.insertar(65)
el_Arbol.insertar(75)
el_Arbol.insertar(165)
el_Arbol.insertar(51)
el_Arbol.insertar(19)
el_Arbol.insertar(12)
el_Arbol.insertar(40)
el_Arbol.insertar(69)
el_Arbol.insertar(73)
el_Arbol.insertar(121)
el_Arbol.insertar(541)
el_Arbol.insertar(321)
el_Arbol.insertar(205)
el_Arbol.insertar(43)
el_Arbol.insertar(6)
el_Arbol.insertar(8)
el_Arbol.insertar(2)

#   Miramos su profundidad
print("La profundidad del arbol es de", el_Arbol.num_profundidad())
print()
