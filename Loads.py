# -*- coding: utf-8 -*-
"""
    This module defines data structures representing different types of loads 
    that can be applied to a beam. Each load type is implemented as a dataclass 
    to provide a clear and structured representation of its physical properties.

    Supported load types:
        - PointLoad: Concentrated force at a specific position
        - UDL: Uniformly distributed load over a given interval
        - TDL: Triangular distributed load with varying intensity
        - ZDL: Trapezoidal distributed load with linear variation
        - Moment: Applied point moment

    These classes are used throughout the analysis and solver modules to 
    standardise load input and simplify force and moment calculations.
    
    Author: Ayaan
"""


from dataclasses import dataclass

@dataclass
class PointLoad:
    """
    Represents a concentrated point load.

    Attributes:
        F (float): Magnitude of the load (N).
        x (float): Position along the beam (m).
    """
    F: float
    x: float
    
@dataclass
class UDL:
    """
    Represents a uniformly distributed load.

    Attributes:
        w (float): Load intensity (N/m).
        a (float): Start position (m).
        b (float): End position (m).
    """
    w: float
    a: float
    b: float

@dataclass
class TDL:
    """
    Represents a triangular distributed load.

    Attributes:
        w_peak (float): Peak load intensity (N/m).
        x_peak (float): Position of peak intensity (m).
        x_zero (float): Position where load reduces to zero (m).
    """
    w_peak: float
    x_peak: float
    x_zero: float

@dataclass
class ZDL:
    """
    Represents a trapezoidal distributed load.

    Attributes:
        w_max (float): Maximum load intensity (N/m).
        w_min (float): Minimum load intensity (N/m).
        x_max (float): Position of maximum intensity (m).
        x_min (float): Position of minimum intensity (m).
    """
    w_max: float
    w_min: float
    x_max: float
    x_min: float

@dataclass
class Moment:
    """
    Represents an applied point moment.

    Attributes:
        M (float): Moment magnitude (Nm).
        x (float): Position along the beam (m).
    """
    M: float
    x: float