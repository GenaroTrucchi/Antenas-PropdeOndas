#!/usr/bin/env python3
import pyvista as pv
from pyvista import Plotter
import main  # tu módulo con calc_Rad_Dia y L_rels

# 1) Desactivar modo off-screen (no usar start_xvfb en Windows)
pv.OFF_SCREEN = False

def visualize():
    for l_rel in main.L_rels:
        # Calcula la malla
        x, y, z = main.calc_Rad_Dia(l_rel)
        grid = pv.StructuredGrid(x, y, z)

        # 2) Crear plotter con GUI activo
        pl = Plotter(off_screen=False)
        pl.add_mesh(grid, color="lightblue", show_edges=False)
        pl.add_mesh(grid, color="tomato")
        pl.add_axes()
        pl.add_title(f"Patrón 3D: L/λ = {l_rel:.2f}")

        # 3) Muestra la ventana interactiva
        pl.show()

if __name__ == "__main__":
    print("Iniciando visualización con PyVista…")
    visualize()

