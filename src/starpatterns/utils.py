"""
توابع کمکی برای نمایش و جلوه‌های بصری
"""

import os
import time
import sys

def clear_screen():
    """پاک کردن صفحه ترمینال"""
    os.system('cls' if os.name == 'nt' else 'clear')

def color_text(text: str, color: str = "white", bold: bool = False) -> str:
    """
    رنگ‌آمیزی متن در ترمینال
    
    Args:
        text: متن مورد نظر
        color: رنگ (red, green, yellow, blue, magenta, cyan, white)
        bold: پررنگ یا نه
    """
    colors = {
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "magenta": 35,
        "cyan": 36,
        "white": 37
    }
    
    code = colors.get(color, 37)
    bold_code = 1 if bold else 0
    return f"\033[{bold_code};{code}m{text}\033[0m"

def get_terminal_size() -> tuple:
    """دریافت اندازه ترمینال"""
    try:
        import shutil
        cols, rows = shutil.get_terminal_size()
        return cols, rows
    except:
        return 80, 24
