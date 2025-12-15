import sys
from pathlib import Path
import time
import matplotlib.pyplot as plt
import math
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from SegundaImplementacion.Models import List_of_Sites
from TestGenerate import (
    generacionPruebasJugadoresBase,
    generacionPruebasSede
)

# =============================================================================
# SECCIÓN 1: CONFIGURACIÓN DE VARIABLES DE PRUEBA
# =============================================================================
# Esta sección es el "Panel de Control" de tus experimentos.
# Aquí defines los escenarios exactos que se van a simular.
#
# FORMATO DE LA TUPLA DE CONFIGURACIÓN:
# (
#   0: Total de Jugadores (N),
#   1: Mínimo de jugadores por equipo,
#   2: Máximo de jugadores por equipo,
#   3: Mínimo de equipos por sede,
#   4: Máximo de equipos por sede,
#   5: Total de Sedes (K)
# )
# =============================================================================

# --- ESCENARIO A: PRUEBA DE ESTRÉS POR CANTIDAD DE SEDES ---
# OBJETIVO: Evaluar cómo se comporta el sistema cuando N (50,000) es constante,
# pero se distribuye en muchas sedes pequeñas vs pocas sedes grandes.
#
# QUÉ MODIFICAR:
# - Mantén el primer número (50000) fijo.
# - Cambia el ÚLTIMO número (10, 50, 100...) para variar las sedes.
# - Ajusta los rangos de equipos (posiciones 3 y 4) para que los datos quepan.
tamanosCambiandoSedes = [
    # (Total, MinJug, MaxJug, MinEq, MaxEq, SEDES)
    (50000, 10, 20, 10, 30, 10), 
    (50000, 10, 20, 10, 30, 50),
    (50000, 5, 15, 5, 15, 100),
    (50000, 4, 10, 4, 10, 500),
    (50000, 4, 6, 8, 12, 1000) 
]
# Eje X de la gráfica para este escenario:
referenciaCambioSedes = [10, 50, 100, 500, 1000]

# --- ESCENARIO B: PRUEBA DE DENSIDAD DE EQUIPOS ---
# OBJETIVO: Evaluar si tener sedes con MUCHOS equipos afecta el rendimiento.
#
# QUÉ MODIFICAR:
# - Mantén Jugadores (50000) y Sedes (50) fijos.
# - Aumenta progresivamente los valores de EQUIPOS POR SEDE (posiciones 3 y 4).
#   Ejemplo: De (2, 5) pasa a (80, 100).
tamanosCambiandoEquipos = [
    (50000, 10, 20, 2, 5, 50),
    (50000, 10, 20, 10, 20, 50),
    (50000, 10, 20, 30, 40, 50),
    (50000, 10, 20, 50, 60, 50),
    (50000, 10, 20, 80, 100, 50)
]
# Eje X de la gráfica (Promedio de equipos):
referenciaCambioEquipos = [3, 15, 35, 55, 90]

# --- ESCENARIO C: PRUEBA DE CRECIMIENTO DE JUGADORES (N) ---
# OBJETIVO: La prueba clásica de complejidad asintótica (O(N) o O(N log N)).
# Ver cómo escala el tiempo al aumentar masivamente los datos.
#
# QUÉ MODIFICAR:
# - Aumenta el PRIMER número (Total Jugadores) exponencialmente (100 -> 200,000).
# - Aumenta proporcionalmente el número de sedes (último número) para evitar
#   que una sola sede colapse con demasiados datos.
tamanosCambiandoJugadores = [
    (100, 2, 5, 2, 4, 2),
    (1000, 5, 10, 2, 5, 5),
    (5000, 10, 20, 5, 10, 10),
    (10000, 10, 30, 5, 10, 15),
    (50000, 15, 40, 10, 20, 20),
    (100000, 20, 50, 10, 20, 30),
    (200000, 20, 50, 15, 25, 40)
]
# Eje X de la gráfica (Cantidad de Jugadores):
referenciaCambioJugadores = [100, 1000, 5000, 10000, 50000, 100000, 200000]


# =============================================================================
# SECCIÓN 2: MOTORES DE MEDICIÓN
# =============================================================================

def medir_tiempo(algoritmo): 
    """Cronómetro de alta precisión que ejecuta la función recibida."""
    inicio = time.perf_counter()
    algoritmo()
    fin = time.perf_counter()
    return fin - inicio

