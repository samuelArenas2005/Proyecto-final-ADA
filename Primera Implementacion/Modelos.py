import math

def counting_sort(arr, criterionName):
    max_rendimiento = 100
    max_edad = 100
    
    count = [[[] for _ in range(max_edad + 1)] for _ in range(max_rendimiento + 1)]
    
    # Agrupar elementos por rendimiento y edad
    for elemento in arr:
        rendimiento = int(getattr(elemento, criterionName))
        edad = int(getattr(elemento, "edad"))
        
        count[rendimiento][edad].append(elemento)
    
    output = []
    # Ordenar ascendente por rendimiento, y dentro de cada rendimiento descendente por edad
    for rendimiento in range(max_rendimiento + 1):  
        for edad in range(max_edad, -1, -1):  # Descendente por edad
            output.extend(count[rendimiento][edad])
    
    return output

def counting_sortSimple(arr, criterionName):
    max_valor = 100
    
    count = [[] for _ in range(max_valor + 1)]
    
    # Agrupar elementos por el atributo especificado
    for elemento in arr:
        valor = int(getattr(elemento, criterionName))
        count[valor].append(elemento)
    
    output = []
    # Ordenar ascendente por el atributo
    for valor in range(max_valor + 1):  
        output.extend(count[valor])
    
    return output

def bucket_sort(arr,criterionName):
    NUM_CUBETAS = 10
    
    cubetas = [[] for _ in range(NUM_CUBETAS)]
    
    for elemento in arr:
        rendimiento = getattr(elemento, criterionName)
        if rendimiento == 100.0:
            indice_cubeta = NUM_CUBETAS - 1
        else:
            indice_cubeta = math.floor(rendimiento / (100.0 / NUM_CUBETAS))
            
        # Aseguramos que el índice esté dentro del rango [0, 9]
        indice_cubeta = min(indice_cubeta, NUM_CUBETAS - 1)
        
        cubetas[indice_cubeta].append(elemento)
        
    for i in range(NUM_CUBETAS):
        cubeta_actual = cubetas[i]
        # Ordenar por rendimiento ascendente, en caso de empate por cantidad de deportistas descendente
        insertion_sort(cubeta_actual,criterionName)
        
    arr_ordenado = []
    for cubeta in cubetas:
        for objeto in cubeta:
            arr_ordenado.append(objeto)
    
    return arr_ordenado

def insertion_sort(arr,rendimientoName):
    for i in range(1,len(arr)):
        actual = arr[i]
        j = i - 1
        
        rend_actual = getattr(actual, rendimientoName)
        deport_actual = getattr(actual, "numeroDeportistas")
        
        while j>=0:
            rend_j = getattr(arr[j], rendimientoName)
            deport_j = getattr(arr[j], "numeroDeportistas")
            
            if rend_actual < rend_j:
                arr[j+1] = arr[j]
            
            elif rend_actual == rend_j and deport_actual > deport_j:
                arr[j+1] = arr[j]
            
            else:
                break
            
            j -= 1
        
        arr[j+1] = actual
        
    return arr
                

class Deportista():
    def __init__(self,id,nombre,edad,rendimiento):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento
        

class Equipo():
    def __init__(self,deporte,deportistas,sede=None):
        self.sede = sede
        self.deporte = deporte
        self.deportistas = deportistas
        self.numeroDeportistas = len(deportistas)
        self.listasIdOrdenados = []
        self.rendimientoPromedio= 0
    
    def calcularRendimientoPromedio(self):
        acumulado = 0
        for deportista in self.deportistas:
            acumulado += deportista.rendimiento
        
        self.rendimientoPromedio = acumulado/self.numeroDeportistas
    
    def obtenerListaOrdenadaPorRendimiento(self):
        deportistas_ordenados = counting_sort(self.deportistas, "rendimiento")
        self.listasIdOrdenados = [dep.id for dep in deportistas_ordenados]
        return self.listasIdOrdenados
        
            

class Sede():
    def __init__(self,nombre,equipos):
        self.nombre = nombre
        self.equipos = equipos 
        for equipo in self.equipos:
            equipo.sede = self
        self.listasIdOrdenados = []
        self.rendimientoPromedio= 0
        self.numeroEquipos = len(equipos)
        self.numeroDeportistas = sum(equipo.numeroDeportistas for equipo in equipos)
        
    def calcularRendimientoPromedio(self):
        self.calcularRendimientosPromediosEquipos()
        acumulado = 0
        for equipo in self.equipos:
            acumulado += equipo.rendimientoPromedio
        
        self.rendimientoPromedio = acumulado/self.numeroEquipos
    
    def calcularRendimientosPromediosEquipos(self):
        for equipo in self.equipos:
            equipo.calcularRendimientoPromedio()
    
    def obtenerListaOrdenadaPorRendimiento(self):
        self.listasIdOrdenados = bucket_sort(self.equipos,"rendimientoPromedio")
        return self.listasIdOrdenados

def ranking(jugadores_base):
    jugadoresb = counting_sort(list(jugadores_base.values()),"rendimiento")
    ranking = []
    for jugadores in jugadoresb:
        ranking.append(jugadores.id)
    print("Ranking de jugadores por rendimiento",ranking)

def rendimientosExtremos(jugadores_base):  
    jugadoresb = counting_sort(list(jugadores_base.values()),"rendimiento")
    print("Jugador con menor rendimiento: ", jugadoresb[0].id, jugadoresb[0].nombre, jugadoresb[0].rendimiento)
    print("Jugador con mayor rendimiento: ", jugadoresb[-1].id, jugadoresb[-1].nombre, jugadoresb[-1].rendimiento)

def rendimientoEquipos(sedes):
    todos_los_equipos = []
    for sede in sedes:
        todos_los_equipos.extend(sede.equipos)
    equipos_ordenados = bucket_sort(todos_los_equipos, "rendimientoPromedio")
    equipo_menor = equipos_ordenados[0]
    print(f"\nEquipo con MENOR rendimiento: {equipo_menor.deporte} - Sede: {equipo_menor.sede.nombre} (Rendimiento: {equipo_menor.rendimientoPromedio:.2f})")

    equipo_mayor = equipos_ordenados[-1]
    print(f"Equipo con MAYOR rendimiento: {equipo_mayor.deporte} - Sede: {equipo_mayor.sede.nombre} (Rendimiento: {equipo_mayor.rendimientoPromedio:.2f})")

def edadesExtremos(jugadores_base):  
    jugadoresb = counting_sortSimple(list(jugadores_base.values()),"edad")
    print("Jugador más joven: ", jugadoresb[0].id, jugadoresb[0].nombre, jugadoresb[0].edad)
    print("Jugador más veterano: ", jugadoresb[-1].id, jugadoresb[-1].nombre, jugadoresb[-1].edad)

def edadPromedioTotal(jugadores_base):
    total = 0
    for jugador in jugadores_base.values():
        total += jugador.edad
    promedio = total / len(jugadores_base)
    print(f"Edad promedio total de los deportistas: {promedio:.2f}")
    
def rendimientoPromedioTotal(jugadores_base):
    total = 0
    for jugador in jugadores_base.values():
        total += jugador.rendimiento
    promedio = total / len(jugadores_base)
    print(f"Rendimiento promedio total de los deportistas: {promedio:.2f}")