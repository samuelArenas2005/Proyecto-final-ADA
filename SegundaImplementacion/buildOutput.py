import math
from pathlib import Path
from typing import List

from . import Models
from .SportsMan import SportsMan


def load_sites_from_input(path: Path) -> List[Models.Site]:
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el archivo de entrada en {path}")

    context = {
        "SportsMan": SportsMan,
        "Team": Models.Team,
        "Site": Models.Site,
    }

    code = path.read_text(encoding="utf-8")
    exec(code, context)

    sites = [value for value in context.values() if isinstance(value, Models.Site)]
    if not sites:
        raise ValueError("El archivo de entrada no definió ninguna sede.")
    return sites


def format_ids(ids):
    return "{" + ", ".join(str(_id) for _id in ids) + "}"


def format_player(player, attribute):
    if player is None:
        return "{}"
    value = getattr(player, attribute, None)
    return f"{{{player.id}, {player.name}, {value}}}"


def build_output(lista_sedes: Models.List_of_Sites) -> List[str]:
    lines: List[str] = []

    current_site = lista_sedes.sites.head
    while current_site is not None:
        site = current_site.data
        lines.append(f"{site.get_name()}, Rendimiento {site.get_average_performance()}:")

        site.order_teams_by_performance()
        current_team = site.teams.head
        while current_team is not None:
            team = current_team.data
            ids_str = format_ids(team.get_ordered_list_ids())
            lines.append(f"\t\t{team.get_name()}, Rendimiento {team.get_average_performance()}: {ids_str}")
            current_team = current_team.next
        lines.append("")  # Línea en blanco entre sedes
        current_site = current_site.next

    ranking_linked_list = lista_sedes.get_all_sportsmen_ranked_across_Sites()
    ranking_ids = []
    current_player = ranking_linked_list.head
    while current_player is not None:
        ranking_ids.append(current_player.data.id)
        current_player = current_player.next

    lines.append("Ranking Jugadores por ids:")
    lines.append(format_ids(ranking_ids))

    lines.append("")

    lines.append("Consultas Solicitadas:")

    lines.append("")

    best_team, best_team_site = lista_sedes.get_best_team_across_Sites()
    worst_team, worst_team_site = lista_sedes.get_worst_team_across_Sites()
    best_player = lista_sedes.get_best_player_across_Sites()
    worst_player = lista_sedes.get_worst_player_across_Sites()
    youngest_player = lista_sedes.get_youngest_player_across_Sites()
    oldest_player = lista_sedes.get_oldest_player_across_Sites()
    average_age = lista_sedes.get_average_age_across_Sites()
    average_performance = lista_sedes.get_average_performance_across_Sites()

    if best_team is not None and best_team_site is not None:
        lines.append(
            f"Equipo con mayor rendimiento: {best_team.get_name()} de {best_team_site.get_name()}."
        )
    else:
        lines.append("Equipo con mayor rendimiento: No disponible.")

    if worst_team is not None and worst_team_site is not None:
        lines.append(
            f"Equipo con menor rendimiento: {worst_team.get_name()} de {worst_team_site.get_name()}."
        )
    else:
        lines.append("Equipo con menor rendimiento: No disponible.")
    lines.append(f"Jugador con mayor rendimiento: {format_player(best_player, 'performance')}.")
    lines.append(f"Jugador con menor rendimiento: {format_player(worst_player, 'performance')}.")
    lines.append(f"Jugador más joven: {format_player(youngest_player, 'age')}.")
    lines.append(f"Jugador más veterano: {format_player(oldest_player, 'age')}.")
    lines.append(f"Promedio de edad de los jugadores: {average_age}")
    lines.append(f"Promedio del rendimiento de los jugadores: {average_performance}")

    return lines


def generate_output(input_path: Path, output_path: Path) -> List[str]:
    """Procesa el archivo de entrada y escribe el resultado en la ruta indicada."""

    sites = load_sites_from_input(input_path)
    lista_sedes = Models.List_of_Sites(sites=sites)

    output_lines = build_output(lista_sedes)
    output_path.write_text("\n".join(output_lines), encoding="utf-8")
    return output_lines
