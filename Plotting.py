# -*- coding: utf-8 -*-
"""

    This module handles the visualisation of structural analysis results. 
    It generates Shear Force Diagrams (SFD) and Bending Moment Diagrams (BMD) 
    based on computed data from the solver.

    The plotting functions are designed to produce clear, engineering-style 
    graphs with consistent formatting, including gridlines, axis styling, 
    and shaded regions for improved interpretability.
    
    Args:
    x (ndarray): Positions along the beam (m).
    V (ndarray): Shear force values (N).
    M (ndarray): Bending moment values (Nm).

    Matplotlib is used for all visual output.
    
    Author: Ayaan
"""

import matplotlib.pyplot as plt

def plot_results(x, V, M):
    """
    Plots Shear Force and Bending Moment Diagrams.
    """

    plt.rcParams['axes.edgecolor'] = 'black'
    plt.rcParams['axes.linewidth'] = 1.5
    plt.rcParams['xtick.color'] = 'black'
    plt.rcParams['ytick.color'] = 'black'

    plt.figure()

    # Shear
    plt.subplot(2,1,1)
    plt.plot(x, V)
    plt.fill_between(x, V, 0, color='lightgrey', hatch='//',
                     edgecolor='black', linewidth=0.0)
    plt.axhline(0)
    plt.title("Shear Force Diagram")
    plt.xlabel("Position (m)")
    plt.ylabel("Shear (N)")
    plt.grid(True, linestyle='--', linewidth=0.5)

    # Moment
    plt.subplot(2,1,2)
    plt.plot(x, M)
    plt.fill_between(x, M, 0, color='lightgrey', hatch='\\\\',
                     edgecolor='black', linewidth=0.0)
    plt.axhline(0)
    plt.title("Bending Moment Diagram")
    plt.xlabel("Position (m)")
    plt.ylabel("Moment (Nm)")
    plt.grid(True, linestyle='--', linewidth=0.5)

    plt.tight_layout()
    plt.show()