import math

#ALGORITMOS DE ORDENAMIENTO

def counting_sort(arr, criterioName):
    max_rendimiento = 100
    max_edad = 100
    
    count = [[[] for _ in range(max_edad + 1)] for _ in range(max_rendimiento + 1)]
    
    # Agrupar elementos por rendimiento y edad
    for elemento in arr:
        rendimiento = int(getattr(elemento, criterioName))
        edad = int(getattr(elemento, "edad"))
        
        count[rendimiento][edad].append(elemento)
    
    output = []
    # Ordenar ascendente por rendimiento, y dentro de cada rendimiento descendente por edad
    for rendimiento in range(max_rendimiento + 1):  
        for edad in range(max_edad, -1, -1):  # Descendente por edad
            output.extend(count[rendimiento][edad])
    
    return output

def counting_sortSimple(arr, criterioName):
    max_valor = 100
    
    count = [[] for _ in range(max_valor + 1)]
    
    # Agrupar elementos por el atributo especificado
    for elemento in arr:
        valor = int(getattr(elemento, criterioName))
        count[valor].append(elemento)
    
    output = []
    # Ordenar ascendente por el atributo
    for valor in range(max_valor + 1):  
        output.extend(count[valor])
    
    return output

def bucket_sort(arr,rendimientoName):
    NUM_CUBETAS = 10
    
    cubetas = [[] for _ in range(NUM_CUBETAS)]
    
    for elemento in arr:
        rendimiento = getattr(elemento, rendimientoName)
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
        insertion_sort(cubeta_actual,rendimientoName)
        
    arr_ordenado = []
    for cubeta in cubetas:
        for objeto in cubeta:
            arr_ordenado.append(objeto)
    
    return arr_ordenado

def insertion_sort(arr,criterioName):
    for i in range(1,len(arr)):
        actual = arr[i]
        j = i - 1
        
        rend_actual = getattr(actual, criterioName)
        deport_actual = getattr(actual, "numeroDeportistas")
        
        while j>=0:
            rend_j = getattr(arr[j], criterioName)
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
                
#CLASES PRINCIPALES

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


def mostrarDeportistas(jugadores_base):
    lines = []
    lines.append("\n" + "="*70)
    lines.append(f"{'ID':<5} {'Nombre':<30} {'Edad':<8} {'Rendimiento':<10}")
    lines.append("="*70)
    for jugador in sorted(jugadores_base.keys()):
        deportista = jugadores_base[jugador]
        lines.append(f"{jugador:<5} {deportista.nombre:<30} {deportista.edad:<8} {deportista.rendimiento:<10}")
    lines.append("="*70 + "\n")
    return lines

#SOLUCIÓN DEL EJERICIO

def ranckingSedes(lista_de_sedes):
    # Calcular rendimientos y ordenar
    for sede in lista_de_sedes:
        sede.calcularRendimientoPromedio()

    sedes_ordenadas = bucket_sort(lista_de_sedes, "rendimientoPromedio")
    
    # Construir estructura de retorno
    resultado = []
    for sede in reversed(sedes_ordenadas):
        equipos_organizados = sede.obtenerListaOrdenadaPorRendimiento()
        equipos_con_deportistas = []
        for equipo in reversed(equipos_organizados):
            deportistas_ordenados = equipo.obtenerListaOrdenadaPorRendimiento()
            equipos_con_deportistas.append({
                'equipo': equipo,
                'deportistas': deportistas_ordenados
            })
        resultado.append({
            'sede': sede,
            'equipos': equipos_con_deportistas
        })
    
    return resultado

def ranking(jugadores_base):
    jugadoresb = counting_sort(list(jugadores_base.values()), "rendimiento")
    ranking = [jug.id for jug in jugadoresb]
    return ranking

def rendimientosExtremos(jugadores_base):  
    jugadoresb = counting_sort(list(jugadores_base.values()), "rendimiento")
    menor = jugadoresb[0]
    mayor = jugadoresb[-1]
    return menor, mayor

def rendimientoEquipos(sedes):
    todos_los_equipos = []
    for sede in sedes:
        todos_los_equipos.extend(sede.equipos)
    equipos_ordenados = bucket_sort(todos_los_equipos, "rendimientoPromedio")
    equipo_menor = equipos_ordenados[0]
    equipo_mayor = equipos_ordenados[-1]
    return equipo_menor, equipo_mayor

def edadesExtremos(jugadores_base):  
    jugadoresb = counting_sortSimple(list(jugadores_base.values()), "edad")
    mas_joven = jugadoresb[0]
    mas_viejo = jugadoresb[-1]
    return mas_joven, mas_viejo

def edadPromedioTotal(jugadores_base):
    total = 0
    for jugador in jugadores_base.values():
        total += jugador.edad
    promedio = total / len(jugadores_base)
    return promedio
    
def rendimientoPromedioTotal(jugadores_base):
    total = 0
    for jugador in jugadores_base.values():
        total += jugador.rendimiento
    promedio = total / len(jugadores_base)
    return promedio