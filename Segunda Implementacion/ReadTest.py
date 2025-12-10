import sys
import os

# Agregar el directorio padre al path para importar los módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from SportsMan import SportsMan
from Models import Team, Site, List_of_Sites

def read_and_execute_input(file_path):
    """
    Lee un archivo de texto con instrucciones de Python y las ejecuta,
    creando objetos SportsMan, Team, Site y List_of_Sites.
    """
    # Diccionario para almacenar los objetos creados
    objects = {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                
                # Saltar líneas vacías
                if not line:
                    continue
                
                # Ejecutar la línea directamente
                exec(line, globals(), objects)
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {file_path}")
        return None
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return None
    
    # Recolectar todos los sites creados
    sites = []
    for key, value in objects.items():
        if isinstance(value, Site):
            sites.append(value)
    
    # Crear y retornar el List_of_Sites
    if sites:
        list_of_sites = List_of_Sites(sites=sites)
        return list_of_sites
    else:
        print("Advertencia: No se encontraron objetos Site en el archivo")
        return None

def main():
    # Ruta al archivo de entrada
    input_file = os.path.join(os.path.dirname(__file__), '..', 'input1.txt')
    
    # Leer y ejecutar el archivo
    print("Leyendo y procesando el archivo de entrada...")
    list_of_sites = read_and_execute_input(input_file)
    
    if list_of_sites:
        print("\n✓ List_of_Sites creado exitosamente!")
        print(f"Número de sedes: {list_of_sites.sites.size}")
        
        # Mostrar información de las sedes
        current = list_of_sites.sites.head
        while current is not None:
            site = current.data
            print(f"\nSede: {site.name}")
            print(f"  Número de equipos: {site.teams.size}")
            print(f"  Total de deportistas: {site.get_number_of_sportsmen()}")
            
            # Mostrar equipos de cada sede
            team_current = site.teams.head
            while team_current is not None:
                team = team_current.data
                print(f"    - Equipo: {team.name}, Deportistas: {team.get_number_of_sportsmen()}")
                team_current = team_current.next
            
            current = current.next
        
        return list_of_sites
    else:
        print("\n✗ No se pudo crear el List_of_Sites")
        return None

main()
