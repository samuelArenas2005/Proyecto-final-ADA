from pathlib import Path
from SegundaImplementacion.buildOutput import generate_output as generate_output_second_implementation
from importlib import import_module

PROJECT_ROOT = Path(__file__).resolve().parent
INPUT_DIR = PROJECT_ROOT / "input"
OUTPUT_FILE = PROJECT_ROOT / "output.txt"

# Cambia este valor a "input2.txt" (o cualquier otro) cuando quieras probar otro archivo.
INPUT_FILENAME = "input1.txt"

IMPLEMENTATION = "array"  # Cambia a "red_&_black_tree" para usar la segunda implementación


def main() -> None:
    input_path = INPUT_DIR / INPUT_FILENAME
    if not input_path.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo {INPUT_FILENAME} en la carpeta input"
        )

    if IMPLEMENTATION == "red_&_black_tree":
        generate_output_second_implementation(input_path=input_path, output_path=OUTPUT_FILE)
    elif IMPLEMENTATION == "array":
        # Importar dinámicamente la primera implementación
        primera_impl = import_module("Primera Implementacion.buildOutput")
        primera_impl.generate_output(input_path=input_path, output_path=OUTPUT_FILE)
    else:
        raise ValueError(
            f"Implementación no válida: {IMPLEMENTATION}. Usa 'array' o 'red_&_black_tree'"
        )
    
    print(f"Resultados guardados en {OUTPUT_FILE} (Implementación: {IMPLEMENTATION})")


if __name__ == "__main__":
    main()
