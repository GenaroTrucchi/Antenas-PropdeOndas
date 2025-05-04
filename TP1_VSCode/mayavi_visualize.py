#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mayavi_visualize.py — Visualización 3D por lotes usando Mayavi
Este script importa las funciones de main.py, parchea TVTKBase para evitar
el error "unhashable type: 'PolyData'", y genera PNGs de cada patrón 3D.
"""

# 0) — Parche ANTES de cualquier import de tvtk o mayavi —
import tvtk.tvtk_base as tvtk_base

def _tvtk_hash(self):
    # Usa la identidad interna de VTK como base del hash
    return id(self._vtk_obj)

# Inyecta __hash__ en la clase base de todos los objetos TVTK
tvtk_base.TVTKBase.__hash__ = _tvtk_hash
print(">>> Parche TVTK aplicado <<<")
# ——————————————————————————————————————————————————————

# 1) Imports principales
import os
import numpy as np

# --- Especificar backend ANTES de importar mlab ---
# Esto puede ayudar a inicializar correctamente la GUI
from mayavi import mlab
mlab.options.backend = 'qt' # Asegúrate de tener PyQt5 instalado (pip install pyqt5)
# -------------------------------------------------

import main   # Asegúrate de que main.py esté en el mismo directorio

# 2) Función para plot y guardado
def plot_radiation_pattern(l_rel_list):
    """
    Grafica y guarda los patrones 3D para cada L/λ en l_rel_list.
    Los guarda en la carpeta 'Imagenes3D/' como 'pattern_Lrel_<valor>.png'.
    """
    out_dir = "Imagenes3D"
    os.makedirs(out_dir, exist_ok=True)

    for l_rel in l_rel_list:
        # Obtener coordenadas del patrón
        x, y, z = main.calc_Rad_Dia(l_rel)

        # Crear figura Mayavi
        # Intenta crear la figura DESPUÉS de establecer el backend
        fig = mlab.figure(size=(800, 600), bgcolor=(1.0,0.39,0.28))
        mlab.mesh(x, y, z, colormap='viridis')
        mlab.title(f"Patrón 3D: L/λ = {l_rel:.2f}", size=0.4)
        mlab.axes(xlabel='X', ylabel='Y', zlabel='Z')
        mlab.orientation_axes()

        # Guardar como PNG
        filename = os.path.join(out_dir, f"pattern_Lrel_{l_rel:.2f}.png")
        mlab.savefig(filename)
        print(f"Guardado: {filename}")

        # Cerrar la figura para liberar memoria
        mlab.close(fig)

# 3) Ejecución principal
if __name__ == '__main__':
    print("Mostrando patrones de radiación 3D usando Mayavi...")
    try:
        L_relations = main.L_rels
    except AttributeError:
        raise RuntimeError("Error: main.py debe definir la variable L_rels (array de relaciones L/λ)")

    plot_radiation_pattern(L_relations)
    print("Todos los patrones guardados en 'Imagenes3D/'")
