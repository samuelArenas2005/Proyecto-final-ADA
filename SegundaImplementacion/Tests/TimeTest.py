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

def preparar_datos_prueba(n, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede):
    """Genera jugadores y calcula número de sedes necesarias"""
    jugadores = generacionPruebasJugadoresBase(n)
    promedio_jug_equipo = (min_jug_equipo + max_jug_equipo) / 2
    promedio_eq_sede = (min_eq_sede + max_eq_sede) / 2
    num_sedes = int(n / (promedio_jug_equipo * promedio_eq_sede) * 1.1) + 1
    return jugadores, num_sedes

def pruebaOrganizarEstructuraDeDatos(n, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede):
    jugadores, num_sedes = preparar_datos_prueba(n, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede)
    
    def prueba():
        lista_sedes = generacionPruebasSede(jugadores, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede, num_sedes)
        lista_sedes.get_structure_by_performance(show=False)
    
    return medir_tiempo(prueba)

def pruebaRankingGlobal(n, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede):
    jugadores, num_sedes = preparar_datos_prueba(n, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede)
    lista_sedes = generacionPruebasSede(jugadores, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede, num_sedes)
    
    def prueba():
        lista_sedes.get_global_ranking(show=False)
    
    return medir_tiempo(prueba)

def pruebaEdadesExtremas(n, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede):
    jugadores, num_sedes = preparar_datos_prueba(n, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede)
    lista_sedes = generacionPruebasSede(jugadores, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede, num_sedes)
    
    def prueba():
        lista_sedes.get_youngest_player_across_Sites()
    
    return medir_tiempo(prueba)

def pruebaEdadPromedio(n, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede):
    jugadores, num_sedes = preparar_datos_prueba(n, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede)
    lista_sedes = generacionPruebasSede(jugadores, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede, num_sedes)
    
    def prueba():
        lista_sedes.get_average_age_across_Sites()
    
    return medir_tiempo(prueba)

def pruebaRendimientoPromedio(n, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede):
    jugadores, num_sedes = preparar_datos_prueba(n, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede)
    lista_sedes = generacionPruebasSede(jugadores, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede, num_sedes)
    
    def prueba():
        lista_sedes.get_average_performance_across_Sites()
    
    return medir_tiempo(prueba)

def pruebaEquiposExtremos(n, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede):
    jugadores, num_sedes = preparar_datos_prueba(n, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede)
    lista_sedes = generacionPruebasSede(jugadores, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede, num_sedes)
    
    def prueba():
        lista_sedes.get_best_team_across_Sites()
    
    return medir_tiempo(prueba)

def pruebaJugadoresExtremos(n, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede):
    jugadores, num_sedes = preparar_datos_prueba(n, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede)
    lista_sedes = generacionPruebasSede(jugadores, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede, num_sedes)
    
    def prueba():
        lista_sedes.get_best_player_across_Sites()
    
    return medir_tiempo(prueba)

def ejecutar_bateria_de_pruebas(funcion_prueba, cantidades_jugadores, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede):
    """Ejecuta una batería de pruebas y retorna lista de tiempos"""
    tiempos = []
    for n in cantidades_jugadores:
        tiempo = funcion_prueba(n, min_jug_equipo, max_jug_equipo, min_eq_sede, max_eq_sede)
        tiempos.append(tiempo)
    return tiempos

# Configuración de las pruebas
CANTIDADES_JUGADORES = [100, 1000, 2000, 5000, 100000, 200000, 400000, 500000]

def graficar_resultados(cantidades, tiempos, titulo, color='blue'):
    """Genera gráfico de tiempos vs cantidad de jugadores"""
    plt.figure(figsize=(10, 6))
    plt.plot(cantidades, tiempos, 'o-', label='Tiempo Real', color=color)
    plt.xlabel('Cantidad de jugadores')
    plt.ylabel('Tiempo (segundos)')
    plt.title(titulo)
    plt.legend()
    plt.grid(True)
    plt.show()

#---------------PRUEBAS DISPONIBLES----------------------
# 1 - Organizar estructura de datos (ordenar sedes y equipos por rendimiento)
# 2 - Ranking global de jugadores
# 3 - Edades extremas (usa el más joven)
# 4 - Edad promedio
# 5 - Rendimiento promedio
# 6 - Equipos extremos (usa el mejor)
# 7 - Jugadores extremos (usa el mejor)

