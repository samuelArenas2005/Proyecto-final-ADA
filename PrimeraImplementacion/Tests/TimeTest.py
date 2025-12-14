import sys
from pathlib import Path
import time
import matplotlib.pyplot as plt
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from PrimeraImplementacion.Models import (
    ranckingSedes, ranking, rendimientosExtremos, rendimientoEquipos, 
    edadesExtremos, edadPromedioTotal, rendimientoPromedioTotal
)
from TestGenerate import generacionPruebasCompleta


def generarDatosSedes(n):
    jugadores_base, lista_de_sedes = generacionPruebasCompleta(
        numeroDeportistas=n[0],
        minDeportistasEquipo=n[1],
        maxDeportistasEquipo=n[2],
        minDeportes=n[3],
        maxDeportes=n[4],
        numeroSedes=n[5],
    )
    return lista_de_sedes


def generarDatosJugadores(n):
    jugadores_base, lista_de_sedes= generacionPruebasCompleta(
        numeroDeportistas=n,
        minDeportistasEquipo=2,
        maxDeportistasEquipo=3,
        minDeportes=3,
        maxDeportes=6,
        numeroSedes=3,
    )
    return jugadores_base


def algoritmoOrdernarSedes(datos):
    ranckingSedes(datos)


def algoritmoRanking(datos):
    ranking(datos)


def algoritmoRendimientosExtremos(datos):
    rendimientosExtremos(datos)


def algoritmoRendimientoEquipos(datos):
    rendimientoEquipos(datos)


def algoritmoEdadesExtremos(datos):
    edadesExtremos(datos)


def algoritmoEdadPromedioTotal(datos):
    edadPromedioTotal(datos)


def algoritmoRendimientoPromedioTotal(datos):
    rendimientoPromedioTotal(datos)


def medir_tiempo(algoritmo, datos): 
    inicio = time.perf_counter()
    algoritmo(datos)
    fin = time.perf_counter()
    
    return (fin - inicio)


tamanosCambiandoSedes = [(50000, 10, 20, 10, 30, 100), (50000, 2, 6, 2, 4, 500),(50000, 2, 6, 2, 4, 800), (50000, 2, 6, 2, 4, 1000), (50000, 2, 6, 2, 4, 1400),(50000, 2, 6, 2, 4, 1800)]
referenciaCambioSedes = [100,500,800,1000,1400,1800]

tamanosCambiandoEquipos = [(50000, 2, 6, 2, 4, 10), (50000, 2, 6, 5, 10, 10), (50000, 2, 6, 10, 20, 10), (50000, 2, 6, 15, 30, 10), (50000, 2, 6, 20, 40, 10), (50000, 2, 6, 25, 50, 10)]
referenciaCambioEquipos = [4, 10, 20, 30, 40, 50]

tamanosCambiandoJugadores = [(100, 2, 6, 2, 4, 5), (1000, 2, 10, 2, 10, 10), (5000, 2, 30, 2, 40, 10), (100000, 2, 450, 2, 40, 10), (200000, 2, 250, 2, 100, 10), (500000, 2, 300, 2, 100, 20)]
referenciaCambioJugadores = [100, 1000, 5000, 100000, 200000, 500000]

tamanoJugadores = [100,1000,2000,5000,100000,200000,400000,500000]


def correrPruebas(algoritmoName, generarDatosName, tamanosPruebasName):
    resultados = []
    for n in tamanosPruebasName:
        datosSedes = generarDatosName(n)
        t = medir_tiempo(algoritmoName, datosSedes)
        resultados.append(t)
    return resultados


#---GRAFICA DE ANALISIS------
def graficaComparativa(tamanos, resultados, teorica, color_real='green', color_teorica='red'):
    plt.figure(figsize=(10, 6))
    # Gráfica Real
    plt.plot(tamanos, resultados, 'o-', label='Tiempo Real Promedio', color=color_real)
    # Gráfica Teórica (Ajustada a la escala de milisegundos)
    plt.plot(tamanos, teorica, '--', label='Proyección Teorica', color=color_teorica)
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Complejidad: Real vs Proyección Lineal')
    plt.legend()
    plt.grid(True)
    plt.show()


K1 = 0.01
K2 = 0.00000005
K3 = 0.0000005
K4 = 0.0001


#---------------PRUEBAS REALIZADAS (definidas como funciones)----------------------

# Tabla de pruebas (asignar un número para ejecutar con `run_prueba(numero)`):
# 1 - Ordenamiento sedes (variando número de sedes)
# 2 - Ordenamiento sedes (variando número de equipos)
# 3 - Ordenamiento sedes (variando número de jugadores)
# 4 - Ranking jugadores (orden total)
# 5 - Rendimientos extremos (jugadores)
# 6 - Edades extremas (jugadores)
# 7 - Edad promedio total (jugadores)
# 8 - Rendimiento promedio total (jugadores)
# 9 - Rendimiento equipos (sedes)


