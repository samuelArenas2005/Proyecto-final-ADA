import random

# Arreglos de datos base
NOMBRES = [
    "Juan", "María", "Carlos", "Ana", "Luis", "Carmen", "José", "Laura", "Pedro", "Isabel",
    "Miguel", "Elena", "Francisco", "Patricia", "Antonio", "Rosa", "Manuel", "Teresa", "Jesús", "Dolores",
    "Javier", "Pilar", "Fernando", "Mercedes", "Daniel", "Josefa", "Rafael", "Concepción", "David", "Francisca",
    "Óscar", "Cristina", "Sergio", "Antonia", "Rubén", "Margarita", "Adrián", "Lucía", "Álvaro", "Victoria",
    "Pablo", "Julia", "Raúl", "Beatriz", "Héctor", "Amparo", "Iván", "Rocío", "Diego", "Andrea",
    "Alberto", "Silvia", "Víctor", "Natalia", "Guillermo", "Marta", "Andrés", "Mónica", "Alejandro", "Alicia",
    "Roberto", "Paula", "Jorge", "Raquel", "Ricardo", "Susana", "Enrique", "Sara", "Ramón", "Inés",
    "Gabriel", "Eva", "Emilio", "Nuria", "Ignacio", "Angela", "Marcos", "Sonia", "Tomás", "Gloria",
    "Gonzalo", "Lorena", "Rodrigo", "Marina", "Eduardo", "Carolina", "Felipe", "Yolanda", "Santiago", "Ángeles",
    "Samuel", "Irene", "Martín", "Montserrat", "Arturo", "Encarnación", "Esteban", "Remedios", "Jaime", "Milagros"
]

APELLIDOS = [
    "García", "Rodríguez", "González", "Fernández", "López", "Martínez", "Sánchez", "Pérez", "Martín", "Gómez",
    "Jiménez", "Ruiz", "Hernández", "Díaz", "Moreno", "Muñoz", "Álvarez", "Romero", "Alonso", "Gutiérrez",
    "Navarro", "Torres", "Domínguez", "Vázquez", "Ramos", "Gil", "Ramírez", "Serrano", "Blanco", "Molina",
    "Castro", "Ortega", "Rubio", "Marín", "Sanz", "Núñez", "Iglesias", "Medina", "Garrido", "Cortés",
    "Castillo", "Santos", "Lozano", "Guerrero", "Cano", "Prieto", "Méndez", "Cruz", "Gallego", "Vega",
    "León", "Herrera", "Peña", "Flores", "Cabrera", "Campos", "Vidal", "Fuentes", "Carrasco", "Diez",
    "Reyes", "Caballero", "Nieto", "Aguilar", "Pascual", "Santana", "Herrero", "Lorenzo", "Hidalgo", "Montero",
    "Giménez", "Ibáñez", "Ferrer", "Durán", "Santiago", "Benítez", "Mora", "Vicente", "Vargas", "Arias",
    "Carmona", "Crespo", "Román", "Pastor", "Soto", "Sáez", "Velasco", "Moya", "Soler", "Parra",
    "Esteban", "Bravo", "Gallardo", "Rojas", "Pardo", "Delgado", "León", "Medina", "Ortiz", "Martos"
]

DEPORTES = [
    "Fútbol", "Baloncesto", "Voleibol", "Tenis", "Natación", "Atletismo", "Béisbol", "Rugby",
    "Hockey", "Ciclismo", "Boxeo", "Karate", "Judo", "Esgrima", "Tiro con Arco", "Gimnasia",
    "Escalada", "Surf", "Snowboard", "Esquí"
]

