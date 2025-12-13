import sys
from pathlib import Path
import time
import matplotlib.pyplot as plt
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from SegundaImplementacion.Models import List_of_Sites

from TestGenerate import (
    generacionPruebasJugadoresBase,
    generacionPruebasSede
)

def medir_tiempo(algoritmo): 
    inicio = time.perf_counter()
    algoritmo()
    fin = time.perf_counter()
    return fin - inicio

def pruebaOrganizarEstructuraDeDatos(n, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede):
    jugadores = generacionPruebasJugadoresBase(n)
    promedio_jug_equipo = (min_jug_equipo + max_jug_equipo) / 2
    promedio_eq_sede = (min_eq_sede + max_eq_sede) / 2
    num_sedes = int(n / (promedio_jug_equipo * promedio_eq_sede) * 1.1) + 1
    
    def prueba():
        lista_sedes = generacionPruebasSede(jugadores, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede, num_sedes)
        lista_sedes.get_structure_by_performance(show=False)
    
    return medir_tiempo(prueba)

def pruebaOrganizarEstructuraDeDatos2(n, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede):
    jugadores = generacionPruebasJugadoresBase(n)
    promedio_jug_equipo = (min_jug_equipo + max_jug_equipo) / 2
    promedio_eq_sede = (min_eq_sede + max_eq_sede) / 2
    num_sedes = int(n / (promedio_jug_equipo * promedio_eq_sede) * 1.1) + 1
    lista_sedes = generacionPruebasSede(jugadores, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede, num_sedes)
    def prueba():
        lista_sedes.get_global_ranking(show=False)
    
    return medir_tiempo(prueba)

def ejecutar_bateria_de_pruebas(cantidades_jugadores):
    tiempos = []
    for n in cantidades_jugadores:
        tiempo = pruebaOrganizarEstructuraDeDatos2(n, 10, 100, 10, 100)
        tiempos.append(tiempo)
    return tiempos

# Configuración de las pruebas
CANTIDADES_JUGADORES = [100, 1000, 2000, 5000, 100000, 200000, 400000, 500000]

if __name__ == "__main__":
    tiempos = ejecutar_bateria_de_pruebas(CANTIDADES_JUGADORES)
    print(tiempos)