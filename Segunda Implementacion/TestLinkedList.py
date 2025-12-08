from LinkedList import LinkedList, Node, LIST_INSERT, LIST_SEARCH, LIST_DELETE, LIST_MERGE_SORT, PRINT_LINKED_LIST

# Test 1: Inserción al inicio
print("=" * 50)
print("TEST 1: LIST_INSERT (insertar al inicio)")
print("=" * 50)
lista = LinkedList()
for val in [5, 3, 7, 1]:
    node = Node(key=val, data=f"Dato {val}")
    LIST_INSERT(lista, node)
    print(f"Insertado: {val}")
    PRINT_LINKED_LIST(lista)

# Test 2: Búsqueda
print("\n" + "=" * 50)
print("TEST 2: LIST_SEARCH (búsqueda)")
print("=" * 50)
print("Lista actual:")
PRINT_LINKED_LIST(lista)
for key in [7, 15, 1]:
    result = LIST_SEARCH(lista, key)
    if result:
        print(f"✓ Encontrado: key={key}, data={result.data}")
    else:
        print(f"✗ No encontrado: key={key}")

# Test 3: Eliminación
print("\n" + "=" * 50)
print("TEST 3: LIST_DELETE (eliminar nodo)")
print("=" * 50)
print("Lista antes de eliminar:")
PRINT_LINKED_LIST(lista)

# Eliminar el nodo con key=5
node_to_delete = LIST_SEARCH(lista, 5)
if node_to_delete:
    LIST_DELETE(lista, node_to_delete)
    print(f"Eliminado nodo con key=5")
    PRINT_LINKED_LIST(lista)

# Eliminar el primer nodo
if lista.head:
    first_key = lista.head.key
    LIST_DELETE(lista, lista.head)
    print(f"Eliminado primer nodo (key={first_key})")
    PRINT_LINKED_LIST(lista)

# Test 4: Merge Sort
print("\n" + "=" * 50)
print("TEST 4: LIST_MERGE_SORT (ordenar con merge sort)")
print("=" * 50)
lista_desordenada = LinkedList()
valores = [45, 23, 67, 12, 89, 34, 56, 78, 9]
print(f"Insertando valores desordenados: {valores}")
for val in valores:
    node = Node(key=val, data=f"Dato {val}")
    LIST_INSERT(lista_desordenada, node)

print("\nLista antes de ordenar:")
PRINT_LINKED_LIST(lista_desordenada)

LIST_MERGE_SORT(lista_desordenada)
print("Lista después de ordenar con MERGE_SORT:")
PRINT_LINKED_LIST(lista_desordenada)

# Verificar que está ordenada
print("\nVerificación de orden:")
current = lista_desordenada.head
is_sorted = True
while current and current.next:
    if current.key > current.next.key:
        is_sorted = False
        break
    current = current.next
print(f"¿Lista ordenada correctamente? {'✓ SÍ' if is_sorted else '✗ NO'}")

print("\n" + "=" * 50)
print("TODOS LOS TESTS COMPLETADOS")
print("=" * 50)
