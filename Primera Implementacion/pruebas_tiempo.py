import time 
from pruebas import generacionPruebasCompleta
from Modelos import bucket_sort, counting_sort, counting_sortSimple, rendimientosExtremos, rendimientoEquipos, edadesExtremos, edadPromedioTotal, rendimientoPromedioTotal

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
    jugadores_base, lista_de_sedes = generacionPruebasCompleta(
        numeroDeportistas=n,
        minDeportistasEquipo=2,
        maxDeportistasEquipo=3,
        minDeportes=3,
        maxDeportes=6,
        numeroSedes=3,
    )
    return jugadores_base

def algoritmoOrdernarSedes(datos):
    for sede in datos:
        sede.calcularRendimientoPromedio()
    listasIdOrdenados = bucket_sort(datos, "rendimientoPromedio")
    for sede in reversed(listasIdOrdenados):
        listasIdOrdenadosEquipos = sede.obtenerListaOrdenadaPorRendimiento()
        for equipo in reversed(listasIdOrdenadosEquipos):
            equipo.obtenerListaOrdenadaPorRendimiento()

def algoritmoRanking(datos):
    datos = counting_sort(list(datos.values()),"rendimiento")
    ranking = []
    for jugadores in datos:
        ranking.append(jugadores.id)
    return ranking

def algoritmoRendimientosExtremos(datos):
    datos_list = counting_sort(list(datos.values()),"rendimiento")
    menor = (datos_list[0].id, datos_list[0].nombre, datos_list[0].rendimiento)
    mayor = (datos_list[-1].id, datos_list[-1].nombre, datos_list[-1].rendimiento)

def algoritmoRendimientoEquipos(datos):
    todos_los_equipos = []
    for sede in datos:
        todos_los_equipos.extend(sede.equipos)
    equipos_ordenados = bucket_sort(todos_los_equipos, "rendimientoPromedio")

def algoritmoEdadesExtremos(datos):
    datos_list = counting_sortSimple(list(datos.values()),"edad")

def algoritmoEdadPromedioTotal(datos):
    total = 0
    for jugador in datos.values():
        total += jugador.edad
    promedio = total / len(datos)

def algoritmoRendimientoPromedioTotal(datos):
    total = 0
    for jugador in datos.values():
        total += jugador.rendimiento
    promedio = total / len(datos)

def medir_tiempo(algoritmo, datos):
    inicio = time.perf_counter()
    algoritmo(datos)
    fin = time.perf_counter()
    return fin - inicio

tamanosCambiandoSedes = [(10,2,6,2,5,2),(100,5,12,4,7,4)]
tamanoJugadores = [5,10,20,40,60,100,120]

def correrPruebas(algoritmoName, generarDatosName, tamanosPruebasName):
    resultados = []
    for n in tamanosPruebasName:
        datosSedes = generarDatosName(n)
        t = medir_tiempo(algoritmoName, datosSedes)
        resultados.append(t)
    return resultados

print("Tiempos realizando el ordenamiento de las sedes en distintos tamaños")
print(correrPruebas(algoritmoOrdernarSedes, generarDatosSedes, tamanosCambiandoSedes))

print("\nTiempos realizando el ranking de todos los jugadores en distintos tamaños")
print(correrPruebas(algoritmoRanking, generarDatosJugadores, tamanoJugadores))

print("\nTiempos obteniendo rendimientos extremos de jugadores en distintos tamaños")
print(correrPruebas(algoritmoRendimientosExtremos, generarDatosJugadores, tamanoJugadores))

print("\nTiempos obteniendo equipos con rendimiento extremo en distintos tamaños")
print(correrPruebas(algoritmoRendimientoEquipos, generarDatosSedes, tamanosCambiandoSedes))

print("\nTiempos obteniendo edades extremas de jugadores en distintos tamaños")
print(correrPruebas(algoritmoEdadesExtremos, generarDatosJugadores, tamanoJugadores))

print("\nTiempos calculando edad promedio total en distintos tamaños")
print(correrPruebas(algoritmoEdadPromedioTotal, generarDatosJugadores, tamanoJugadores))

print("\nTiempos calculando rendimiento promedio total en distintos tamaños")
print(correrPruebas(algoritmoRendimientoPromedioTotal, generarDatosJugadores, tamanoJugadores))