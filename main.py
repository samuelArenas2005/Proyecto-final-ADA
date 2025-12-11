from pathlib import Path
from SegundaImplementacion import generate_output as generate_output_second_implementation

PROJECT_ROOT = Path(__file__).resolve().parent
INPUT_DIR = PROJECT_ROOT / "input"
OUTPUT_FILE = PROJECT_ROOT / "output.txt"

# Cambia este valor a "input2.txt" (o cualquier otro) cuando quieras probar otro archivo.
INPUT_FILENAME = "input1.txt"


def main() -> None:
    input_path = INPUT_DIR / INPUT_FILENAME
    if not input_path.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo {INPUT_FILENAME} en la carpeta input"
        )

    generate_output_second_implementation(input_path=input_path, output_path=OUTPUT_FILE)
    print(f"Resultados guardados en {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
