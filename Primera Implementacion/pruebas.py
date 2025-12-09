import random
from Modelos import Deportista,Equipo, Sede
from valoresPruebas import DEPORTISTAS,DEPORTES,SEDES


def generacionPruebasJugadoresBase(numeroDeportistas):
    jugadoresBase = {}
    NombreDeportistas = DEPORTISTAS.copy()
    
    for i in range(numeroDeportistas):
        posicionJugador = random.randint(0, len(NombreDeportistas) - 1)
        edadJugador = random.randint(17, 45)
        rendimientoJugador = distribucionNormalDeRendimiento()
        jugadoresBase[i+1] = Deportista((i+1), NombreDeportistas[posicionJugador], edadJugador, rendimientoJugador)
        NombreDeportistas.pop(posicionJugador)
    
    return jugadoresBase

def generacionPruebasSede(jugadoresBase, minDeportistasEquipo, maxDeportistasEquipo, 
                          minDeportes, maxDeportes, numeroSedes):
    
    lista_deportistas = list(jugadoresBase.values())
    lista_de_sedes = []
    indice_deportista = 0
    
    # Mezclar aleatoriamente la lista de deportistas para una mejor distribución
    random.shuffle(lista_deportistas)
    
    # Crear cada sede
    for num_sede in range(numeroSedes):
        nombre_sede = SEDES[num_sede % len(SEDES)]  # Usar nombres disponibles cíclicamente
        
        # Decidir aleatoriamente cuántos deportes tendrá esta sede
        numero_deportes = random.randint(minDeportes, maxDeportes)
        equipos_sede = []
        
        # Crear equipos para esta sede
        for num_equipo in range(numero_deportes):
            # Seleccionar deporte
            deporte = DEPORTES[num_equipo % len(DEPORTES)]
            
            # Decidir cuántos deportistas en este equipo
            numero_deportistas_equipo = random.randint(minDeportistasEquipo, maxDeportistasEquipo)
            
            # Recolectar deportistas para este equipo
            deportistas_equipo = []
            for _ in range(numero_deportistas_equipo):
                # Si se acaban los deportistas, no agregar más (evitar duplicados)
                if indice_deportista >= len(lista_deportistas):
                    break
                
                deportistas_equipo.append(lista_deportistas[indice_deportista])
                indice_deportista += 1
            
            # Solo crear el equipo si tiene deportistas
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
    
    # Generar deportistas base
    jugadores_base = generacionPruebasJugadoresBase(numeroDeportistas)
    
    # Generar sedes con equipos distribuidos
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