def generar_casos_prueba(min_jugadores_por_equipo, max_jugadores_por_equipo, num_equipos, num_sedes):
    """
    Genera casos de prueba aleatorios para el proyecto.
    
    Args:
        min_jugadores_por_equipo: Cantidad mínima de jugadores por equipo
        max_jugadores_por_equipo: Cantidad máxima de jugadores por equipo
        num_equipos: Cantidad fija de equipos por sede
        num_sedes: Cantidad fija de sedes
    
    Returns:
        tuple: (lista_sedes, lista_equipos, lista_deportistas)
    """
    
    # 1. Generar sedes (cantidad fija)
    lista_sedes = [f"Sede {i+1}" for i in range(num_sedes)]
    
    print(f"Generadas {num_sedes} sedes")
    
    # 2. Generar equipos base (cantidad fija, se replicarán en todas las sedes)
    equipos_base = []
    deportes_usados = {}  # Para controlar las repeticiones
    
    for i in range(num_equipos):
        deporte = random.choice(DEPORTES)
        
        # Si el deporte ya fue usado, agregar número
        if deporte in deportes_usados:
            deportes_usados[deporte] += 1
            nombre_equipo = f"{deporte} {deportes_usados[deporte]}"
        else:
            deportes_usados[deporte] = 1
            nombre_equipo = deporte
        
        equipos_base.append(nombre_equipo)
    
    # Crear lista completa de equipos: cada equipo base existe en cada sede
    lista_equipos = []
    for sede in lista_sedes:
        for equipo_base in equipos_base:
            lista_equipos.append(f"{equipo_base} - {sede}")
    
    print(f"Generados {num_equipos} tipos de equipos base")
    print(f"Total de equipos (replicados en {num_sedes} sedes): {len(lista_equipos)} equipos")
    
    # 3. Generar deportistas
    lista_deportistas = []
    id_counter = 1
    
    for equipo_completo in lista_equipos:
        # Extraer la sede del nombre del equipo
        equipo_base, sede_equipo = equipo_completo.rsplit(" - ", 1)
        
        # Cantidad aleatoria de jugadores para este equipo
        num_jugadores = random.randint(min_jugadores_por_equipo, max_jugadores_por_equipo)
        
        for j in range(num_jugadores):
            # Generar 2 nombres y 2 apellidos únicos
            nombres_elegidos = random.sample(NOMBRES, 2)
            apellidos_elegidos = random.sample(APELLIDOS, 2)
            
            nombre_completo = f"{nombres_elegidos[0]} {nombres_elegidos[1]} {apellidos_elegidos[0]} {apellidos_elegidos[1]}"
            
            deportista = {
                "id": id_counter,
                "nombre": nombre_completo,
                "edad": random.randint(8, 100),
                "rendimiento": random.randint(1, 100),
                "equipo": equipo_base,  # Solo el nombre base del equipo
                "sede": sede_equipo
            }
            
            lista_deportistas.append(deportista)
            id_counter += 1
    
    print(f"Generados {len(lista_deportistas)} deportistas")
    
    return lista_sedes, lista_equipos, lista_deportistas


def imprimir_resumen(lista_sedes, lista_equipos, lista_deportistas):
    """Imprime un resumen de los datos generados"""
    print("\n" + "="*60)
    print("RESUMEN DE DATOS GENERADOS")
    print("="*60)
    
    print(f"\n📍 SEDES ({len(lista_sedes)}):")
    for sede in lista_sedes:
        print(f"  - {sede}")
    
    print(f"\n🏆 EQUIPOS ({len(lista_equipos)}):")
    print("  (Formato: Equipo - Sede)")
    for equipo in lista_equipos[:10]:  # Mostrar solo los primeros 10
        print(f"  - {equipo}")
    if len(lista_equipos) > 10:
        print(f"  ... y {len(lista_equipos) - 10} más")
    
    print(f"\n👤 DEPORTISTAS ({len(lista_deportistas)}):")
    print("  Primeros 5 deportistas:")
    for deportista in lista_deportistas[:5]:
        print(f"  - ID: {deportista['id']}, {deportista['nombre']}, "
              f"Edad: {deportista['edad']}, Rendimiento: {deportista['rendimiento']}, "
              f"Equipo: {deportista['equipo']}, Sede: {deportista['sede']}")
    
    if len(lista_deportistas) > 5:
        print(f"  ... y {len(lista_deportistas) - 5} más")
    
    # Estadísticas por sede
    print("\n📊 ESTADÍSTICAS POR SEDE:")
    for sede in lista_sedes:
        deportistas_en_sede = [d for d in lista_deportistas if d['sede'] == sede]
        equipos_en_sede = set([d['equipo'] for d in deportistas_en_sede])
        print(f"  {sede}: {len(equipos_en_sede)} equipos, {len(deportistas_en_sede)} deportistas")
    
    print("\n" + "="*60)

if True:
    # Configuración
    MIN_JUGADORES_POR_EQUIPO = 5
    MAX_JUGADORES_POR_EQUIPO = 15
    NUM_EQUIPOS = 5  # Cantidad fija de equipos por sede
    NUM_SEDES = 10   # Cantidad fija de sedes

    print("Generando casos de prueba...")
    print(f"Configuración:")
    print(f"  - Min jugadores por equipo: {MIN_JUGADORES_POR_EQUIPO}")
    print(f"  - Max jugadores por equipo: {MAX_JUGADORES_POR_EQUIPO}")
    print(f"  - Equipos por sede: {NUM_EQUIPOS}")
    print(f"  - Sedes: {NUM_SEDES}")
    print()

    sedes, equipos, deportistas = generar_casos_prueba(
        MIN_JUGADORES_POR_EQUIPO,
        MAX_JUGADORES_POR_EQUIPO,
        NUM_EQUIPOS,
        NUM_SEDES
    )

    imprimir_resumen(sedes, equipos, deportistas)

    # Guardar en variables globales para uso externo
    SEDES_GENERADAS = sedes
    EQUIPOS_GENERADOS = equipos
    DEPORTISTAS_GENERADOS = deportistas
