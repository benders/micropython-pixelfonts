"""
pixelfonts Package

A package for bitmap fonts designed for microcontrollers and small displays.
"""

# Import main classes to make them available directly from the package
from .basefont import BaseFont
from .fonts.font3x5 import Font3x5
from .fonts.font4x7 import Font4x7

__version__ = "0.1.0"
__all__ = ['BaseFont', 'Font3x5', 'Font4x7']