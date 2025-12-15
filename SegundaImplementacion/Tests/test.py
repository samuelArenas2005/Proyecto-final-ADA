import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from SegundaImplementacion.SportsMan import SportsMan
from SegundaImplementacion.Models import Team, Site, List_of_Sites


# Crear los deportistas manualmente (ejemplo del input1.txt)
j1 = SportsMan(1, "Juan", 20, 94)
j2 = SportsMan(2, "Maria", 21, 94)
j3 = SportsMan(3, "Pedro", 22, 21)
j4 = SportsMan(4, "Ana", 23, 25)
j5 = SportsMan(5, "Carlos", 24, 66)
j6 = SportsMan(6, "Laura", 25, 52)
j7 = SportsMan(7, "Jose", 26, 48)
j8 = SportsMan(8, "Luis", 27, 73)
j9 = SportsMan(9, "Sara", 28, 92)
j10 = SportsMan(10, "Jorge", 29, 51)
j11 = SportsMan(11, "Lorena", 30, 90)
j12 = SportsMan(12, "Raul", 31, 100)

# Crear los equipos
e1 = Team("Futbol", [j1, j2, j3])
e2 = Team("Volleyball", [j4, j5, j6])
e3 = Team("Futbol", [j7, j8, j9])
e4 = Team("Volleyball", [j10, j11, j12])

# Crear las sedes
s1 = Site("Sede Cali", [e1, e2])
s2 = Site("Sede Medellin", [e3, e4])

# Crear la lista de sedes
lista_sedes = List_of_Sites(sites=[s1, s2])

print("="*60)
print("RESULTADOS POR SEDE Y EQUIPO")
print("="*60)

# Mostrar resultados por sede/equipo
current_site = lista_sedes.sites.head
while current_site is not None:
    site = current_site.data
    print(f"\n{site.get_name()}, Rendimiento {site.get_average_performance():.2f}:")
    
    site.order_teams_by_performance()
    current_team = site.teams.head
    while current_team is not None:
        team = current_team.data
        ids = team.get_ordered_list_ids()
        ids_str = "{" + ", ".join(str(id) for id in ids) + "}"
        print(f"\t\t{team.get_name()}, Rendimiento {team.get_average_performance():.2f}: {ids_str}")
        current_team = current_team.next
    
    current_site = current_site.next

print("\n" + "="*60)
print("RANKING DE JUGADORES POR IDS")
print("="*60)

# Obtener y mostrar ranking global
ranking_linked_list = lista_sedes.get_all_sportsmen_ranked_across_Sites()
ranking_ids = []
current_player = ranking_linked_list.head
while current_player is not None:
    ranking_ids.append(current_player.data.id)
    current_player = current_player.next

ids_str = "{" + ", ".join(str(id) for id in ranking_ids) + "}"
print(f"Ranking Jugadores por ids:\n{ids_str}")

print("\n" + "="*60)
print("CONSULTAS SOLICITADAS")
print("="*60)
print()

# Obtener todas las consultas
best_team, best_team_site = lista_sedes.get_best_team_across_Sites()
worst_team, worst_team_site = lista_sedes.get_worst_team_across_Sites()
best_player = lista_sedes.get_best_player_across_Sites()
worst_player = lista_sedes.get_worst_player_across_Sites()
youngest_player = lista_sedes.get_youngest_player_across_Sites()
oldest_player = lista_sedes.get_oldest_player_across_Sites()
average_age = lista_sedes.get_average_age_across_Sites()
average_performance = lista_sedes.get_average_performance_across_Sites()

# Imprimir consultas
if best_team is not None and best_team_site is not None:
    print(f"Equipo con mayor rendimiento: {best_team.get_name()} de {best_team_site.get_name()}.")
else:
    print("Equipo con mayor rendimiento: No disponible.")

if worst_team is not None and worst_team_site is not None:
    print(f"Equipo con menor rendimiento: {worst_team.get_name()} de {worst_team_site.get_name()}.")
else:
    print("Equipo con menor rendimiento: No disponible.")

if best_player is not None:
    print(f"Jugador con mayor rendimiento: {{{best_player.id}, {best_player.name}, {best_player.performance}}}.")
else:
    print("Jugador con mayor rendimiento: {}.")

if worst_player is not None:
    print(f"Jugador con menor rendimiento: {{{worst_player.id}, {worst_player.name}, {worst_player.performance}}}.")
else:
    print("Jugador con menor rendimiento: {}.")

if youngest_player is not None:
    print(f"Jugador más joven: {{{youngest_player.id}, {youngest_player.name}, {youngest_player.age}}}.")
else:
    print("Jugador más joven: {}.")

if oldest_player is not None:
    print(f"Jugador más veterano: {{{oldest_player.id}, {oldest_player.name}, {oldest_player.age}}}.")
else:
    print("Jugador más veterano: {}.")

print(f"Promedio de edad de los jugadores: {average_age:.2f}")
print(f"Promedio del rendimiento de los jugadores: {average_performance:.2f}")

print("\n" + "="*60)
print("FIN DE LA EJECUCIÓN")
print("="*60)
