from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    key: int
    data: any
    next: "Node" = None
    prev: "Node" = None

@dataclass
class LinkedList:
    head: Optional[Node] = None
    tail: Optional[Node] = None
    size: int = 0

def LIST_INSERT(L: LinkedList, x: Node):
    L.size += 1
    x.next = L.head
    if L.head != None:
        L.head.prev = x
    L.head = x
    x.prev = None

def LIST_SEARCH(L: LinkedList, key) -> Optional[Node]:
    x = L.head
    while x != None and x.key != key:
        x = x.next
    return x

def LIST_DELETE(L: LinkedList, x: Node):
    L.size -= 1
    if x.prev != None:
        x.prev.next = x.next
    else:
        L.head = x.next
    if x.next != None:
        x.next.prev = x.prev

def LIST_MERGE_SORT(L: LinkedList):
    """Ordena la lista enlazada usando merge sort"""
    if L.size <= 1:
        return
    
    L.head = MERGE_SORT_AUXILIAR(L.head)
    
    # Actualizar tail después del ordenamiento
    current = L.head
    while current.next is not None:
        current = current.next
    L.tail = current

def MERGE_SORT_AUXILIAR(head: Node) -> Node:
    """Función auxiliar recursiva para merge sort"""
    if head is None or head.next is None:
        return head
    
    # Dividir la lista en dos mitades
    middle = GET_MIDDLE(head)
    next_to_middle = middle.next
    middle.next = None
    
    # Ordenar recursivamente cada mitad
    left = MERGE_SORT_AUXILIAR(head)
    right = MERGE_SORT_AUXILIAR(next_to_middle)
    
    # Combinar las dos mitades ordenadas
    return MERGE(left, right)

def GET_MIDDLE(head: Node) -> Node:
    """Encuentra el nodo medio de la lista usando dos punteros"""
    if head is None:
        return head
    
    slow = head
    fast = head
    
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def MERGE(left: Node, right: Node) -> Node:
    """Combina dos listas ordenadas en una sola lista ordenada"""
    if left is None:
        return right
    if right is None:
        return left
    
    result = None
    
    if left.key < right.key:
        result = left
        result.next = MERGE(left.next, right)
        if result.next is not None:
            result.next.prev = result
        result.prev = None
    elif left.key > right.key:
        result = right
        result.next = MERGE(left, right.next)
        if result.next is not None:
            result.next.prev = result
        result.prev = None
    else:  # left.key == right.key
        # Si las llaves son iguales, comparar por número de jugadores
        if left.data.get_number_of_sportsmen() >= right.data.get_number_of_sportsmen():
            result = left
            result.next = MERGE(left.next, right)
            if result.next is not None:
                result.next.prev = result
            result.prev = None
        else:
            result = right
            result.next = MERGE(left, right.next)
            if result.next is not None:
                result.next.prev = result
            result.prev = None
    
    return result

def PRINT_LINKED_LIST(L: LinkedList):
    """Imprime la lista enlazada de forma visual"""
    if L.head is None:
        print("Lista vacía")
        return
    
    print(f"Size: {L.size}")
    print("Forward: ", end="")
    current = L.head
    while current is not None:
        print(f"[{current.key}]", end="")
        if current.next is not None:
            print(" <-> ", end="")
        current = current.next
    print()
    
    print("Backward: ", end="")
    current = L.tail
    while current is not None:
        print(f"[{current.key}]", end="")
        if current.prev is not None:
            print(" <-> ", end="")
        current = current.prev
    print("\n" + "-" * 50)