def preparar_datos_con_tupla(params):
    """
    Traduce la tupla de configuración en estructuras de datos reales.
    Utiliza los generadores aleatorios definidos en TestGenerate.py.
    """
    n, min_j, max_j, min_eq, max_eq, num_sedes = params
    jugadores = generacionPruebasJugadoresBase(n)
    lista_sedes = generacionPruebasSede(jugadores, min_j, max_j, min_eq, max_eq, num_sedes)
    return lista_sedes


# =============================================================================
# SECCIÓN 3: ENVOLTORIOS DE PRUEBAS (WRAPPERS)
# =============================================================================
# Estas funciones aíslan la generación de datos de la medición del algoritmo.
# 1. Primero crean los datos (preparar_datos_con_tupla) SIN medir tiempo.
# 2. Luego definen una función interna 'prueba' que solo ejecuta el algoritmo.
# 3. Finalmente cronometran solo la función interna.

def pruebaOrganizarEstructuraDeDatos(params):
    lista_sedes = preparar_datos_con_tupla(params)
    
    def prueba():
        # Algoritmo a medir: Ordenamiento interno de Sedes y Equipos
        lista_sedes.get_structure_by_performance(show=False)
    
    return medir_tiempo(prueba)

def pruebaRankingGlobal(params):
    lista_sedes = preparar_datos_con_tupla(params)
    
    def prueba():
        # Algoritmo a medir: Ranking Global (Merge Sort N log N)
        lista_sedes.get_global_ranking(show=False)
    
    return medir_tiempo(prueba)

def pruebaEdadesExtremas(params):
    lista_sedes = preparar_datos_con_tupla(params)
    def prueba():
        # Algoritmo a medir: Búsqueda del más joven (Lineal o Logarítmica)
        lista_sedes.get_youngest_player_across_Sites()
    return medir_tiempo(prueba)

def pruebaEdadPromedio(params):
    lista_sedes = preparar_datos_con_tupla(params)
    def prueba():
        # Algoritmo a medir: Promedio (Recorrido Lineal O(N))
        lista_sedes.get_average_age_across_Sites()
    return medir_tiempo(prueba)

def pruebaRendimientoPromedio(params):
    lista_sedes = preparar_datos_con_tupla(params)
    def prueba():
        lista_sedes.get_average_performance_across_Sites()
    return medir_tiempo(prueba)

def pruebaEquiposExtremos(params):
    lista_sedes = preparar_datos_con_tupla(params)
    def prueba():
        lista_sedes.get_best_team_across_Sites()
    return medir_tiempo(prueba)

def pruebaJugadoresExtremos(params):
    lista_sedes = preparar_datos_con_tupla(params)
    def prueba():
        lista_sedes.get_best_player_across_Sites()
    return medir_tiempo(prueba)


# =============================================================================
# SECCIÓN 4: EJECUCIÓN Y VISUALIZACIÓN
# =============================================================================

def ejecutar_bateria_de_pruebas(funcion_prueba, lista_tuplas):
    """Itera sobre la lista de escenarios y guarda los tiempos reales."""
    tiempos = []
    print(f"Iniciando pruebas ({len(lista_tuplas)} escenarios)...")
    for params in lista_tuplas:
        tiempo = funcion_prueba(params)
        tiempos.append(tiempo)
        print(f"  -> Escenario completado: {tiempo:.5f} s")
    return tiempos

def graficar_resultados(eje_x, tiempos_reales, tiempos_teoricos, titulo, label_x):
    """
    Genera la gráfica comparativa.
    - Azul: Tiempo Real medido por tu PC.
    - Roja (Punteada): Proyección matemática ideal.
    """
    plt.figure(figsize=(10, 6))
    
    plt.plot(eje_x, tiempos_reales, 'o-', label='Tiempo Real', color='blue')
    
    if tiempos_teoricos:
        plt.plot(eje_x, tiempos_teoricos, '--', label='Complejidad Teórica', color='red')
    
    plt.xlabel(label_x)
    plt.ylabel('Tiempo (segundos)')
    plt.title(titulo)
    plt.legend()
    plt.grid(True)
    plt.show()

