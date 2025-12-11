import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from PrimeraImplementacion.Models import (
    ranckingSedes,ranking, rendimientosExtremos, rendimientoEquipos, edadesExtremos, rendimientoPromedioTotal, edadPromedioTotal
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

print("\n" + "="*70)
print(f"{'ID':<5} {'Nombre':<30} {'Edad':<8} {'Rendimiento':<10}")
print("="*70)
for jugador in jugadores_base:
    deportista = jugadores_base[jugador]
    print(f"{jugador:<5} {deportista.nombre:<30} {deportista.edad:<8} {deportista.rendimiento:<10}")
print("="*70 + "\n")


ranckingSedes(lista_de_sedes)
ranking(jugadores_base)

print("\nConsultas Solicitadas:\n")
rendimientosExtremos(jugadores_base)
rendimientoEquipos(lista_de_sedes)
edadesExtremos(jugadores_base)
edadPromedioTotal(jugadores_base)
rendimientoPromedioTotal(jugadores_base)