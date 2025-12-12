from pathlib import Path
from typing import List, Dict
from . import Models


def load_sites_from_input(path: Path) -> List[Models.Sede]:
    """Carga las sedes desde un archivo de entrada."""
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el archivo de entrada en {path}")

    context = {
        "SportsMan": Models.Deportista,
        "Team": Models.Equipo,
        "Site": Models.Sede,
    }

    code = path.read_text(encoding="utf-8")
    exec(code, context)

    sites = [value for value in context.values() if isinstance(value, Models.Sede)]
    if not sites:
        raise ValueError("El archivo de entrada no definió ninguna sede.")
    return sites


def build_output(lista_de_sedes: List[Models.Sede]) -> List[str]:
    """Construye la salida formateada a partir de las sedes usando métodos de Models."""
    lines: List[str] = []

    # Recolectar todos los deportistas
    todos_los_deportistas: Dict[int, Models.Deportista] = {}
    for sede in lista_de_sedes:
        for equipo in sede.equipos:
            for deportista in equipo.deportistas:
                todos_los_deportistas[deportista.id] = deportista

    # Mostrar deportistas usando el método de Models
    lines.extend(Models.mostrarDeportistas(todos_los_deportistas))

    # Resultados ordenados usando ranckingSedes de Models
    resultados_sedes = Models.ranckingSedes(lista_de_sedes)
    lines.append("=== RESULTADOS===")
    for item_sede in resultados_sedes:
        sede = item_sede['sede']
        lines.append(f"Sede {sede.nombre}:")
        for item_equipo in item_sede['equipos']:
            equipo = item_equipo['equipo']
            deportistas = item_equipo['deportistas']
            lines.append(f"\t{equipo.deporte}: {deportistas}")
        lines.append("")

    # Ranking de jugadores usando método de Models
    lines.append("")
    ranking_list = Models.ranking(todos_los_deportistas)
    lines.append("Ranking Jugadores por ids:")
    lines.append(str(ranking_list))
    lines.append("")

    # Consultas solicitadas
    lines.append("Consultas Solicitadas:")
    lines.append("")

    # Mejores y peores equipos usando método de Models
    equipo_menor, equipo_mayor = Models.rendimientoEquipos(lista_de_sedes)
    lines.append(
        f"Equipo con mayor rendimiento: {equipo_mayor.deporte} de {equipo_mayor.sede.nombre}."
    )
    lines.append(
        f"Equipo con menor rendimiento: {equipo_menor.deporte} de {equipo_menor.sede.nombre}."
    )

    # Mejores y peores deportistas usando método de Models
    menor_rend, mayor_rend = Models.rendimientosExtremos(todos_los_deportistas)
    lines.append(
        f"Jugador con mayor rendimiento: {{{mayor_rend.id}, {mayor_rend.nombre}, {mayor_rend.rendimiento}}}."
    )
    lines.append(
        f"Jugador con menor rendimiento: {{{menor_rend.id}, {menor_rend.nombre}, {menor_rend.rendimiento}}}."
    )

    # Edades extremas usando método de Models
    mas_joven, mas_viejo = Models.edadesExtremos(todos_los_deportistas)
    lines.append(f"Jugador más joven: {{{mas_joven.id}, {mas_joven.nombre}, {mas_joven.edad}}}.")
    lines.append(f"Jugador más veterano: {{{mas_viejo.id}, {mas_viejo.nombre}, {mas_viejo.edad}}}.")

    # Promedios usando métodos de Models
    edad_promedio = Models.edadPromedioTotal(todos_los_deportistas)
    rendimiento_promedio = Models.rendimientoPromedioTotal(todos_los_deportistas)
    lines.append(f"Promedio de edad de los jugadores: {edad_promedio:.2f}")
    lines.append(f"Promedio del rendimiento de los jugadores: {rendimiento_promedio:.2f}")

    return lines


def generate_output(input_path: Path, output_path: Path) -> List[str]:
    """Procesa el archivo de entrada y escribe el resultado en la ruta indicada."""
    sites = load_sites_from_input(input_path)
    output_lines = build_output(sites)
    output_path.write_text("\n".join(output_lines), encoding="utf-8")
    return output_lines
