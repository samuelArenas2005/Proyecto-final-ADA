import random
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from PrimeraImplementacion.Models import (
    Deportista,Equipo, Sede
)

from TestValues import *


def generacionPruebasJugadoresBase(numeroDeportistas):
    jugadoresBase = {}
    for i in range(numeroDeportistas):
        nombre = random.choice(FIRST_NAMES)
        apellido = random.choice(LAST_NAMES)
        nombre_completo = f"{nombre} {apellido}"
        edadJugador = random.randint(17, 45)
        rendimientoJugador = distribucionNormalDeRendimiento()
        jugadoresBase[i+1] = Deportista((i+1), nombre_completo, edadJugador, rendimientoJugador)

    return jugadoresBase

def generacionPruebasSede(jugadoresBase, minDeportistasEquipo, maxDeportistasEquipo, 
                          minDeportes, maxDeportes, numeroSedes):
    
    lista_deportistas = list(jugadoresBase.values())
    lista_de_sedes = []
    indice_deportista = 0
    
    # Mezclar aleatoriamente la lista de SPORTMEN para una mejor distribución
    random.shuffle(lista_deportistas)
    
    # Crear cada sede
    for num_sede in range(numeroSedes):
        nombre_sede = SITES[num_sede % len(SITES)]  # Usar nombres disponibles cíclicamente
        
        # Decidir aleatoriamente cuántos SPORT tendrá esta sede
        numero_deportes = random.randint(minDeportes, maxDeportes)
        equipos_sede = []
        
        # Crear equipos para esta sede
        for num_equipo in range(numero_deportes):
            # Seleccionar deporte
            deporte = SPORT[num_equipo % len(SPORT)]
            
            # Decidir cuántos SPORTMEN en este equipo
            numero_deportistas_equipo = random.randint(minDeportistasEquipo, maxDeportistasEquipo)
            
            # Recolectar SPORTMEN para este equipo
            deportistas_equipo = []
            for _ in range(numero_deportistas_equipo):
                # Si se acaban los SPORTMEN, no agregar más (evitar duplicados)
                if indice_deportista >= len(lista_deportistas):
                    break
                
                deportistas_equipo.append(lista_deportistas[indice_deportista])
                indice_deportista += 1
            
            # Solo crear el equipo si tiene SPORTMEN
            if deportistas_equipo:
                # Crear equipo
                equipo = Equipo(deporte, deportistas_equipo)
                equipo.calcularRendimientoPromedio()
                equipos_sede.append(equipo)
        
        # Solo crear la sede si tiene equipos
        if equipos_sede:
            # Crear sede con sus equipos
            sede = Sede(nombre_sede, equipos_sede)
            sede.calcularRendimientoPromedio()
            lista_de_sedes.append(sede)
    
    return lista_de_sedes


def generacionPruebasCompleta(numeroDeportistas, minDeportistasEquipo, maxDeportistasEquipo,
                              minDeportes, maxDeportes, numeroSedes):
    
    # Generar SPORTMEN base
    jugadores_base = generacionPruebasJugadoresBase(numeroDeportistas)
    
    # Generar SITES con equipos distribuidos
    lista_de_sedes = generacionPruebasSede(
        jugadores_base,
        minDeportistasEquipo,
        maxDeportistasEquipo,
        minDeportes,
        maxDeportes,
        numeroSedes
    )
    
    return jugadores_base, lista_de_sedes


def distribucionNormalDeRendimiento():
    media = 50      
    desviacion = 20  

    valor = int(random.gauss(media, desviacion))

    valor = max(1, min(100, valor))
    
    return valor