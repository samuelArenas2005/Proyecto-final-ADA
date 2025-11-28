from Modelos import Deportista,Equipo, Sede,counting_sort,bucket_sort

MinDeportistas = 0
MaxDeportistas = 7
MAXEQUIPOS = 5
MAXSEDES = 3

jugadores_base = {
    1: Deportista(1, "Sofía García", 21, 66),
    2: Deportista(2, "Alejandro Torres", 27, 24),
    3: Deportista(3, "Valentina Rodríguez", 19, 15),
    4: Deportista(4, "Juan López", 22, 78),
    5: Deportista(5, "Martina Martínez", 30, 55),
    6: Deportista(6, "Sebastián Pérez", 25, 42),
    7: Deportista(7, "Camila Fernández", 24, 36),
    8: Deportista(8, "Mateo González", 29, 89),
    9: Deportista(9, "Isabella Díaz", 21, 92),
    10: Deportista(10, "Daniel Ruiz", 17, 57),
    11: Deportista(11, "Luciana Sánchez", 18, 89),
    12: Deportista(12, "Lucas Vásquez", 26, 82)
}

# --- Sede Cali ---

# Fútbol Cali: IDs 10, 2
deportistas_cali_futbol = [jugadores_base[10], jugadores_base[2]]
equipo_cali_futbol = Equipo("Futbol", deportistas_cali_futbol, MaxDeportistas)

# Volleyball Cali: IDs 1, 9, 12, 6
deportistas_cali_volley = [jugadores_base[1], jugadores_base[9], jugadores_base[12], jugadores_base[6]]
equipo_cali_volley = Equipo("Volleyball", deportistas_cali_volley, MaxDeportistas)

deportes_sede_cali = [
    equipo_cali_futbol,
    equipo_cali_volley
]

sede_cali = Sede("Cali", deportes_sede_cali)


# --- Sede Medellín ---

# Fútbol Medellín: IDs 11, 8, 7
deportistas_medellin_futbol = [jugadores_base[11], jugadores_base[8], jugadores_base[7]]
equipo_medellin_futbol = Equipo("Futbol", deportistas_medellin_futbol, MaxDeportistas)

# Volleyball Medellín: IDs 3, 4, 5
deportistas_medellin_volley = [jugadores_base[3], jugadores_base[4], jugadores_base[5]]
equipo_medellin_volley = Equipo("Volleyball", deportistas_medellin_volley, MaxDeportistas)

deportes_sede_medellin = [
    equipo_medellin_futbol,
    equipo_medellin_volley
]

sede_medellin = Sede("Medellin", deportes_sede_medellin)


lista_de_sedes = [
    sede_cali,
    sede_medellin
]

for sede in lista_de_sedes:
    sede.calcularRendimientoPromedio()

listasIdOrdenados = bucket_sort(lista_de_sedes,"rendimientoPromedio")

for sede in reversed(listasIdOrdenados):
    print("Sede ", sede.nombre , ":\n")
    listasIdOrdenadosEquipos = sede.obtenerListaOrdenadaPorRendimiento()
    for equipo in reversed(listasIdOrdenadosEquipos):
        listasIdOrdenadosDeportistas = equipo.obtenerListaOrdenadaPorRendimiento()
        print("\t",equipo.deporte,": ", listasIdOrdenadosDeportistas, "\n")