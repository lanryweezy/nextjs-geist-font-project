"""
E8Leech: A comprehensive framework for E8 and Leech lattices with applications in cryptography, AI, and quantum computing.

This package provides mathematically rigorous implementations of the E8 and Leech lattices,
along with optimized algorithms for lattice operations, quantum-safe cryptographic protocols,
and AI applications.
"""

__version__ = "0.1.0"
__author__ = "E8Leech Framework Team"

from .lattices.e8 import E8Lattice
from .lattices.leech import LeechLattice

__all__ = ["E8Lattice", "LeechLattice"]
