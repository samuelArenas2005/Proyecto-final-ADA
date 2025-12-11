import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from RBTree import RBTree, Node, RB_INSERT, PRINT_TREE
from SportsMan import SportsMan

# Crear árbol vacío
tree = RBTree(root=None)

# Crear deportistas y nodos para probar
valores = [10, 20, 30, 15, 25, 5, 1]

print("Insertando valores:", valores)
print("\n" + "="*50 + "\n")

for i, val in enumerate(valores):
    nodo = Node(
        value=val,
        sportsMan=SportsMan(id=val, name=f"Atleta {val}", age=20 + i, performance=val * 10)
    )
    
    RB_INSERT(tree, nodo)
    
    print(f"Después de insertar {val}:")
    if tree.root:
        PRINT_TREE(tree.root)
    print("\n" + "-"*50 + "\n")

print("Árbol final:")
if tree.root:
    PRINT_TREE(tree.root)
else:
    print("Árbol vacío")
