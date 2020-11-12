class Nodo():
    def __init__(self, dato, padre, n):
        self.dato = dato
        self.izq = None
        self.der = None
        self.padre = padre
        self.n = n
    
    def setDato(self, dato):
        self.dato = dato
    
    def setPadre(self, padre):
        self.padre = padre

class Arbol():
    def __init__(self):
        self.root = None

    def insertar(self, n, elemento):
        self.root = self._insertar(self.root, n, elemento, None)

    def _insertar(self, raiz, n, dato, padre):
        if raiz == None:
            raiz = Nodo(dato, padre, n)
        else:
            if n < raiz.n:
                raiz.izq = self._insertar(raiz.izq, n, dato, raiz)
            else:
                raiz.der = self._insertar(raiz.der, n, dato, raiz)
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
            print(raiz.dato, end= " ")

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, raiz):
        if raiz == None:
            return None
        else:
            print(raiz.dato, end=" ")
            self._preorder(raiz.izq)
            self._preorder(raiz.der)

def postOrden(inorder, preorder, arbol):
    inorder_dicc, preorder_dicc = [], []
    for i in range(len(inorder)):
        aux = [inorder[i], i]
        inorder_dicc.append(aux)
    for i in range(len(preorder)):
        n = 0
        for j in range(len(preorder)):
            if inorder_dicc[j][0] == preorder[i]:
                n = j
                break
        aux = [preorder[i], n]
        preorder_dicc.append(aux)

    arbol = Arbol()
    
    for i in range(len(preorder)):
        arbol.insertar(preorder_dicc[i][1], preorder_dicc[i][0])
    

    return arbol




Arbolito = Arbol()
preorder = ["G","E","A","I","B","M","C","L","D","F","K","J","H"]
inorder  = ["I","A","B","E","G","L","C","D","F","M","K","H","J"]

Pe = postOrden(inorder, preorder, Arbolito)
Pe.preorder()
print()
Pe.inorder()
print()
Pe.postorder()

