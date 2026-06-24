"""
رسم اشکال هندسی پایه
"""

import math
from typing import List, Tuple, Optional
from .core import Canvas, Pattern

def draw_line(canvas: Canvas, x1: int, y1: int, x2: int, y2: int, char: str = "*") -> Pattern:
    """رسم خط با الگوریتم برزنهام"""
    pattern = Pattern(canvas)
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    
    x, y = x1, y1
    
    while True:
        pattern.add_point(x, y, char)
        if x == x2 and y == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
    
    return pattern

def draw_rectangle(canvas: Canvas, x: int, y: int, width: int, height: int, char: str = "*") -> Pattern:
    """رسم مستطیل"""
    pattern = Pattern(canvas)
    
    for i in range(width):
        pattern.add_point(x + i, y, char)
        pattern.add_point(x + i, y + height - 1, char)
    
    for i in range(height):
        pattern.add_point(x, y + i, char)
        pattern.add_point(x + width - 1, y + i, char)
    
    return pattern

def draw_circle(canvas: Canvas, cx: int, cy: int, radius: int, char: str = "*") -> Pattern:
    """رسم دایره با الگوریتم نقطه‌میانی"""
    pattern = Pattern(canvas)
    
    x = 0
    y = radius
    d = 3 - 2 * radius
    
    while x <= y:
        pattern.add_point(cx + x, cy + y, char)
        pattern.add_point(cx - x, cy + y, char)
        pattern.add_point(cx + x, cy - y, char)
        pattern.add_point(cx - x, cy - y, char)
        pattern.add_point(cx + y, cy + x, char)
        pattern.add_point(cx - y, cy + x, char)
        pattern.add_point(cx + y, cy - x, char)
        pattern.add_point(cx - y, cy - x, char)
        
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1
    
    return pattern

def draw_triangle(canvas: Canvas, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, char: str = "*") -> Pattern:
    """رسم مثلث با سه نقطه"""
    pattern = Pattern(canvas)
    
    line1 = draw_line(canvas, x1, y1, x2, y2, char)
    line2 = draw_line(canvas, x2, y2, x3, y3, char)
    line3 = draw_line(canvas, x3, y3, x1, y1, char)
    
    for point in line1.points + line2.points + line3.points:
        pattern.add_point(point[0], point[1], char)
    
    return pattern
