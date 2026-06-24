"""
الگوهای فراکتال
"""

import math
from typing import List, Tuple
from .core import Canvas, Pattern
from .shapes import draw_line, draw_triangle

def sierpinski_triangle(canvas: Canvas, x: int, y: int, size: int, depth: int, char: str = "*") -> Pattern:
    """رسم مثلث سیرپینسکی"""
    pattern = Pattern(canvas)
    
    if depth == 0:
        triangle = draw_triangle(canvas, x, y, x + size, y, x + size//2, y - size, char)
        for point in triangle.points:
            pattern.add_point(point[0], point[1], char)
    else:
        half = size // 2
        sub1 = sierpinski_triangle(canvas, x, y, half, depth - 1, char)
        sub2 = sierpinski_triangle(canvas, x + half, y, half, depth - 1, char)
        sub3 = sierpinski_triangle(canvas, x + half//2, y - half, half, depth - 1, char)
        
        for p in sub1.points + sub2.points + sub3.points:
            pattern.add_point(p[0], p[1], char)
    
    return pattern

def koch_snowflake(canvas: Canvas, x1: int, y1: int, x2: int, y2: int, depth: int, char: str = "*") -> Pattern:
    """رسم دانه برف کخ"""
    pattern = Pattern(canvas)
    
    if depth == 0:
        line = draw_line(canvas, x1, y1, x2, y2, char)
        for point in line.points:
            pattern.add_point(point[0], point[1], char)
    else:
        dx = x2 - x1
        dy = y2 - y1
        
        x3 = x1 + dx // 3
        y3 = y1 + dy // 3
        
        x4 = x1 + 2 * dx // 3
        y4 = y1 + 2 * dy // 3
        
        angle = math.radians(60)
        x5 = x3 + int((x4 - x3) * math.cos(angle) - (y4 - y3) * math.sin(angle))
        y5 = y3 + int((x4 - x3) * math.sin(angle) + (y4 - y3) * math.cos(angle))
        
        for segment in [
            (x1, y1, x3, y3),
            (x3, y3, x5, y5),
            (x5, y5, x4, y4),
            (x4, y4, x2, y2)
        ]:
            sub = koch_snowflake(canvas, segment[0], segment[1], segment[2], segment[3], depth - 1, char)
            for point in sub.points:
                pattern.add_point(point[0], point[1], char)
    
    return pattern