def prueba_ordenar_sedes(color_real='green', color_teorica='red'):
    resultados = correrPruebas(algoritmoOrdernarSedes, generarDatosSedes, tamanosCambiandoSedes)
    teorica = [K1 * n for n in referenciaCambioSedes]
    print("Tiempos realizando el ordenamiento de las sedes en distintos tamaños de sedes")
    print(resultados)
    graficaComparativa(referenciaCambioSedes, resultados, teorica, color_real, color_teorica)


def prueba_ordenar_equipos(color_real='blue', color_teorica='orange'):
    resultados = correrPruebas(algoritmoOrdernarSedes, generarDatosSedes, tamanosCambiandoEquipos)
    teorica = [K1 * n for n in referenciaCambioEquipos]
    print("\nTiempos realizando el ordenamiento de las sedes en distintos números de equipos")
    print(resultados)
    graficaComparativa(referenciaCambioEquipos, resultados, teorica, color_real, color_teorica)


def prueba_ordenar_jugadores(color_real='purple', color_teorica='gray'):
    resultados = correrPruebas(algoritmoOrdernarSedes, generarDatosSedes, tamanosCambiandoJugadores)
    teorica = [K4 * n for n in referenciaCambioJugadores]
    print("\nTiempos realizando el ordenamiento de las sedes en distintos números de jugadores")
    print(resultados)
    graficaComparativa(referenciaCambioJugadores, resultados, teorica, color_real, color_teorica)


def prueba_ranking_jugadores(color_real='green', color_teorica='red'):
    resultados = correrPruebas(algoritmoRanking, generarDatosJugadores, tamanoJugadores)
    teorica = [ K3* n for n in tamanoJugadores]
    print("\nTiempos realizando el ranking de todos los jugadores en distintos tamaños")
    print(resultados)
    graficaComparativa(tamanoJugadores, resultados, teorica, color_real, color_teorica)


def prueba_rendimientos_extremos(color_real='blue', color_teorica='red'):
    resultados = correrPruebas(algoritmoRendimientosExtremos, generarDatosJugadores, tamanoJugadores)
    teorica = [K3 * n for n in tamanoJugadores]
    print("\nTiempos rendimientos extremos (jugadores)")
    print(resultados)
    graficaComparativa(tamanoJugadores, resultados, teorica, color_real, color_teorica)


def prueba_edades_extremas(color_real='blue', color_teorica='red'):
    resultados = correrPruebas(algoritmoEdadesExtremos, generarDatosJugadores, tamanoJugadores)
    teorica = [K3 * n for n in tamanoJugadores]
    print("\nTiempos edades extremas (jugadores)")
    print(resultados)
    graficaComparativa(tamanoJugadores, resultados, teorica, color_real, color_teorica)


def prueba_edad_promedio(color_real='blue', color_teorica='green'):
    resultados = correrPruebas(algoritmoEdadPromedioTotal, generarDatosJugadores, tamanoJugadores)
    teorica = [K2 * n for n in tamanoJugadores]
    print("\nTiempos edad promedio total (jugadores)")
    print(resultados)
    graficaComparativa(tamanoJugadores, resultados, teorica, color_real, color_teorica)


def prueba_rendimiento_promedio(color_real='orange', color_teorica='blue'):
    resultados = correrPruebas(algoritmoRendimientoPromedioTotal, generarDatosJugadores, tamanoJugadores)
    teorica = [K2 * n for n in tamanoJugadores]
    print("\nTiempos rendimiento promedio total (jugadores)")
    print(resultados)
    graficaComparativa(tamanoJugadores, resultados, teorica, color_real, color_teorica)


def prueba_rendimiento_equipos(color_real='blue', color_teorica='red'):
    resultados = correrPruebas(algoritmoRendimientoEquipos, generarDatosSedes, tamanosCambiandoSedes)
    teorica = [K4 * n for n in referenciaCambioSedes]
    print("\nTiempos rendimiento equipos (sedes)")
    print(resultados)
    graficaComparativa(referenciaCambioSedes, resultados, teorica, color_real, color_teorica)


def run_prueba(numero):
    """Ejecuta la prueba indicada por `numero`.
    """
    if numero == 1:
        prueba_ordenar_sedes()
    elif numero == 2:
        prueba_ordenar_equipos()
    elif numero == 3:
        prueba_ordenar_jugadores()
    elif numero == 4:
        prueba_ranking_jugadores()
    elif numero == 5:
        prueba_rendimientos_extremos()
    elif numero == 6:
        prueba_edades_extremas()
    elif numero == 7:
        prueba_edad_promedio()
    elif numero == 8:
        prueba_rendimiento_promedio()
    elif numero == 9:
        prueba_rendimiento_equipos()
    else:
        print(f"Prueba {numero} no definida. Revisa la tabla de mapeo en el archivo.")



run_prueba(3)
