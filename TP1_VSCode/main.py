#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.py  —  Genera diagramas de radiación 2D y 3D
USO: python main.py
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Parámetros globales ---
# Array de relaciones L/λ a graficar
L_rels = np.array([1/8, 1/4, 1/2, 3/4, 5/4, 3/2, 7/4, 2, 9/4])

# Mallas angulares
phi   = np.linspace(0, 2*np.pi, 200)
theta = np.linspace(1e-3, np.pi-1e-3, 100)  # evito división por cero
phi_m, theta_m = np.meshgrid(phi, theta)

# Carpeta de salida
OUT2D = "Imagenes2D"
OUT3D = "Imagenes3D"
os.makedirs(OUT2D, exist_ok=True)
os.makedirs(OUT3D, exist_ok=True)


def calc_Rad_Dia(l_rel):
    """
    Calcula x,y,z para el diagrama 3D dado l = L/λ.
    Fórmula: r(θ) = [cos(π l cosθ) – cos(π l)] / sinθ
    """
    r = (np.cos(np.pi * l_rel * np.cos(theta_m)) - np.cos(np.pi * l_rel)) / np.sin(theta_m)
    x = r * np.sin(theta_m) * np.cos(phi_m)
    y = r * np.sin(theta_m) * np.sin(phi_m)
    z = r * np.cos(theta_m)
    return x, y, z


def calc_Plane_RD(l_rel):
    """
    Calcula x(θ), z(θ) para el corte planar en φ=0 y φ=π.
    """
    # Generamos plano φ=0 y π
    phi_plane = np.array([0, np.pi])
    theta_plane = theta
    phi_p, theta_p = np.meshgrid(phi_plane, theta_plane)
    r = (np.cos(np.pi * l_rel * np.cos(theta_p)) - np.cos(np.pi * l_rel)) / np.sin(theta_p)
    x = r * np.sin(theta_p) * np.cos(phi_p)
    z = r * np.cos(theta_p)
    return x, z


def plot_and_save_3d(x, y, z, l_rel):
    fig = plt.figure(figsize=(6,5))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
    ax.set_title(f"Diagrama 3D, L/λ = {l_rel:.2f}")
    ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
    plt.tight_layout()
    fname = os.path.join(OUT3D, f"3D_Lrel_{l_rel:.2f}.png")
    plt.savefig(fname, dpi=150)
    plt.close(fig)


def plot_and_save_2d(x, z, l_rel):
    plt.figure(figsize=(6,4))
    for col in range(x.shape[1]):
        plt.plot(x[:,col], z[:,col], lw=1.5)
    plt.title(f"Diagrama 2D plano, L/λ = {l_rel:.2f}")
    plt.xlabel("X"); plt.ylabel("Z")
    plt.grid(True)
    plt.tight_layout()
    fname = os.path.join(OUT2D, f"2D_Lrel_{l_rel:.2f}.png")
    plt.savefig(fname, dpi=150)
    plt.close()


def main():
    print("Generando diagramas de radiación para L/λ:", L_rels)
    for l in L_rels:
        x3, y3, z3 = calc_Rad_Dia(l)
        plot_and_save_3d(x3, y3, z3, l)
        
        x2, z2 = calc_Plane_RD(l)
        plot_and_save_2d(x2, z2, l)
    print("¡Listo! Revisá las carpetas Imagenes2D e Imagenes3D")

if __name__ == "__main__":
    main()
input("Presioná ENTER para terminar")