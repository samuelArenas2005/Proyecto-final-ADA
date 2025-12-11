import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from PrimeraImplementacion.Models import (
    Deportista, Equipo, Sede, bucket_sort, counting_sort
)

# =============================================================================
# PRUEBA 1: Desempate de EQUIPOS por cantidad de deportistas (bucket_sort)
# =============================================================================

# Crear deportistas de prueba
deportistas_grupo1 = [
    Deportista(1, "Juan", 25, 75),
    Deportista(2, "Maria", 30, 75),
    Deportista(3, "Pedro", 35, 75),
]

deportistas_grupo2 = [
    Deportista(4, "Ana", 20, 75),
    Deportista(5, "Carlos", 28, 75),
]

deportistas_grupo3 = [
    Deportista(6, "Laura", 22, 75),
    Deportista(7, "Diego", 40, 75),
    Deportista(8, "Sofia", 26, 75),
    Deportista(9, "Miguel", 33, 75),
]

# Crear equipos con el MISMO rendimiento promedio (75) pero diferente cantidad de deportistas
equipo1 = Equipo("Futbol", deportistas_grupo1)
equipo1.calcularRendimientoPromedio()

equipo2 = Equipo("Baloncesto", deportistas_grupo2)
equipo2.calcularRendimientoPromedio()

equipo3 = Equipo("Voleibol", deportistas_grupo3)
equipo3.calcularRendimientoPromedio()

equipos = [equipo1, equipo2, equipo3]

print("\n" + "="*80)
print("PRUEBA 1: DESEMPATE DE EQUIPOS por cantidad de deportistas (bucket_sort)")
print("="*80)

print("\nANTES DEL ORDENAMIENTO:")
print("-" * 80)
for equipo in equipos:
    print(f"Equipo: {equipo.deporte:<20} Rendimiento: {equipo.rendimientoPromedio:.2f}  Deportistas: {equipo.numeroDeportistas}")

print("\nDESPUÉS DEL ORDENAMIENTO (bucket_sort):")
print("-" * 80)

equipos_ordenados = bucket_sort(equipos, "rendimientoPromedio")

for equipo in equipos_ordenados:
    print(f"Equipo: {equipo.deporte:<20} Rendimiento: {equipo.rendimientoPromedio:.2f}  Deportistas: {equipo.numeroDeportistas}")

print("\nVERIFICACIÓN:")
print("   Todos tienen rendimiento igual (75)")
print("   Orden esperado por cantidad de deportistas (descendente):")
print("    1. Voleibol (4 deportistas)")
print("    2. Futbol (3 deportistas)")
print("    3. Baloncesto (2 deportistas)")

# Verificar que el orden es correcto
orden_correcto = (
    equipos_ordenados[0].deporte == "Voleibol" and equipos_ordenados[0].numeroDeportistas == 4 and
    equipos_ordenados[1].deporte == "Futbol" and equipos_ordenados[1].numeroDeportistas == 3 and
    equipos_ordenados[2].deporte == "Baloncesto" and equipos_ordenados[2].numeroDeportistas == 2
)

if orden_correcto:
    print("\n ¡PRUEBA 1 EXITOSA!")
else:
    print("\n ERROR en Prueba 1")

# =============================================================================
# PRUEBA 2: Desempate de SEDES por cantidad de equipos (bucket_sort)
# =============================================================================

print("\n\n" + "="*80)
print("PRUEBA 2: DESEMPATE DE SEDES por cantidad de equipos (bucket_sort)")
print("="*80)

# Crear sedes con MISMO rendimiento promedio pero diferente cantidad de equipos
deportistas_temp1 = [Deportista(10+i, f"Dep{i}", 25, 75) for i in range(3)]
deportistas_temp2 = [Deportista(20+i, f"Dep{i}", 25, 75) for i in range(3)]
deportistas_temp3 = [Deportista(30+i, f"Dep{i}", 25, 75) for i in range(3)]
deportistas_temp4 = [Deportista(40+i, f"Dep{i}", 25, 75) for i in range(3)]
deportistas_temp5 = [Deportista(50+i, f"Dep{i}", 25, 75) for i in range(3)]

eq_s1_1 = Equipo("Deporte1", deportistas_temp1)
eq_s1_1.calcularRendimientoPromedio()

eq_s2_1 = Equipo("Deporte1", deportistas_temp2)
eq_s2_1.calcularRendimientoPromedio()
eq_s2_2 = Equipo("Deporte2", deportistas_temp3)
eq_s2_2.calcularRendimientoPromedio()

eq_s3_1 = Equipo("Deporte1", deportistas_temp4)
eq_s3_1.calcularRendimientoPromedio()
eq_s3_2 = Equipo("Deporte2", deportistas_temp5)
eq_s3_2.calcularRendimientoPromedio()