def prueba_organizar_estructura():
    """Prueba 1: Organizar estructura de datos"""
    print("\n=== Prueba 1: Organizar Estructura de Datos ===")
    tiempos = ejecutar_bateria_de_pruebas(pruebaOrganizarEstructuraDeDatos, CANTIDADES_JUGADORES, 10, 100, 10, 100)
    print("Tiempos:", tiempos)
    graficar_resultados(CANTIDADES_JUGADORES, tiempos, 'Organizar Estructura de Datos', 'green')
    return tiempos

def prueba_ranking_global():
    """Prueba 2: Ranking global de jugadores"""
    print("\n=== Prueba 2: Ranking Global de Jugadores ===")
    tiempos = ejecutar_bateria_de_pruebas(pruebaRankingGlobal, CANTIDADES_JUGADORES, 10, 100, 10, 100)
    print("Tiempos:", tiempos)
    graficar_resultados(CANTIDADES_JUGADORES, tiempos, 'Ranking Global de Jugadores', 'blue')
    return tiempos

def prueba_edades_extremas():
    """Prueba 3: Edades extremas (usa el caso del jugador más joven)"""
    print("\n=== Prueba 3: Edades Extremas ===")
    tiempos = ejecutar_bateria_de_pruebas(pruebaEdadesExtremas, CANTIDADES_JUGADORES, 10, 100, 10, 100)
    print("Tiempos:", tiempos)
    graficar_resultados(CANTIDADES_JUGADORES, tiempos, 'Consulta: Edades Extremas (Más Joven)', 'orange')
    return tiempos

def prueba_edad_promedio():
    """Prueba 4: Edad promedio"""
    print("\n=== Prueba 4: Edad Promedio ===")
    tiempos = ejecutar_bateria_de_pruebas(pruebaEdadPromedio, CANTIDADES_JUGADORES, 10, 100, 10, 100)
    print("Tiempos:", tiempos)
    graficar_resultados(CANTIDADES_JUGADORES, tiempos, 'Consulta: Edad Promedio', 'red')
    return tiempos

def prueba_rendimiento_promedio():
    """Prueba 5: Rendimiento promedio"""
    print("\n=== Prueba 5: Rendimiento Promedio ===")
    tiempos = ejecutar_bateria_de_pruebas(pruebaRendimientoPromedio, CANTIDADES_JUGADORES, 10, 100, 10, 100)
    print("Tiempos:", tiempos)
    graficar_resultados(CANTIDADES_JUGADORES, tiempos, 'Consulta: Rendimiento Promedio', 'cyan')
    return tiempos

def prueba_equipos_extremos():
    """Prueba 6: Equipos extremos (usa el caso del mejor equipo)"""
    print("\n=== Prueba 6: Equipos Extremos ===")
    tiempos = ejecutar_bateria_de_pruebas(pruebaEquiposExtremos, CANTIDADES_JUGADORES, 10, 100, 10, 100)
    print("Tiempos:", tiempos)
    graficar_resultados(CANTIDADES_JUGADORES, tiempos, 'Consulta: Equipos Extremos (Mejor)', 'magenta')
    return tiempos

def prueba_jugadores_extremos():
    """Prueba 7: Jugadores extremos (usa el caso del mejor jugador)"""
    print("\n=== Prueba 7: Jugadores Extremos ===")
    tiempos = ejecutar_bateria_de_pruebas(pruebaJugadoresExtremos, CANTIDADES_JUGADORES, 10, 100, 10, 100)
    print("Tiempos:", tiempos)
    graficar_resultados(CANTIDADES_JUGADORES, tiempos, 'Consulta: Jugadores Extremos (Mejor)', 'lime')
    return tiempos

def run_prueba(numero):
    """Ejecuta la prueba indicada por número"""
    if numero == 1:
        prueba_organizar_estructura()
    elif numero == 2:
        prueba_ranking_global()
    elif numero == 3:
        prueba_edades_extremas()
    elif numero == 4:
        prueba_edad_promedio()
    elif numero == 5:
        prueba_rendimiento_promedio()
    elif numero == 6:
        prueba_equipos_extremos()
    elif numero == 7:
        prueba_jugadores_extremos()
    else:
        print(f"Prueba {numero} no definida. Revisa la tabla de pruebas disponibles.")

run_prueba(2)