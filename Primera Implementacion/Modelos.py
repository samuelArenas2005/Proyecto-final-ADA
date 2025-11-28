import math

def counting_sort(arr,rendimientoName,idName):
    # 1. Encontrar el valor máximo (k)
    max_val = 100
        
    count = [0] * (max_val + 1)
        
        # 3. Contar la frecuencia de cada elemento
    for num in arr:
        rendimiento = getattr(num, rendimientoName)
        count[rendimiento] += 1
            
    for i in range(1, len(count)):
        count[i] += count[i - 1]
            
    # 5. Inicializar el arreglo de salida
    output = [0] * len(arr)
        
    for num in reversed(arr):
        # La posición final es count[num] - 1
        rendimiento = getattr(num, rendimientoName)
        id = getattr(num, idName)
        posicion_final = count[rendimiento] - 1
        output[posicion_final] = id
            
        # Decrementar el contador para el próximo número igual
        count[num.rendimiento] -= 1
        
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
        cubeta_actual.sort(key=lambda elemento: getattr(elemento, rendimientoName))
        
    arr_ordenado = []
    for cubeta in cubetas:
        for objeto in cubeta:
            arr_ordenado.append(objeto)
    
    return arr_ordenado


class Deportista():
    def __init__(self,id,nombre,edad,rendimiento):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento
        

class Equipo():
    def __init__(self,deporte,deportistas,MaxDeportistas):
        self.deporte = deporte
        self.deportistas = deportistas
        self.numeroDeportistas = len(deportistas)
        self.MaxDeportistas = MaxDeportistas
        self.listasIdOrdenados = []
        self.rendimientoPromedio= 0
    
    def calcularRendimientoPromedio(self):
        acumulado = 0
        for deportista in self.deportistas:
            acumulado += deportista.rendimiento
        
        self.rendimientoPromedio = acumulado/self.numeroDeportistas
    
    def obtenerListaOrdenadaPorRendimiento(self):
        self.listasIdOrdenados = counting_sort(self.deportistas,"rendimiento","id")
        return self.listasIdOrdenados
        
            

class Sede():
    def __init__(self,nombre,equipos):
        self.nombre = nombre
        self.equipos = equipos 
        self.listasIdOrdenados = []
        self.rendimientoPromedio= 0
        self.numeroEquipos = len(equipos)
        
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

        