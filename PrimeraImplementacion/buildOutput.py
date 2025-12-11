from pathlib import Path
from typing import List, Dict
from .Models import Deportista, Equipo, Sede, counting_sort, counting_sortSimple, bucket_sort


def load_sites_from_input(path: Path) -> List[Sede]:
    """Carga las sedes desde un archivo de entrada."""
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el archivo de entrada en {path}")

    context = {
        "SportsMan": Deportista,
        "Team": Equipo,
        "Site": Sede,
    }

    code = path.read_text(encoding="utf-8")
    exec(code, context)

    sites = [value for value in context.values() if isinstance(value, Sede)]
    if not sites:
        raise ValueError("El archivo de entrada no definió ninguna sede.")
    return sites


def build_output(lista_de_sedes: List[Sede]) -> List[str]:
    """Construye la salida formateada a partir de las sedes."""
    lines: List[str] = []

    # Recolectar todos los deportistas
    todos_los_deportistas: Dict[int, Deportista] = {}
    for sede in lista_de_sedes:
        for equipo in sede.equipos:
            for deportista in equipo.deportistas:
                todos_los_deportistas[deportista.id] = deportista

    # Tabla de deportistas
    lines.append("\n" + "="*70)
    lines.append(f"{'ID':<5} {'Nombre':<30} {'Edad':<8} {'Rendimiento':<10}")
    lines.append("="*70)
    for deport_id in sorted(todos_los_deportistas.keys()):
        deportista = todos_los_deportistas[deport_id]
        lines.append(
            f"{deportista.id:<5} {deportista.nombre:<30} {deportista.edad:<8} {deportista.rendimiento:<10}"
        )
    lines.append("="*70 + "\n")

    # Calcular rendimientos
    for sede in lista_de_sedes:
        sede.calcularRendimientoPromedio()

    # Ordenar sedes por rendimiento
    listasIdOrdenados = bucket_sort(lista_de_sedes, "rendimientoPromedio")

    # Resultados ordenados
    lines.append("=== RESULTADOS===\n")
    for sede in reversed(listasIdOrdenados):
        lines.append(f"Sede {sede.nombre}:\n")
        listasIdOrdenadosEquipos = sede.obtenerListaOrdenadaPorRendimiento()
        for equipo in reversed(listasIdOrdenadosEquipos):
            listasIdOrdenadosDeportistas = equipo.obtenerListaOrdenadaPorRendimiento()
            lines.append(f"\t{equipo.deporte}: {listasIdOrdenadosDeportistas}\n")

    # Ranking de jugadores
    lines.append("")
    deportistas_ordenados = counting_sort(list(todos_los_deportistas.values()), "rendimiento")
    ranking_ids = [dep.id for dep in deportistas_ordenados]
    lines.append("Ranking Jugadores por ids:")
    lines.append(str(ranking_ids))
    lines.append("")

    # Consultas solicitadas
    lines.append("Consultas Solicitadas:")
    lines.append("")

    # Mejores y peores equipos
    todos_los_equipos = []
    equipo_mejor = None
    equipo_peor = None
    equipo_mejor_sede = None
    equipo_peor_sede = None

    for sede in lista_de_sedes:
        for equipo in sede.equipos:
            todos_los_equipos.append(equipo)
            if equipo_mejor is None or equipo.rendimientoPromedio > equipo_mejor.rendimientoPromedio:
                equipo_mejor = equipo
                equipo_mejor_sede = sede
            if equipo_peor is None or equipo.rendimientoPromedio < equipo_peor.rendimientoPromedio:
                equipo_peor = equipo
                equipo_peor_sede = sede

    if equipo_mejor and equipo_mejor_sede:
        lines.append(
            f"Equipo con mayor rendimiento: {equipo_mejor.deporte} de {equipo_mejor_sede.nombre}."
        )
    else:
        lines.append("Equipo con mayor rendimiento: No disponible.")

    if equipo_peor and equipo_peor_sede:
        lines.append(
            f"Equipo con menor rendimiento: {equipo_peor.deporte} de {equipo_peor_sede.nombre}."
        )
    else:
        lines.append("Equipo con menor rendimiento: No disponible.")

    # Mejores y peores deportistas
    deportistas_ordenados_asc = counting_sort(list(todos_los_deportistas.values()), "rendimiento")
    mejor_rendimiento = deportistas_ordenados_asc[-1]
    peor_rendimiento = deportistas_ordenados_asc[0]

    lines.append(
        f"Jugador con mayor rendimiento: {{{mejor_rendimiento.id}, {mejor_rendimiento.nombre}, {mejor_rendimiento.rendimiento}}}."
    )
    lines.append(
        f"Jugador con menor rendimiento: {{{peor_rendimiento.id}, {peor_rendimiento.nombre}, {peor_rendimiento.rendimiento}}}."
    )

    # Edades extremas
    deportistas_por_edad = counting_sortSimple(list(todos_los_deportistas.values()), "edad")
    mas_joven = deportistas_por_edad[0]
    mas_viejo = deportistas_por_edad[-1]

    lines.append(f"Jugador más joven: {{{mas_joven.id}, {mas_joven.nombre}, {mas_joven.edad}}}.")
    lines.append(f"Jugador más veterano: {{{mas_viejo.id}, {mas_viejo.nombre}, {mas_viejo.edad}}}.")

    # Promedios
    edad_promedio = sum(d.edad for d in todos_los_deportistas.values()) / len(todos_los_deportistas)
    rendimiento_promedio = sum(
        d.rendimiento for d in todos_los_deportistas.values()
    ) / len(todos_los_deportistas)

    lines.append(f"Promedio de edad de los jugadores: {edad_promedio:.2f}")
    lines.append(f"Promedio del rendimiento de los jugadores: {rendimiento_promedio:.2f}")

    return lines


def generate_output(input_path: Path, output_path: Path) -> List[str]:
    """Procesa el archivo de entrada y escribe el resultado en la ruta indicada."""
    sites = load_sites_from_input(input_path)
    output_lines = build_output(sites)
    output_path.write_text("\n".join(output_lines), encoding="utf-8")
    return output_lines
