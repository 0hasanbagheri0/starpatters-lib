"""
کلاس‌های اصلی برای ایجاد الگوها
"""

import os
import sys
import time
from typing import List, Tuple, Optional

class Canvas:
    """بوم (Canvas) برای رسم الگوها"""
    
    def __init__(self, width: int = 80, height: int = 24, char: str = " "):
        self.width = width
        self.height = height
        self.char = char
        self.grid = [[char for _ in range(width)] for _ in range(height)]
    
    def set_pixel(self, x: int, y: int, char: str):
        """تنظیم یک پیکسل در مختصات مشخص"""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = char
    
    def get_pixel(self, x: int, y: int) -> str:
        """دریافت مقدار یک پیکسل"""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return self.char
    
    def draw(self):
        """چاپ کل بوم در ترمینال"""
        print("\n".join("".join(row) for row in self.grid))
    
    def clear(self):
        """پاک کردن بوم"""
        self.grid = [[self.char for _ in range(self.width)] for _ in range(self.height)]
    
    def fill(self, char: str):
        """پر کردن کل بوم با یک کاراکتر"""
        self.grid = [[char for _ in range(self.width)] for _ in range(self.height)]

class Pattern:
    """کلاس پایه برای ایجاد الگوهای ریاضی"""
    
    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self.points = []
    
    def draw(self):
        """رسم الگو روی بوم"""
        for x, y, char in self.points:
            self.canvas.set_pixel(x, y, char)
    
    def add_point(self, x: int, y: int, char: str = "*"):
        """افزودن یک نقطه به الگو"""
        self.points.append((x, y, char))
    
    def clear(self):
        """پاک کردن نقاط الگو"""
        self.points = []
