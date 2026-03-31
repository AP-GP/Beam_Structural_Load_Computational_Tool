# -*- coding: utf-8 -*-
"""
    Generates shear force and bending moment distributions along the beam.

    The function discretises the beam into n points and incrementally 
    applies contributions from all load types to compute shear force (V) 
    and bending moment (M) at each position.

    Args:
        L (float): Beam length (m).
        RL (float): Reaction force at the left support (N).
        point_loads (list[PointLoad]): List of point loads.
        udls (list[UDL]): List of uniformly distributed loads.
        tdls (list[TDL]): List of triangular loads.
        zdls (list[ZDL]): List of trapezoidal loads.
        moments (list[Moment]): List of applied moments.
        n (int, optional): Number of discretisation points. Default is 2000.

    Returns:
        tuple:
            x (ndarray): Positions along the beam (m).
            V (ndarray): Shear force values (N).
            M (ndarray): Bending moment values (Nm).
    
    Author: Ayaan
"""


import numpy as np

def build_arrays(L, RL, point_loads, udls, tdls, zdls, moments, n=2000):
    x = np.linspace(0, L, n)
    V = np.full_like(x, RL)
    M = RL * x

    dx = x[1] - x[0]

    # Point loads
    for p in point_loads:
        mask = x >= p.x
        V[mask] -= p.F
        M[mask] -= p.F * (x[mask] - p.x)

    # UDL
    for u in udls:
        length = np.clip(x - u.a, 0, u.b - u.a)
        V -= u.w * length
        M -= u.w * length * (x - (u.a + length/2))

    # Triangular loads
    for t in tdls:
        denom = (t.x_peak - t.x_zero)
        if denom == 0:
            continue

        a = min(t.x_peak, t.x_zero)
        b = max(t.x_peak, t.x_zero)

        prog = np.clip((x - t.x_zero) / denom, 0, 1)
        w = t.w_peak * prog

        length = np.clip(x - a, 0, b - a)

        F = 0.5 * w * length
        V -= F

        xbar = a + length/2  # stable approx
        M -= F * (x - xbar)

    # Trapezoidal loads
    for z in zdls:
        denom = (z.x_max - z.x_min)
        if denom == 0:
            continue

        a = min(z.x_min, z.x_max)
        b = max(z.x_min, z.x_max)

        w = np.zeros_like(x)
        mask = (x >= a) & (x <= b)
        w[mask] = z.w_min + (z.w_max - z.w_min)*(x[mask]-z.x_min)/denom

        V -= w * dx
        M -= w * dx * (x - a)

    # Moments
    for m in moments:
        M[x >= m.x] += m.M

    return x, V, M

