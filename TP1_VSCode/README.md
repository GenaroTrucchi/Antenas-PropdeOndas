# TP1 - Visualización de Patrones de Radiación de Dipolos

Este proyecto calcula y visualiza los patrones de radiación de antenas dipolo de diferentes longitudes relativas (L/λ) utilizando Python. Genera imágenes 2D y 3D de los patrones y ofrece visualizaciones interactivas.

## Contenido

*   `main.py`: Script principal que calcula los patrones de radiación y guarda imágenes estáticas 2D (en `Imagenes2D/`) y 3D (en `Imagenes3D/`) usando Matplotlib.
*   `mayavi_visualize.py`: Script para generar y guardar imágenes 3D de los patrones de radiación utilizando la biblioteca Mayavi. Guarda los archivos en `Imagenes3D/`.
*   `view_pyvista.py`: Script para visualizar los patrones de radiación 3D de forma interactiva utilizando la biblioteca PyVista.
*   `requirements.txt`: Lista de dependencias básicas (numpy, matplotlib).

## Requisitos

*   **Python:** Se recomienda **Python 3.9** para una mejor compatibilidad con las bibliotecas de visualización 3D (especialmente Mayavi/VTK). Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
*   **Git:** Para clonar el repositorio.

## Instalación

1.  **Clonar el Repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO_EN_GITHUB>
    cd TP1_VSCode 
    ```
    (Reemplaza `<URL_DEL_REPOSITORIO_EN_GITHUB>` con la URL real de tu repositorio).

2.  **Crear y Activar un Entorno Virtual:**
    (Se recomienda usar un entorno virtual para aislar las dependencias del proyecto).
    ```bash
    # Crear el entorno (puedes llamarlo .venv o como prefieras)
    python -m venv .venv 

    # Activar en Windows (PowerShell)
    .\.venv\Scripts\Activate.ps1

    # Activar en Windows (Git Bash o CMD)
    .\.venv\Scripts\activate

    # Activar en macOS/Linux
    source .venv/bin/activate
    ```
    *Deberías ver `(.venv)` al principio de la línea de comandos de tu terminal.*

3.  **Instalar Dependencias Básicas:**
    Estas son necesarias para `main.py`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Instalar Dependencias para Visualización 3D (Opcional):**

    *   **Para `mayavi_visualize.py`:**
        Mayavi requiere VTK y un backend de GUI como PyQt5. La instalación puede ser compleja; se recomienda Python 3.9 y VTK 9.1.0 para mayor estabilidad.
        ```bash
        # Instalar PyQt5 (backend GUI)
        pip install PyQt5 PyQt5-sip

        # Instalar VTK (versión recomendada para compatibilidad)
        pip install vtk==9.1.0 

        # Instalar Mayavi y sus dependencias asociadas
        pip install mayavi traits pyface apptools envisage configobj six traitsui pygments
        ```
        *Nota: Si `pip install vtk==9.1.0` falla, puede ser por incompatibilidad con tu versión de Python. Intenta con una versión más reciente de VTK (`pip install vtk`) o asegúrate de usar Python 3.9.*

    *   **Para `view_pyvista.py`:**
        PyVista es generalmente más fácil de instalar.
        ```bash
        pip install pyvista
        ```

## Uso

Asegúrate de tener el entorno virtual activado antes de ejecutar los scripts.

1.  **Generar Imágenes 2D y 3D (Matplotlib):**
    Este script calcula los patrones y guarda las imágenes en las carpetas `Imagenes2D` e `Imagenes3D`.
    ```bash
    python main.py
    ```
    *El script esperará a que presiones ENTER al finalizar.*

2.  **Generar Imágenes 3D (Mayavi):**
    Este script utiliza Mayavi para generar y guardar las imágenes 3D en `Imagenes3D`. Requiere las dependencias de Mayavi instaladas.
    ```bash
    python mayavi_visualize.py
    ```

3.  **Visualización Interactiva 3D (PyVista):**
    Este script abre ventanas interactivas para cada patrón de radiación usando PyVista. Requiere PyVista instalado.
    ```bash
    python view_pyvista.py
    ```
    *Se abrirá una ventana por cada valor de L/λ definido en `main.py`. Cierra cada ventana para que se muestre la siguiente.*

## Salida

*   **`Imagenes2D/`**: Contiene los gráficos 2D de los patrones de radiación generados por `main.py`.
*   **`Imagenes3D/`**: Contiene los gráficos 3D de los patrones de radiación generados por `main.py` y/o `mayavi_visualize.py`.
*   **Ventanas Interactivas**: `view_pyvista.py` mostrará ventanas interactivas para explorar los modelos 3D.
