# 🏆 Proyecto Final: Gestión de Asociación de Deportes

Este repositorio contiene la solución al problema de la **"Asociación de Deportes"**, desarrollado como proyecto final para la asignatura de **Análisis y Diseño de Algoritmos I**.

El sistema modela una estructura jerárquica (**Sedes $\to$ Equipos $\to$ Deportistas**) para optimizar la gestión de recursos y realizar consultas estadísticas complejas (rankings, promedios, búsqueda de extremos) de manera eficiente.

## 📋 Características

El proyecto compara dos paradigmas de programación para resolver el mismo problema:

### 1. Primera Implementación (Estática / Arreglos)
*   **Enfoque:** Uso de **Arreglos Dinámicos** (Listas de Python).
*   **Algoritmos:** `Counting Sort` y `Bucket Sort` (Algoritmos de ordenamiento lineal para rangos acotados).
*   **Complejidad:** $O(N)$ bajo condiciones ideales.

### 2. Segunda Implementación (Dinámica / Punteros)
*   **Enfoque:** Uso de **Estructuras de Datos Dinámicas**.
*   **Estructuras:**
    *   **Árboles Rojinegros (Red-Black Trees):** Para mantener a los deportistas ordenados automáticamente por rendimiento/edad.
    *   **Listas Doblemente Enlazadas:** Para la gestión de Equipos y Sedes.
*   **Algoritmos:** `Merge Sort` adaptado a listas enlazadas.
*   **Complejidad:** $O(N \log N)$ (Escalable y eficiente en memoria).

## 🛠️ Estructura del Proyecto

```text
Proyecto-final-ADA/
├── input/                      # Archivos de entrada (ej: input3.txt)
├── output.txt                  # Archivo de salida generado automáticamente
├── main.py                     # 🟢 PUNTO DE ENTRADA (Orquestador)
│
├── PrimeraImplementacion/      # Solución basada en Arreglos
│   ├── Models.py               # Lógica de Counting/Bucket Sort
│   ├── buildOutput.py          # Generador de reportes
│   └── Tests/                  # Scripts de pruebas y gráficas
│
└── SegundaImplementacion/      # Solución basada en Árboles RB y Listas
    ├── SportsMan.py            # Clase Deportista (Nodo)
    ├── RBTree.py               # Clase Árbol Rojinegro
    ├── LinkedList.py           # Clase Lista Doblemente Enlazada
    ├── Models.py               # Gestión de la estructura
    ├── buildOutput.py          # Generador de reportes
    └── Tests/                  # Scripts de pruebas y gráficas
```
## ⚙️ Requisitos e Instalación

### 📌 Requisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- (Opcional) Entorno virtual recomendado (`venv` o `virtualenv`)
- Paquetes para gráficas: `matplotlib`, `numpy`

---

### 📥 Clonar el repositorio

```bash
git clone https://github.com/samuelArenas2005/Proyecto-final-ADA.git
cd Proyecto-final-ADA
```

### 🧰 Crear entorno virtual (recomendado)

Windows (PowerShell):
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```
Windows (cmd):
```bash
python -m venv venv
venv\Scripts\activate
```
Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```
---
### 📦Instalar dependencias 
```bash
pip install matplotlib numpy
```
### 📚Instalar la librería matplotlib
```bash
pip install matplotlib
```
---
## 🚀 Ejecución del Programa

El archivo `main.py` es el orquestador principal del proyecto.

---

### 🔧 Configuración

Edita las siguientes constantes al inicio del archivo `main.py`:

```python
# Archivo de entrada ubicado en la carpeta /input
#No es necesariamente input3.txt sino el archivo que tenga el input que se vaya a pasar por la implementación
INPUT_FILENAME = "input3.txt"

# Implementaciones disponibles:
# "array"             -> Primera Implementación (Arreglos)
# "red_&_black_tree"  -> Segunda Implementación (Árboles Rojinegros)
IMPLEMENTATION = "array"
````

---

### ▶️ Ejecutar

Desde la raíz del proyecto:

```bash
python main.py
```

El resultado se guardará automáticamente en el archivo `output.txt`.

---
## 🧪 Ejecución de Pruebas (Tests)

El proyecto incluye dos tipos de pruebas que se pueden ejecutar directamente desde la consola para validar cada implementación por separado.

- **Pruebas Funcionales (`Test.py` / `test.py`):** Imprimen en la terminal la lista de sedes, equipos, rankings y consultas para verificar que la lógica funciona correctamente.
- **Pruebas de Rendimiento (`TimeTest.py`):** Miden el tiempo de ejecución y generan gráficas comparativas entre la complejidad teórica \(O(n)\) y el comportamiento real.

---

### 🔹 Primera Implementación (Arreglos)

#### 📁 Navegar a la carpeta de pruebas

```bash
cd PrimeraImplementacion/Tests
````

#### ▶️ Opción A: Ver funcionamiento en consola

Ejecuta el script para ver cómo se generan los datos aleatorios y se calculan los rankings:

```bash
python Test.py
```

#### 📈 Opción B: Generar gráficas de rendimiento

1. Abre el archivo `TimeTest.py`.
2. Al final del archivo, modifica el valor en `run_prueba(X)` (del 1 al 9).

| Código | Descripción                                |
| ------ | ------------------------------------------ |
| 1–3    | Ordenamiento (Sedes / Equipos / Jugadores) |
| 4      | Ranking global                             |
| 5–9    | Consultas extremas y promedios             |

4. Ejecuta el script:

```bash
python TimeTest.py
```

---

### 🔸 Segunda Implementación (Árboles Rojinegros)

#### 📁 Navegar a la carpeta de pruebas

```bash
cd SegundaImplementacion/Tests
```

#### ▶️ Opción A: Ver funcionamiento en consola

Ejecuta el script para ver la estructura jerárquica y las consultas en tiempo real:

```bash
python test.py
```

#### 📉 Opción B: Generar gráficas de rendimiento

1. Abre el archivo `TimeTest.py`.
2. Al final del archivo, modifica el valor en `run_prueba(X)` según la tabla:

| Código | Descripción de la Prueba | Complejidad Esperada |
| ------ | ------------------------ | -------------------- |
| 1      | Ranking global           | (O(N \log N))        |
| 2      | Promedios (Lineal)       | (O(N))               |
| 3      | Sedes                    | (O(K \log K))        |
| 4      | Jugador extremo          | Eficiente ((~O(1)))  |
| 5      | Equipos por sede         | (O(M \log M))        |

3. Ejecuta el test:

```bash
python TimeTest.py
```

## ✒️ Autores

Proyecto realizado por estudiantes de la **Universidad del Valle**:

* Samuel Arenas Valencia
* Nicolás David Córdoba Osorio
* Juan Manuel Ampudia Jaramillo
* Daniel Andrade Reyes
* Miguel Ángel Castillo Sánchez


