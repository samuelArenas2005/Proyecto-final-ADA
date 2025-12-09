import Models
from SportsMan import SportsMan
import RBTree

# Base de deportistas disponibles
jugadores_base = {
    1: SportsMan(1, "Sofía García", 2000, 66),
    2: SportsMan(2, "Alejandro Torres", 27, 24),
    3: SportsMan(3, "Valentina Rodríguez", 19, 15),
    4: SportsMan(4, "Juan López", 22, 78),
    5: SportsMan(5, "Martina Martínez", 30, 55),
    6: SportsMan(6, "Sebastián Pérez", 25, 42),
    7: SportsMan(7, "Camila Fernández", 24, 36),
    8: SportsMan(8, "Mateo González", 29, 89),
    9: SportsMan(9, "Isabella Díaz", 21, 92),
    10: SportsMan(10, "Daniel Ruiz", 100, 57),
    11: SportsMan(11, "Luciana Sánchez", 18, 89),
    12: SportsMan(12, "Lucas Vásquez", 26, 82)
}

# --- SEDE CALI ---
print("=" * 60)
print("SEDE CALI")
print("=" * 60)

# Equipo Fútbol Cali: IDs 10, 2
equipo_cali_futbol = Models.Team("Fútbol")
deportistas_cali_futbol = [jugadores_base[10], jugadores_base[2]]
equipo_cali_futbol.insert_sportsmen(deportistas_cali_futbol)
equipo_cali_futbol.cal_average_performance()

# Equipo Volleyball Cali: IDs 1, 9, 12, 6
equipo_cali_volley = Models.Team("Volleyball")
deportistas_cali_volley = [jugadores_base[1], jugadores_base[9], jugadores_base[12], jugadores_base[6]]
equipo_cali_volley.insert_sportsmen(deportistas_cali_volley)
equipo_cali_volley.cal_average_performance()

# Crear Sede Cali
sede_cali = Models.Site("Cali")
sede_cali.insert_teams([equipo_cali_futbol, equipo_cali_volley])
sede_cali.cal_average_performance()

# Mostrar resultados Cali
print(f"\nDeporte Fútbol:")
print(f"  - Mejor rendimiento: {equipo_cali_futbol.cal_max_performance().name} ({equipo_cali_futbol.cal_max_performance().performance})")
print(f"  - Peor rendimiento: {equipo_cali_futbol.cal_min_performance().name} ({equipo_cali_futbol.cal_min_performance().performance})")
print(f"  - Jugador más joven: {equipo_cali_futbol.cal_youngest_player().name} ({equipo_cali_futbol.cal_youngest_player().age} años)")
print(f"  - Jugador más veterano: {equipo_cali_futbol.cal_most_veteran_player().name} ({equipo_cali_futbol.cal_most_veteran_player().age} años)")
print(f"  - Rendimiento promedio: {equipo_cali_futbol.get_average_performance():.2f}")
print(f"  - Edad promedio: {equipo_cali_futbol.cal_average_age():.2f}")

print(f"\nDeporte Volleyball:")
print(f"  - Mejor rendimiento: {equipo_cali_volley.cal_max_performance().name} ({equipo_cali_volley.cal_max_performance().performance})")
print(f"  - Peor rendimiento: {equipo_cali_volley.cal_min_performance().name} ({equipo_cali_volley.cal_min_performance().performance})")
print(f"  - Jugador más joven: {equipo_cali_volley.cal_youngest_player().name} ({equipo_cali_volley.cal_youngest_player().age} años)")
print(f"  - Jugador más veterano: {equipo_cali_volley.cal_most_veteran_player().name} ({equipo_cali_volley.cal_most_veteran_player().age} años)")
print(f"  - Rendimiento promedio: {equipo_cali_volley.get_average_performance():.2f}")
print(f"  - Edad promedio: {equipo_cali_volley.cal_average_age():.2f}")

print(f"\nRendimiento promedio Sede Cali: {sede_cali.get_average_performance():.2f}")

# --- SEDE MEDELLÍN ---
print("\n" + "=" * 60)
print("SEDE MEDELLÍN")
print("=" * 60)

# Equipo Fútbol Medellín: IDs 11, 8, 7
equipo_medellin_futbol = Models.Team("Fútbol")
deportistas_medellin_futbol = [jugadores_base[11], jugadores_base[8], jugadores_base[7]]
equipo_medellin_futbol.insert_sportsmen(deportistas_medellin_futbol)
equipo_medellin_futbol.cal_average_performance()

# Equipo Volleyball Medellín: IDs 3, 4, 5
equipo_medellin_volley = Models.Team("Volleyball")
deportistas_medellin_volley = [jugadores_base[3], jugadores_base[4], jugadores_base[5]]
equipo_medellin_volley.insert_sportsmen(deportistas_medellin_volley)
equipo_medellin_volley.cal_average_performance()

# Crear Sede Medellín
sede_medellin = Models.Site("Medellín")
sede_medellin.insert_teams([equipo_medellin_futbol, equipo_medellin_volley])
sede_medellin.cal_average_performance()





# Mostrar resultados Medellín
print(f"\nDeporte Fútbol:")
print(f"  - Mejor rendimiento: {equipo_medellin_futbol.cal_max_performance().name} ({equipo_medellin_futbol.cal_max_performance().performance})")
print(f"  - Peor rendimiento: {equipo_medellin_futbol.cal_min_performance().name} ({equipo_medellin_futbol.cal_min_performance().performance})")
print(f"  - Jugador más joven: {equipo_medellin_futbol.cal_youngest_player().name} ({equipo_medellin_futbol.cal_youngest_player().age} años)")
print(f"  - Jugador más veterano: {equipo_medellin_futbol.cal_most_veteran_player().name} ({equipo_medellin_futbol.cal_most_veteran_player().age} años)")
print(f"  - Rendimiento promedio: {equipo_medellin_futbol.get_average_performance():.2f}")
print(f"  - Edad promedio: {equipo_medellin_futbol.cal_average_age():.2f}")

print(f"\nDeporte Volleyball:")
print(f"  - Mejor rendimiento: {equipo_medellin_volley.cal_max_performance().name} ({equipo_medellin_volley.cal_max_performance().performance})")
print(f"  - Peor rendimiento: {equipo_medellin_volley.cal_min_performance().name} ({equipo_medellin_volley.cal_min_performance().performance})")
print(f"  - Jugador más joven: {equipo_medellin_volley.cal_youngest_player().name} ({equipo_medellin_volley.cal_youngest_player().age} años)")
print(f"  - Jugador más veterano: {equipo_medellin_volley.cal_most_veteran_player().name} ({equipo_medellin_volley.cal_most_veteran_player().age} años)")
print(f"  - Rendimiento promedio: {equipo_medellin_volley.get_average_performance():.2f}")
print(f"  - Edad promedio: {equipo_medellin_volley.cal_average_age():.2f}")

print(f"\nRendimiento promedio Sede Medellín: {sede_medellin.get_average_performance():.2f}")

# --- RESUMEN GENERAL ---
print("\n" + "=" * 60)
print("RESUMEN GENERAL")
print("=" * 60)
lista_sedes = Models.List_of_Sites()
lista_sedes.insert_sites([sede_cali, sede_medellin])
print(f"Mejor Sede: Medellín ({sede_medellin.get_average_performance():.2f})") if sede_medellin.get_average_performance() > sede_cali.get_average_performance() else print(f"Mejor Sede: Cali ({sede_cali.get_average_performance():.2f})")

print("Ejemplo medellin")
print(f"Jugador más veterano de medellin: {sede_medellin.get_oldest_player_across_teams().name} ")