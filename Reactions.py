# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:22:21 2026

@author: ayaan
"""

def reactions(L, point_loads, udls, tdls, zdls, moments):
    total_F = 0
    total_M = 0

    # Point loads
    for p in point_loads:
        total_F += p.F
        total_M += p.F * p.x

    # UDL
    for u in udls:
        length = u.b - u.a
        F = u.w * length
        xbar = (u.a + u.b) / 2
        total_F += F
        total_M += F * xbar

    # Triangular
    for t in tdls:
        base = abs(t.x_peak - t.x_zero)
        F = 0.5 * t.w_peak * base
        xbar = (2*t.x_peak + t.x_zero)/3
        total_F += F
        total_M += F * xbar

    # Trapezoidal
    for z in zdls:
        base = abs(z.x_max - z.x_min)

        F_rect = z.w_min * base
        x_rect = (z.x_min + z.x_max)/2

        F_tri = 0.5 * (z.w_max - z.w_min) * base
        x_tri = (2*z.x_max + z.x_min)/3

        total_F += F_rect + F_tri
        total_M += F_rect * x_rect + F_tri * x_tri

    # Moments
    for m in moments:
        total_M += m.M

    RR = total_M / L
    RL = total_F - RR

    return RL, RR

