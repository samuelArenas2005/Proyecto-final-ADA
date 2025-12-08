import Models
from SportsMan import SportsMan
import RBTree

#Ejemplos

# Crear un equipo
equipo = Models.Team("Real Madrid")

# Crear algunos deportistas
deportistas = [
    SportsMan(id=1, name="Cristiano", age=38, performance=95),
    SportsMan(id=2, name="Benzema", age=36, performance=92),
    SportsMan(id=3, name="Vinicius", age=23, performance=94),
    SportsMan(id=4, name="Modric", age=37, performance=80),
    SportsMan(id=5, name="Nacho", age=28, performance=85),
]

# Insertar los deportistas en el equipo
equipo.insert_sportsmen(deportistas)

# Obtener el deportista con máximo rendimiento
max_deportista = equipo.cal_max_performance()
min_deportista = equipo.cal_min_performance()
joven_deportista = equipo.cal_youngest_player()
deportista_veterano = equipo.cal_most_veteran_player()
equipo.cal_average_performance()


print("=== Equipo:", equipo.name, "===")
print(f"Deportista con mejor rendimiento: {max_deportista.name}",
      f"su puntaje es: {max_deportista.performance}")
print(f"Deportista con menor rendimiento: {min_deportista.name}",
      f"su puntaje es: {min_deportista.performance}")
print(f"El deportista mas joven es: {joven_deportista.name}")
print(f"El deportista mas veterano es: {deportista_veterano.name}")
print(f"La edad promedio del equipo es: {equipo.cal_average_age()} años")
print(f"El rendimiento promedio del equipo es: {equipo.get_average_performance()}")
