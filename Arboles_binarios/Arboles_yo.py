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
        self.e = None

    def insertar(self, elemento):
        self.e = self._insertar(self.e, elemento, None)

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
        self._inorder(self.e)

    def _inorder(self, raiz):
        if raiz == None:
            return None
        else:
            self._inorder(raiz.izq)
            print(raiz.dato)
            self._inorder(raiz.der)

    def postorder(self):
        self._postorder(self.e)

    def _postorder(self, raiz):
        if raiz == None:
            return None
        else:
            self._postorder(raiz.izq)
            self._postorder(raiz.der)
            print(raiz.dato)

    def preorder(self):
        self._preorder(self.e)

    def _preorder(self, raiz):
        if raiz == None:
            return None
        else:
            print(raiz.dato)
            self._preorder(raiz.izq)
            self._preorder(raiz.der)

    def buscar(self, elemento):
        return self._buscar(elemento, self.e)

    def _buscar(self, elemento, raiz):
        if raiz == None:
            print("el elemento no se encuentra")
            return False
        else:
            if elemento == raiz.dato:
                print("el elemento se encuentra")
                return True
            elif elemento < raiz.dato:
                return self._buscar(elemento, raiz.izq)
            else:
                return self._buscar(elemento, raiz.der)

    def eliminar(self, elemento):
        self.e = self._eliminar(elemento, self.e)

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
                aux = cambiar(aux)
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

    def num_niveles(self):
        return self._num_niveles(self.e)

    def _num_niveles(self, raiz, num=0):
        aux = num
        if raiz == None:
            return 0
        else:
            self._num_niveles(raiz.izq, num+1)
            self._num_niveles(raiz.der, num+1)
            if num < aux:
                aux = num
        return aux

    def getMax(self):
        return self._getMax(self.e)

    def _getMax(self, raiz):
        if raiz == None:
            return None
        else:
            while raiz.der is not None:
                raiz = raiz.der
        return raiz.dato

    def getMin(self):
        return self._getMin(self.e)

    def _getMin(self, raiz):
        if raiz == None:
            return None
        else:
            while raiz.izq is not None:
                raiz = raiz.izq
        return raiz.dato

el_Arbol = Arbol()
el_Arbol.insertar(12)
el_Arbol.insertar(1)
el_Arbol.insertar(24)
el_Arbol.insertar(2)
el_Arbol.insertar(99)
el_Arbol.insertar(77)
el_Arbol.insertar(111)
el_Arbol.insertar(4)
el_Arbol.inorder()
print()

el_Arbol.eliminar(77)
el_Arbol.eliminar(2)
el_Arbol.eliminar(4)
el_Arbol.eliminar(111)
el_Arbol.inorder()
