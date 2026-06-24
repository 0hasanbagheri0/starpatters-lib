"""
الگوهای ریاضی و تزیینی
"""

import math
from typing import List, Tuple
from .core import Canvas, Pattern

def draw_grid(canvas: Canvas, spacing: int = 5, char: str = "+") -> Pattern:
    """رسم شبکه (Grid) با فاصله مشخص"""
    pattern = Pattern(canvas)
    
    for x in range(0, canvas.width, spacing):
        for y in range(0, canvas.height, spacing):
            pattern.add_point(x, y, char)
    
    return pattern

def draw_checkerboard(canvas: Canvas, size: int = 4, char1: str = "#", char2: str = " ") -> Pattern:
    """رسم صفحه شطرنجی"""
    pattern = Pattern(canvas)
    
    for y in range(0, canvas.height, size):
        for x in range(0, canvas.width, size):
            char = char1 if ((x // size) + (y // size)) % 2 == 0 else char2
            for i in range(size):
                for j in range(size):
                    if x + i < canvas.width and y + j < canvas.height:
                        pattern.add_point(x + i, y + j, char)
    
    return pattern

def draw_diagonal(canvas: Canvas, char: str = "/") -> Pattern:
    """رسم الگوی مورب (قطری)"""
    pattern = Pattern(canvas)
    
    for i in range(min(canvas.width, canvas.height)):
        pattern.add_point(i, i, char)
        pattern.add_point(canvas.width - 1 - i, i, char)
    
    return pattern

def draw_spiral(canvas: Canvas, cx: int, cy: int, max_radius: int, char: str = "*") -> Pattern:
    """رسم مارپیچ (Spiral)"""
    pattern = Pattern(canvas)
    
    for r in range(0, max_radius, 2):
        angle = r * 0.3
        x = int(cx + r * math.cos(angle))
        y = int(cy + r * math.sin(angle))
        pattern.add_point(x, y, char)
    
    return pattern
