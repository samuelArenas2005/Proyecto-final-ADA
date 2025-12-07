from Modelos import Deportista,Equipo, Sede,counting_sort,bucket_sort
from pruebas import generacionPruebasCompleta


# Ejemplo 1: Usar el método generacionPruebasCompleta para crear todo automáticamente
jugadores_base, lista_de_sedes = generacionPruebasCompleta(
    numeroDeportistas=10,          # Número de deportistas a generar
    minDeportistasEquipo=2,         # Mínimo de deportistas por equipo
    maxDeportistasEquipo=6,         # Máximo de deportistas por equipo
    minDeportes=2,                  # Mínimo de deportes por sede
    maxDeportes=5,                  # Máximo de deportes por sede
    numeroSedes=2                  # Número de sedes
)

print("\n" + "="*70)
print(f"{'ID':<5} {'Nombre':<30} {'Edad':<8} {'Rendimiento':<10}")
print("="*70)
for jugador in jugadores_base:
    deportista = jugadores_base[jugador]
    print(f"{jugador:<5} {deportista.nombre:<30} {deportista.edad:<8} {deportista.rendimiento:<10}")
print("="*70 + "\n")

# Calcular rendimientos y ordenar
for sede in lista_de_sedes:
    sede.calcularRendimientoPromedio()

listasIdOrdenados = bucket_sort(lista_de_sedes, "rendimientoPromedio")

print("=== RESULTADOS===\n")
for sede in reversed(listasIdOrdenados):
    print("Sede ", sede.nombre , ":\n")
    listasIdOrdenadosEquipos = sede.obtenerListaOrdenadaPorRendimiento()
    for equipo in reversed(listasIdOrdenadosEquipos):
        listasIdOrdenadosDeportistas = equipo.obtenerListaOrdenadaPorRendimiento()
        print("\t",equipo.deporte,": ", listasIdOrdenadosDeportistas, "\n")