# CONSTANTES DE CALIBRACIÓN (K)
# Estas variables ajustan la altura de la curva teórica (roja) para que
# coincida visualmente con la curva real (azul). Dependen de la velocidad de tu CPU.
# Si la línea roja sale muy arriba o muy abajo, modifica estos valores.
K_NLOGN = 0.00000008  # Para algoritmos O(N log N)
K_N = 0.0000005       # Para algoritmos Lineales O(N)
K_SEDES = 0.00002      # Para algoritmos dependientes de Sedes
K_EQUIPOS = 0.0001    # Para algoritmos dependientes de Equipos

def run_prueba(numero):
    """
    SELECTOR PRINCIPAL DE PRUEBAS
    Cambia el número en 'if __name__ == "__main__":' para ejecutar:
    
    1: RANKING GLOBAL (Variable N)
       - Prueba la complejidad N log N.
       - Usa la lista 'tamanosCambiandoJugadores'.
       
    2: CONSULTAS LINEALES (Variable N)
       - Prueba cálculos de promedios O(N).
       - Usa la lista 'tamanosCambiandoJugadores'.
       
    3: ESTRUCTURA VS SEDES (Variable K)
       - Prueba el impacto de tener muchas Sedes.
       - Usa la lista 'tamanosCambiandoSedes'.
       
    4: BÚSQUEDA EXTREMA (Variable N)
       - Busca el mejor/peor jugador.
       - Usa la lista 'tamanosCambiandoJugadores'.
       
    5: ESTRUCTURA VS EQUIPOS (Variable M)
       - Prueba el impacto de tener sedes muy densas (muchos equipos).
       - Usa la lista 'tamanosCambiandoEquipos'.
    """
    
    if numero == 1:
        print("\n=== Prueba 1: Ranking Global (Teórica: N log N) ===")
        tiempos = ejecutar_bateria_de_pruebas(pruebaRankingGlobal, tamanosCambiandoJugadores)
        teorica = [K_NLOGN * n * math.log2(n) for n in referenciaCambioJugadores]
        graficar_resultados(referenciaCambioJugadores, tiempos, teorica, 
                            'Ranking Global vs N', 'Cantidad de Jugadores')

    elif numero == 2:
        print("\n=== Prueba 2: Consultas Lineales (Teórica: O(n)) ===")
        tiempos = ejecutar_bateria_de_pruebas(pruebaEdadPromedio, tamanosCambiandoJugadores)
        teorica = [K_N * n for n in referenciaCambioJugadores]
        graficar_resultados(referenciaCambioJugadores, tiempos, teorica, 
                            'Consulta Promedio vs N', 'Cantidad de Jugadores')

    elif numero == 3:
        print("\n=== Prueba 3: Organizar Estructura vs Cantidad de Sedes ===")
        tiempos = ejecutar_bateria_de_pruebas(pruebaOrganizarEstructuraDeDatos, tamanosCambiandoSedes)
        teorica = [K_SEDES * k * math.log2(k) for k in referenciaCambioSedes]
        graficar_resultados(referenciaCambioSedes, tiempos, teorica, 
                            'Organizar Estructura vs Número de Sedes', 'Cantidad de Sedes')
        
    elif numero == 4:
        print("\n=== Prueba 4: Jugadores Extremos (Lineal) ===")
        tiempos = ejecutar_bateria_de_pruebas(pruebaJugadoresExtremos, tamanosCambiandoJugadores)
        teorica = [K_N * n for n in referenciaCambioJugadores]
        graficar_resultados(referenciaCambioJugadores, tiempos, teorica, 
                            'Jugador Extremo vs N', 'Cantidad de Jugadores')

    elif numero == 5:
        print("\n=== Prueba 5: Organizar Estructura vs Equipos por Sede ===")
        tiempos = ejecutar_bateria_de_pruebas(pruebaOrganizarEstructuraDeDatos, tamanosCambiandoEquipos)
        # Teórica aproximada: M * log(M)
        teorica = [K_EQUIPOS * m * (math.log2(m) if m > 0 else 1) for m in referenciaCambioEquipos]
        graficar_resultados(referenciaCambioEquipos, tiempos, teorica, 
                            'Organizar Estructura vs Equipos por Sede', 'Promedio Equipos por Sede')

    else:
        print("Opción no válida. Por favor elija un número del 1 al 5.")

# =============================================================================
# PUNTO DE ENTRADA
# =============================================================================
if __name__ == "__main__":
    # INSTRUCCIONES PARA EJECUTAR:
    # Cambia el número dentro de run_prueba() para seleccionar qué gráfica generar.
    # Ejemplo: run_prueba(1) generará la gráfica de N log N.
    
    run_prueba(3)