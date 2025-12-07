from RBTree import RBTree, Node, RB_INSERT, print_tree
from modelos import sportsMan

# Crear árbol vacío
tree = RBTree(root=None)

# Crear deportistas y nodos para probar
valores = [10, 20, 30, 15, 25, 5, 1]

print("Insertando valores:", valores)
print("\n" + "="*50 + "\n")

for i, val in enumerate(valores):
    deportista = sportsMan()
    deportista.id = val
    deportista.name = f"Atleta {val}"
    deportista.age = 20 + i
    deportista.performance = val * 10
    
    nodo = Node(
        value=val,
        sportsMan=deportista,
        isBlack=True,
        left=None,
        right=None,
        parent=None
    )
    
    RB_INSERT(tree, nodo)
    
    print(f"Después de insertar {val}:")
    if tree.root:
        print_tree(tree.root)
    print("\n" + "-"*50 + "\n")

print("Árbol final:")
if tree.root:
    print_tree(tree.root)
else:
    print("Árbol vacío")
