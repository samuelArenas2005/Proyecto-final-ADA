import math

import Models
from SportsMan import SportsMan

# Base de deportistas disponibles
jugadores_base = {
    1: SportsMan(1, "Sofía García", 21, 66),
    2: SportsMan(2, "Alejandro Torres", 27, 24),
    3: SportsMan(3, "Valentina Rodríguez", 19, 15),
    4: SportsMan(4, "Juan López", 22, 78),
    5: SportsMan(5, "Martina Martínez", 30, 55),
    6: SportsMan(6, "Sebastián Pérez", 25, 42),
    7: SportsMan(7, "Camila Fernández", 24, 36),
    8: SportsMan(8, "Mateo González", 29, 89),
    9: SportsMan(9, "Isabella Díaz", 21, 92),
    10: SportsMan(10, "Daniel Ruiz", 17, 57),
    11: SportsMan(11, "Luciana Sánchez", 18, 89),
    12: SportsMan(12, "Lucas Vásquez", 26, 82),
}

# --- SEDE CALI ---
# Equipo Fútbol Cali: IDs 10, 2
equipo_cali_futbol = Models.Team("Fútbol sede Cali", [jugadores_base[10], jugadores_base[2]])

# Equipo Volleyball Cali: IDs 1, 9, 12, 6
equipo_cali_volley = Models.Team("Voleibol sede Cali", [jugadores_base[1], jugadores_base[9], jugadores_base[6], jugadores_base[12]])

# Crear Sede Cali
sede_cali = Models.Site("Cali", [equipo_cali_futbol, equipo_cali_volley])



# --- SEDE MEDELLÍN ---
# Equipo Fútbol Medellín: IDs 11, 8, 7
equipo_medellin_futbol = Models.Team("Fútbol sede Medellín", [jugadores_base[11], jugadores_base[8], jugadores_base[7]])

# Equipo Volleyball Medellín: IDs 3, 4, 5
equipo_medellin_volley = Models.Team("Voleibol sede Medellín", [jugadores_base[3], jugadores_base[4], jugadores_base[5]])

# Crear Sede Medellín
sede_medellin = Models.Site("Medellín", [equipo_medellin_futbol, equipo_medellin_volley])


# Crear Lista de Sedes
lista_sedes = Models.List_of_Sites(sites=[sede_cali, sede_medellin])

def truncate_two_decimals(value):
    return math.floor(value * 100) / 100 if value is not None else 0

best_team = lista_sedes.get_best_team_across_Sites()
worst_team = lista_sedes.get_worst_team_across_Sites()
best_player = lista_sedes.get_best_player_across_Sites()
worst_player = lista_sedes.get_worst_player_across_Sites()
youngest_player = lista_sedes.get_youngest_player_across_Sites()
oldest_player = lista_sedes.get_oldest_player_across_Sites()
average_age = lista_sedes.get_average_age_across_Sites()
average_performance = lista_sedes.get_average_performance_across_Sites()

best_player_str = best_player.format_attribute("performance") if best_player else "{}"
worst_player_str = worst_player.format_attribute("performance") if worst_player else "{}"
youngest_player_str = youngest_player.format_attribute("age") if youngest_player else "{}"
oldest_player_str = oldest_player.format_attribute("age") if oldest_player else "{}"

print(f"Equipo con mayor rendimiento: {best_team.get_name() if best_team else 'No disponible'}.")
print(f"Equipo con menor rendimiento: {worst_team.get_name() if worst_team else 'No disponible'}.")
print(f"Jugador con mayor rendimiento: {best_player_str}")
print(f"Jugador con menor rendimiento: {worst_player_str}")
print(f"Jugador más joven: {youngest_player_str}")
print(f"Jugador más veterano: {oldest_player_str}")
print(f"Promedio de edad de los jugadores: {truncate_two_decimals(average_age):.2f}")
print(f"Promedio del rendimiento de los jugadores: {truncate_two_decimals(average_performance):.2f}")