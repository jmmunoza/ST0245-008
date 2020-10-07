class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self, head):
        self.head = head

    def length(self):
        current = self.head
        if current is not None:
            count = 1

            while current.next is not None:
                count += 1
                current = current.next
            return count
        else:
            return 0

    def insert(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = linked_list.head
            linked_list.head = new_node
        else:
            current = linked_list.head
            k = 1
            while current.next is not None and k < position:
                current = current.next
                k += 1
            new_node.next = current.next
            current.next = new_node

    #   Este es el método del Reto2. Se ingresa un valor K, que será el número de veces
    #   que se correrá la lista. En el primer if se verifica si K es mayor a la longitud de
    #   la lista, si es así, se le aplica una operación de módulo "%" para que así solo
    #   haga los cambios necesesarios, por ejemplo, si K = 10000008 y  la longitud de la lista
    #   es 5, el número de intercambios necesarios serían 3. Así no tenemos que hacer los 
    #   otras 10000005 intercambios innecesarios.
    # 
    #   Despues de esto entramos en una while que se recorrerá K veces, y se creará un objeto
    #   que apunte a la cabeza de la lista, lo entramos en otro while hasta que apunte al elemento
    #   que está de penúltimo en la cola.
    #   Hacemos que el elemento siguiente al último elemento apunte a la cabeza, hacesmos que la
    #   cabeza apunte al último elemento y luego volvemos nulo al último elemento.

    #   En pocas palabras, tomamos el último elemento y lo ponemos de primero K veces. 
    def correr_k_veces(self, k):
        if k >= self.length():
            k = k % self.length()

        i = 1
        while i <= k:
            current = self.head
            while current.next.next is not None:
                current = current.next

            current.next.next = self.head
            self.head = current.next
            current.next = None
            i += 1

    def show_list(self):
        current = linked_list.head
        while current is not None:
            print(current.data, end = ", ")
            current = current.next   
        print()
            
#creamos la lista
linked_list = SinglyLinkedList(Node(1))

#rellenamos la lista
for i in range(2,6):
    linked_list.insert(i, i-1)


print("Lista:")
linked_list.show_list()

linked_list.correr_k_veces(10000008)
print("Lista corrida K veces:")
linked_list.show_list()
