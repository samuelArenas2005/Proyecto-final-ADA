import math

def counting_sort(arr, rendimientoName):
    max_rendimiento = 100
    max_edad = 100
    
    count = [[[] for _ in range(max_edad + 1)] for _ in range(max_rendimiento + 1)]
    
    # Agrupar elementos por rendimiento y edad
    for elemento in arr:
        rendimiento = int(getattr(elemento, rendimientoName))
        edad = int(getattr(elemento, "edad"))
        
        count[rendimiento][edad].append(elemento)
    
    output = []
    # Ordenar ascendente por rendimiento, y dentro de cada rendimiento descendente por edad
    for rendimiento in range(max_rendimiento + 1):  
        for edad in range(max_edad, -1, -1):  # Descendente por edad
            output.extend(count[rendimiento][edad])
    
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

def obtenerEquiposOrdenados(sedes):
    todos_los_equipos = []
    
    for sede in sedes:
        for equipo in sede.equipos:
            todos_los_equipos.append(equipo)
    equipos_ordenados = bucket_sort(todos_los_equipos, "rendimientoPromedio")
    
    return equipos_ordenados