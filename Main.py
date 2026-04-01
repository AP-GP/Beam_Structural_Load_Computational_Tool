# -*- coding: utf-8 -*-
"""
    Main execution function for user interaction and analysis workflow.

    Prompts the user to define beam geometry and loading conditions, 
    computes reactions, generates shear force and bending moment data, 
    and visualises the results using plots.

    Outputs:
        - Reaction forces at supports
        - Maximum and minimum shear force values
        - Maximum and minimum bending moment 
        - Location of Zero Shear Force
        - SFD and BMD plots
    
    Author: Ayaan
"""

from Loads import PointLoad, UDL, TDL, ZDL, Moment
from Reactions import reactions
from Arrays import build_arrays
from Plotting import plot_results
import numpy as np

def main():
    L = float(input("Beam length (m): "))

    point_loads, udls, tdls, zdls, moments = [], [], [], [], []

    while True:
        choice = input(
            "\n1) Point 2) UDL 3) Triangular 4) Trapezoidal 5) Moment 6) Done: "
        )

        if choice == "1":
            F = float(input("Force (N): "))
            x = float(input("Position (m) from left Support: "))
            point_loads.append(PointLoad(F, x))

        elif choice == "2":
            w = float(input("Intensity (N/m): "))
            a = float(input("Start Position (m) from Left Support: "))
            b = float(input("End Position (m) from left Support: "))
            udls.append(UDL(w, a, b))

        elif choice == "3":
            w_peak = float(input("Peak (N/m): "))
            x_peak = float(input("Peak position (m) from Left Support: "))
            x_zero = float(input("Zero position (m) from Left Support: "))
            tdls.append(TDL(w_peak, x_peak, x_zero))

        elif choice == "4":
            w_max = float(input("Max intensity (N/m): "))
            w_min = float(input("Min intensity (N/m): "))
            x_max = float(input("Max position (m) from Left Support:"))
            x_min = float(input("Min position (m) from Left Support: "))
            zdls.append(ZDL(w_max, w_min, x_max, x_min))

        elif choice == "5":
            Mval = float(input("Moment (Nm): Enter clockwise as positive" 
                               "and anticlockwise as negative"))
            x = float(input("Position (m) from Left Support: "))
            moments.append(Moment(Mval, x))

        elif choice == "6":
            break

    RL, RR = reactions(L, point_loads, udls, tdls, zdls, moments)
    x, V, M = build_arrays(L, RL, point_loads, udls, tdls, zdls, moments)
    
    #Zero Shear Force Crossing Analysis
    zero_crossings = []

    for i in range(len(V)-1):
        if V[i] == 0:
            zero_crossings.append(x[i])
        elif V[i] * V[i+1] < 0:
        # linear interpolation for better accuracy
            x0 = x[i] - V[i] * (x[i+1] - x[i]) / (V[i+1] - V[i])
            zero_crossings.append(x0)
    
    # Max / Min
    i_maxV = np.argmax(V)
    i_minV = np.argmin(V)

    i_maxM = np.argmax(M)
    i_minM = np.argmin(M)

    print("\nReactions:")
    print(f"RL = {RL:.2f} N, RR = {RR:.2f} N")

    print("\nShear:")
    print(f"Max = {V[i_maxV]:.2f} at x = {x[i_maxV]:.2f}")
    print(f"Min = {V[i_minV]:.2f} at x = {x[i_minV]:.2f}")

    print("\nZero Shear Locations (V = 0):")
    for z in zero_crossings:
        print(f"x = {z:.2f} m")

    print("\nMoment:")
    print(f"Max = {round(M[i_maxM],1):.2f} at x = {x[i_maxM]:.2f}")
    print(f"Min = {round(M[i_minM],1):.2f} at x = {x[i_minM]:.2f}")

    plot_results(x, V, M)


if __name__ == "__main__":
    main()
