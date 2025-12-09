from dataclasses import dataclass
from typing import Optional
from SportsMan import SportsMan

"""Implementación de un Árbol Rojinegro (Red-Black Tree)"""

#Implementa la estructura de un nodo del árbol rojinegro
@dataclass
class Node:
    value: int
    sportsMan: SportsMan #Modificacion
    isBlack: bool = False
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None

#Implementa la estructura del árbol rojinegro
@dataclass
class RBTree:
    root: Optional[Node]
    size: int = 0

#Implementa la rotación izquierda en el árbol rojinegro
def LEFT_ROTATE(T: RBTree, x: Node):
    y = x.right
    x.right = y.left
    if y.left != None:
        y.left.parent = x
    y.parent = x.parent
    if (x.parent == None):
        T.root = y
    elif (x == x.parent.left):
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y

#Implementa la rotación derecha en el árbol rojinegro
def RIGHT_ROTATE(T: RBTree, x: Node):
    y = x.left
    x.left = y.right
    if y.right != None:
        y.right.parent = x
    y.parent = x.parent
    if x.parent == None:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.right = x
    x.parent = y

#Implementa la inserción de un nodo en el árbol rojinegro
def TREE_INSERT(T: RBTree, x: Node):
    y = None
    z = T.root
    while z != None:
        y = z
        if x.value < z.value:
            z = z.left
        elif x.value > z.value:
            z = z.right
        else:  # x.value == z.value
            # Si tienen el mismo rendimiento, comparar por edad
            if x.sportsMan.age > z.sportsMan.age:
                z = z.left  # Mayor edad va a la izquierda (primero)
            else:
                z = z.right  # Menor o igual edad va a la derecha (después)
    x.parent = y
    if y == None:
        T.root = x
    elif x.value < y.value:
        y.left = x
    elif x.value > y.value:
        y.right = x
    else:  # x.value == y.value
        # Si tienen el mismo rendimiento, comparar por edad
        if x.sportsMan.age > y.sportsMan.age:
            y.left = x  # Mayor edad va a la izquierda (primero)
        else:
            y.right = x  # Menor o igual edad va a la derecha (después)

#Implementa la función de inserción en el árbol rojinegro con balanceo
def RB_INSERT(T: RBTree, x: Node):
    TREE_INSERT(T, x)
    T.size += 1  # Incrementar el tamaño del árbol
    x.isBlack = False  # color[z] <- RED
    while x.parent != None and x.parent.isBlack == False:  # while color[p[x]]=RED
        if x.parent == x.parent.parent.left:  # do if p[x]=left[p[p[x]]]
            y = x.parent.parent.right  # then y <- right[p[p[z]]]
            if y != None and y.isBlack == False:  # if color[y]=RED
                # Caso 1
                x.parent.isBlack = True  # color[p[x]] <- BLACK
                y.isBlack = True  # color[y] <- BLACK
                x.parent.parent.isBlack = False  # color[p[p[x]]] <- RED
                x = x.parent.parent  # x <- p[p[x]]
            else:
                if x == x.parent.right:  # if x=right[p[x]]
                    # Caso 2
                    x = x.parent  # x <- p[x]
                    LEFT_ROTATE(T, x)  # LEFT-ROTATE(T,x)
                # Caso 3
                x.parent.isBlack = True  # color[p[x]] <- BLACK
                x.parent.parent.isBlack = False  # color[p[p[x]]] <- RED
                RIGHT_ROTATE(T, x.parent.parent)  # RIGHT-ROTATE(T,p[p[x]])
        else:  # procedimiento simétrico cambiando "right" por "left"
            y = x.parent.parent.left
            if y != None and y.isBlack == False:
                # Caso 1
                x.parent.isBlack = True
                y.isBlack = True
                x.parent.parent.isBlack = False
                x = x.parent.parent
            else:
                if x == x.parent.left:
                    # Caso 2
                    x = x.parent
                    RIGHT_ROTATE(T, x)
                # Caso 3
                x.parent.isBlack = True
                x.parent.parent.isBlack = False
                LEFT_ROTATE(T, x.parent.parent)
    T.root.isBlack = True  # color[root[T]] <- BLACK

#Implementa la función para imprimir el árbol rojinegro
def PRINT_TREE(node: Node, prefix: str = "", is_tail: bool = True):
    """Imprime el árbol rojinegro en consola"""
    if node is None:
        # Mostrar hojas NIL en negro
        print(prefix + ("└── " if is_tail else "├── ") + "\033[90mNIL\033[0m")
        return
    
    # Rojo: \033[91m, Negro: \033[90m, Reset: \033[0m
    color_code = "\033[90m" if node.isBlack else "\033[91m"
    print(prefix + ("└── " if is_tail else "├── ") + f"{color_code}{node.value}\033[0m")
    
    # Mostrar siempre ambos hijos (izquierdo y derecho)
    extension = "    " if is_tail else "│   "
    PRINT_TREE(node.left, prefix + extension, False)
    PRINT_TREE(node.right, prefix + extension, True)

#Implementa la función para encontrar el nodo con el valor máximo en el árbol rojinegro
def TREE_MAXIMUM(node: Node) -> Node:
    while node.right is not None:
        node = node.right
    return node

#Implementa la función para encontrar el nodo con el valor mínimo en el árbol rojinegro
def TREE_MINIMUM(node: Node) -> Node:
    while node.left is not None:
        node = node.left
    return node