import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from PrimeraImplementacion.Models import (
    ranckingSedes,ranking, rendimientosExtremos, rendimientoEquipos, 
    edadesExtremos, rendimientoPromedioTotal, edadPromedioTotal,
    mostrarDeportistas
)

from TestGenerate import generacionPruebasCompleta


# Ejemplo 1: Usar el método generacionPruebasCompleta para crear todo automáticamente
jugadores_base, lista_de_sedes = generacionPruebasCompleta(
    numeroDeportistas=10,          # Número de deportistas a generar
    minDeportistasEquipo=2,         # Mínimo de deportistas por equipo
    maxDeportistasEquipo=6,         # Máximo de deportistas por equipo
    minDeportes=2,                  # Mínimo de deportes por sede
    maxDeportes=5,                  # Máximo de deportes por sede
    numeroSedes=2                  # Número de sedes
)

# Mostrar deportistas
lines = mostrarDeportistas(jugadores_base)
for line in lines:
    print(line)

# Resultados por sede/equipo
resultados_sedes = ranckingSedes(lista_de_sedes)
print("=== RESULTADOS===")
for item_sede in resultados_sedes:
    sede = item_sede['sede']
    print(f"Sede {sede.nombre}:")
    for item_equipo in item_sede['equipos']:
        equipo = item_equipo['equipo']
        deportistas = item_equipo['deportistas']
        print(f"\t{equipo.deporte}: {deportistas}")
    print()

# Ranking de jugadores
ranking_list = ranking(jugadores_base)
print("Ranking de jugadores por rendimiento", ranking_list)

print("\nConsultas Solicitadas:\n")

# Rendimientos extremos
menor, mayor = rendimientosExtremos(jugadores_base)
print("Jugador con menor rendimiento:", menor.id, menor.nombre, menor.rendimiento)
print("Jugador con mayor rendimiento:", mayor.id, mayor.nombre, mayor.rendimiento)

# Equipos extremos
equipo_menor, equipo_mayor = rendimientoEquipos(lista_de_sedes)
print(f"Equipo con MENOR rendimiento: {equipo_menor.deporte} - Sede: {equipo_menor.sede.nombre} (Rendimiento: {equipo_menor.rendimientoPromedio:.2f})")
print(f"Equipo con MAYOR rendimiento: {equipo_mayor.deporte} - Sede: {equipo_mayor.sede.nombre} (Rendimiento: {equipo_mayor.rendimientoPromedio:.2f})")

# Edades extremas
mas_joven, mas_viejo = edadesExtremos(jugadores_base)
print("Jugador más joven:", mas_joven.id, mas_joven.nombre, mas_joven.edad)
print("Jugador más veterano:", mas_viejo.id, mas_viejo.nombre, mas_viejo.edad)

# Promedios
prom_edad = edadPromedioTotal(jugadores_base)
prom_rend = rendimientoPromedioTotal(jugadores_base)
print(f"Edad promedio total de los deportistas: {prom_edad:.2f}")
print(f"Rendimiento promedio total de los deportistas: {prom_rend:.2f}")