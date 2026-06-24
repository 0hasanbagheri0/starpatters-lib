"""
StarPatterns-Lib - تجسم الگوهای ریاضی در ترمینال
"""

from .core import Canvas, Pattern
from .shapes import draw_line, draw_rectangle, draw_circle, draw_triangle
from .patterns import draw_grid, draw_checkerboard, draw_diagonal, draw_spiral
from .fractals import sierpinski_triangle, koch_snowflake
from .utils import clear_screen, color_text

__version__ = "0.1.0"
__all__ = [
    "Canvas",
    "Pattern",
    "draw_line",
    "draw_rectangle",
    "draw_circle",
    "draw_triangle",
    "draw_grid",
    "draw_checkerboard",
    "draw_diagonal",
    "draw_spiral",
    "sierpinski_triangle",
    "koch_snowflake",
    "clear_screen",
    "color_text"
]
