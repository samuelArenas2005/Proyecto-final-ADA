import Models
from SportsMan import SportsMan
import RBTree

# Base de deportistas disponibles
jugadores_base = {
    1: SportsMan(1, "Sofía Medina", 20, 66),
    2: SportsMan(2, "Alejandro medina", 27, 24),
    3: SportsMan(3, "Valentina Rodríguez", 19, 15),
    4: SportsMan(4, "Juan López", 22, 78),
    5: SportsMan(5, "Martina Martínez", 30, 55),
    6: SportsMan(6, "Sebastián Pérez", 25, 42),
    7: SportsMan(7, "Camila Fernández", 24, 36),
    8: SportsMan(8, "Mateo González", 29, 89),
    9: SportsMan(9, "Isabella Díaz", 21, 92),
    10: SportsMan(10, "Daniel Ruiz", 100, 57),
    11: SportsMan(11, "Luciana Sánchez", 18, 89),
    12: SportsMan(12, "Lucas Vásquez", 2600, 82)
}

# --- SEDE CALI ---
print("=" * 60)
print("SEDE CALI")
print("=" * 60)

cali_equipo_futbol = Models.Team("Cali Fútbol Club")
cali_equipo_futbol.insert_sportsmen([jugadores_base[1], jugadores_base[2], jugadores_base[3]])
cali_equipo_basket = Models.Team("Cali Basket Club")
cali_equipo_basket.insert_sportsmen([jugadores_base[4], jugadores_base[5], jugadores_base[6]])

sede_cali = Models.Site("Cali")
sede_cali.insert_teams([cali_equipo_futbol, cali_equipo_basket])
print(sede_cali.get_oldest_player_across_teams())

print("=" * 60)
print("SEDE MEDELLIN")
print("=" * 60)

medellin_equipo_futbol = Models.Team("Medellín Fútbol Club")
medellin_equipo_futbol.insert_sportsmen([jugadores_base[7], jugadores_base[8]])
medellin_equipo_basket = Models.Team("Medellín Basket Club")
medellin_equipo_basket.insert_sportsmen([jugadores_base[9], jugadores_base[10], jugadores_base[11], jugadores_base[12]])
sede_medellin = Models.Site("Medellín")
sede_medellin.insert_teams([medellin_equipo_futbol, medellin_equipo_basket])
print(sede_medellin.get_oldest_player_across_teams())

print("Volvemos a imprimir la sede de Cali para verificar que no se ha modificado:")
print(sede_cali.get_oldest_player_across_teams())