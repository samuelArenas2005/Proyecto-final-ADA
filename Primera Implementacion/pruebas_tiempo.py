import time 
from pruebas import generacionPruebasCompleta
from Modelos import bucket_sort
from Modelos import counting_sort

def generarDatosSedes(n):
    jugadores_base, lista_de_sedes = generacionPruebasCompleta(
        numeroDeportistas=n[0],          # Número de deportistas a generar
        minDeportistasEquipo=n[1],         # Mínimo de deportistas por equipo
        maxDeportistasEquipo=n[2],         # Máximo de deportistas por equipo
        minDeportes=n[3],                  # Mínimo de deportes por sede
        maxDeportes=n[4],                  # Máximo de deportes por sede
        numeroSedes=n[5],                 # Número de sedes
    )
    
    return lista_de_sedes

def generarDatosJugadores(n):
    jugadores_base, lista_de_sedes = generacionPruebasCompleta(
        numeroDeportistas=n,          # Número de deportistas a generar
        minDeportistasEquipo=2,         # Mínimo de deportistas por equipo
        maxDeportistasEquipo=3,         # Máximo de deportistas por equipo
        minDeportes=3,                  # Mínimo de deportes por sede
        maxDeportes=6,                  # Máximo de deportes por sede
        numeroSedes=3,                 # Número de sedes
    )
    
    return jugadores_base


def algoritmoOrdernarSedes(datos):
    # Calcular rendimientos y ordenar
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

def medir_tiempo(algoritmo,datos):
    inicio = time.perf_counter()
    algoritmo(datos)
    fin = time.perf_counter()
    return fin - inicio

tamanosCambiandoSedes = [(10,2,6,2,5,2),(100,5,12,4,7,4)]
tamanosCambiandoEquipos = []
tamanosCambiandoJugadores = []

tamanoJugadores = [5,10,20,40,60,100,120]



def correrPruebas(algoritmoName,generarDatosName,tamanosPruebasName):
    resultados = []
    for n in tamanosPruebasName:
        datosSedes = generarDatosName(n)
        t = medir_tiempo(algoritmoName,datosSedes)
        resultados.append(t)
        
    return resultados

print("Tiempos realizando el ordenamiento de las sedes en distintos tamaños")
print(correrPruebas(algoritmoOrdernarSedes,generarDatosSedes,tamanosCambiandoSedes))
print("Tiempos realizando el ranking de los todos los jugadores en distintos tamaños")
print(correrPruebas(algoritmoRanking,generarDatosJugadores,tamanoJugadores))