sede1 = Sede("Medellin", [eq_s1_1])
sede1.calcularRendimientoPromedio()

sede2 = Sede("Bogota", [eq_s2_1, eq_s2_2])
sede2.calcularRendimientoPromedio()

sede3 = Sede("Cali", [eq_s3_1, eq_s3_2])
sede3.calcularRendimientoPromedio()

sedes = [sede1, sede2, sede3]

print("\nANTES DEL ORDENAMIENTO:")
print("-" * 80)
for sede in sedes:
    print(f"Sede: {sede.nombre:<20} Rendimiento: {sede.rendimientoPromedio:.2f}  Equipos: {sede.numeroEquipos}")

print("\nDESPUÉS DEL ORDENAMIENTO (bucket_sort):")
print("-" * 80)

sedes_ordenadas = bucket_sort(sedes, "rendimientoPromedio")

for sede in sedes_ordenadas:
    print(f"Sede: {sede.nombre:<20} Rendimiento: {sede.rendimientoPromedio:.2f}  Equipos: {sede.numeroEquipos}")

print("\nVERIFICACIÓN:")
print("   Todas tienen rendimiento igual (75)")
print("   Orden esperado por cantidad de equipos (descendente):")
print("    1. Cali (2 equipos)")
print("    2. Bogota (2 equipos)")
print("    3. Medellin (1 equipo)")

orden_correcto_sedes = (
    sedes_ordenadas[2].nombre == "Medellin" and sedes_ordenadas[2].numeroEquipos == 1
)

if orden_correcto_sedes:
    print("\n ¡PRUEBA 2 EXITOSA!")
else:
    print("\n ERROR en Prueba 2")

# =============================================================================
# PRUEBA 3: Desempate de DEPORTISTAS por edad (counting_sort)
# =============================================================================

print("\n\n" + "="*80)
print("PRUEBA 3: DESEMPATE DE DEPORTISTAS por edad (counting_sort)")
print("="*80)

# Crear deportistas con MISMO rendimiento pero diferente edad
deportistas_desempate = [
    Deportista(100, "Juan", 25, 80),
    Deportista(101, "Maria", 35, 80),    # Mismo rendimiento, más vieja
    Deportista(102, "Pedro", 20, 80),    # Mismo rendimiento, más joven
    Deportista(103, "Ana", 30, 80),      # Mismo rendimiento
]

print("\nANTES DEL ORDENAMIENTO:")
print("-" * 80)
for dep in deportistas_desempate:
    print(f"ID: {dep.id:<3} Nombre: {dep.nombre:<15} Edad: {dep.edad:<3} Rendimiento: {dep.rendimiento}")

print("\nDESPUÉS DEL ORDENAMIENTO (counting_sort):")
print("-" * 80)

deportistas_ordenados = counting_sort(deportistas_desempate, "rendimiento")

for dep in deportistas_ordenados:
    print(f"ID: {dep.id:<3} Nombre: {dep.nombre:<15} Edad: {dep.edad:<3} Rendimiento: {dep.rendimiento}")

print("\nVERIFICACIÓN:")
print("   Todos tienen rendimiento igual (80)")
print("   Orden esperado por edad (descendente):")
print("    1. Maria (35 años)")
print("    2. Ana (30 años)")
print("    3. Juan (25 años)")
print("    4. Pedro (20 años)")

orden_correcto_deport = (
    deportistas_ordenados[0].nombre == "Maria" and deportistas_ordenados[0].edad == 35 and
    deportistas_ordenados[1].nombre == "Ana" and deportistas_ordenados[1].edad == 30 and
    deportistas_ordenados[2].nombre == "Juan" and deportistas_ordenados[2].edad == 25 and
    deportistas_ordenados[3].nombre == "Pedro" and deportistas_ordenados[3].edad == 20
)

if orden_correcto_deport:
    print("\n ¡PRUEBA 3 EXITOSA!")
else:
    print("\n ERROR en Prueba 3")

# =============================================================================
# RESUMEN FINAL
# =============================================================================

print("\n\n" + "="*80)
print("RESUMEN FINAL")
print("="*80)
print(f"Prueba 1 (Equipos): {' EXITOSA' if orden_correcto else ' FALLÓ'}")
print(f"Prueba 2 (Sedes): {' EXITOSA' if orden_correcto_sedes else ' FALLÓ'}")
print(f"Prueba 3 (Deportistas): {' EXITOSA' if orden_correcto_deport else ' FALLÓ'}")

if orden_correcto and orden_correcto_sedes and orden_correcto_deport:
    print("\n ¡TODAS LAS PRUEBAS EXITOSAS!")
else:
    print("\n ALGUNAS PRUEBAS FALLARON")
