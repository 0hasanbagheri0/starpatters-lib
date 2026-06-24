# StarPatterns-Lib

تجسم الگوهای ریاضی و گرافیکی در ترمینال با استفاده از کاراکترهای ASCII

[![PyPI version](https://badge.fury.io/py/starpatters-lib.svg)](https://badge.fury.io/py/starpatters-lib)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🌐 English | [فارسی](#فارسی)

---

# English Documentation

## 📁 StarPatterns-Lib

**StarPatterns-Lib** is a library for visualizing mathematical patterns, geometric shapes, and fractals in the terminal using ASCII characters. It's an excellent tool for teaching programming, mathematics, and creating text-based art.

### ✨ Key Features

- **Geometric Shapes**: Line, rectangle, circle, triangle
- **Decorative Patterns**: Grid, checkerboard, diagonal, spiral
- **Fractals**: Sierpinski triangle, Koch snowflake
- **Visual Effects**: Text coloring, screen clearing
- **No Dependencies**: Uses only Python standard library

---

### 📦 Installation

```bash
pip install starpatterns-lib
```
---

### 🚀 Quick Start
```bash
from starpatterns import Canvas, draw_circle, sierpinski_triangle, color_text
```
# Create a canvas
```bash
canvas = Canvas(60, 20)
```
# Draw a circle
```bash
circle = draw_circle(canvas, 30, 10, 8, "*")
circle.draw()
```
# Draw a fractal
```bash
canvas2 = Canvas(60, 20)
triangle = sierpinski_triangle(canvas2, 5, 18, 50, 3, "#")
triangle.draw()
```
# Colored text
```bash
print(color_text("StarPatterns-Lib", "blue", bold=True))
print(color_text("StarPatterns-Lib", "blue", bold=True))
```
---

### 📚 API Reference
# Canvas Class
|Method	|Description|
|:--- |:--- |
|Canvas(width, height, char)	|Create a new canvas|
|set_pixel(x, y, char)	|Set a pixel at position|
|get_pixel(x, y)	|Get pixel value at position|
|draw()	Display |the canvas in terminal|
|clear()	|Clear the canvas|
|fill(char)	|Fill entire canvas with a character|
# Shapes Functions
|Function	|Description|
|:--- |:--- |
|draw_line(canvas, x1, y1, x2, y2, char)	|Draw a line using Bresenham's algorithm|
|draw_rectangle(canvas, x, y, width, height, char)	|Draw a rectangle|
|draw_circle(canvas, cx, cy, radius, char)	|Draw a circle using midpoint algorithm|
|draw_triangle(canvas, x1, y1, x2, y2, x3, y3, char)	|Draw a triangle|
# Patterns Functions
|Function	|Description|
|:--- |:--- |
|draw_grid(canvas, spacing, char)	|Draw a grid pattern|
|draw_checkerboard(canvas, size, char1, char2)	|Draw a checkerboard pattern|
|draw_diagonal(canvas, char)	|Draw diagonal pattern|
|draw_spiral(canvas, cx, cy, max_radius, char)	|Draw a spiral pattern|
# Fractals Functions
|Function	|Description|
|:--- |:--- |
|sierpinski_triangle(canvas, x, y, size, depth, char)	|Draw Sierpinski triangle|
|koch_snowflake(canvas, x1, y1, x2, y2, depth, char)	|Draw Koch snowflake|
# Utility Functions
|Function	|Description|
|:--- |:--- |
|clear_screen()	|Clear the terminal screen|
|color_text(text, color, bold)	|Colorize text in terminal|
|get_terminal_size()	|Get terminal dimensions|

---

# 🛠️ Requirements
##  Python 3.7 or higher

##  No external dependencies

---

### 🤝 Contributing
We welcome contributions! Please:

1.Fork the repository

2.Create a new branch (``` git checkout -b feature/amazing-feature ```)

3.Commit your changes (``` git commit -m 'Add amazing feature' ```)

4.Push to the branch (``` git push origin feature/amazing-feature ```)

5.Open a Pull Request
---
# 📄 License
This project is licensed under the MIT License.
---
# 📧 Contact
 Email: hasan111bagher@gmail.com

 GitHub: https://github.com/0hasanbagheri0
---
---
## 🌐 فارسی  |   [English](#English)

# 📁 StarPatterns-Lib
 StarPatterns-Lib کتابخانه‌ای برای تجسم الگوهای ریاضی، اشکال هندسی و فراکتال‌ها در ترمینال با استفاده از کاراکترهای ASCII است. ابزاری عالی برای آموزش برنامه‌نویسی، ریاضیات و خلق آثار هنری متنی.
---
### ✨ ویژگی‌ها
 اشکال هندسی: خط، مستطیل، دایره، مثلث

 الگوهای تزیینی: شبکه، شطرنجی، مورب، مارپیچ

 فراکتال‌ها: مثلث سیرپینسکی، دانه برف کخ

 جلوه‌های بصری: رنگ‌آمیزی متن، پاک کردن صفحه

 بدون وابستگی: فقط با ماژول‌های استاندارد پایتون
---
### 📦 نصب

```bash
pip install starpatterns-lib
```
---

# 🚀 شروع سریع

```bash
from starpatterns import Canvas, draw_circle, sierpinski_triangle, color_text
```

# ایجاد بوم

```bash
canvas = Canvas(60, 20)
```

# رسم دایره

```bash
circle = draw_circle(canvas, 30, 10, 8, "*")
circle.draw()
```

# رسم فراکتال

```bash
canvas2 = Canvas(60, 20)
triangle = sierpinski_triangle(canvas2, 5, 18, 50, 3, "#")
triangle.draw()
```

# متن رنگی

```bash
print(color_text("StarPatterns-Lib", "blue", bold=True))
```

## 📚 راهنمای توابع

# کلاس Canvas

|توضیح|تابع 
|:---|:---|
|Canvas(width, height, char)|	ایجاد بوم جدید|
|set_pixel(x, y, char)|	تنظیم یک پیکسل در موقعیت مشخص|
|get_pixel(x, y)	|دریافت مقدار پیکسل در موقعیت مشخص|
|draw()	|نمایش بوم در ترمینال|
|clear()|	پاک کردن بوم|
|fill(char)	|پر کردن کل بوم با یک کاراکتر|

# توابع اشکال

|تابع	|توضیح|
|:---|:---|
|draw_line(canvas, x1, y1, x2, y2, char)	|رسم خط با الگوریتم برزنهام|
|draw_rectangle(canvas, x, y, width, height, char)	|رسم مستطیل|
|draw_circle(canvas, cx, cy, radius, char)	|رسم دایره با الگوریتم نقطه‌میانی|
|draw_triangle(canvas, x1, y1, x2, y2, x3, y3, char)|	رسم مثلث|

# توابع الگوها

|تابع	|توضیح|
|:---|:---|
|draw_grid(canvas, spacing, char)	|رسم شبکه|
|draw_checkerboard(canvas, size, char1, char2)|	رسم صفحه شطرنجی|
|draw_diagonal(canvas, char)	|رسم الگوی مورب|
|draw_spiral(canvas, cx, cy, max_radius, char)	|رسم مارپیچ|

# توابع فراکتال

|تابع	|توضیح|
|:---|:---|
sierpinski_triangle(canvas, x, y, size, depth, char)	|رسم مثلث سیرپینسکی|
koch_snowflake(canvas, x1, y1, x2, y2, depth, char)	|رسم دانه برف کخ|

# توابع کمکی

|تابع	|توضیح|
|:---|:---|
|clear_screen()	|پاک کردن صفحه ترمینال|
|color_text(text, color, bold)|	رنگ‌آمیزی متن در ترمینال|
|get_terminal_size()	|دریافت اندازه ترمینال|

---
# 🛠️ نیازمندی‌ها

Python 3.7 یا بالاتر

بدون وابستگی‌های خارجی 
---
# 🤝 مشارکت

از مشارکت شما استقبال می‌کنیم! لطفاً :

1.مخزن را Fork کنید

2.یک شاخه جدید بسازید (``` git checkout -b feature/amazing-feature ```)

3.تغییرات را Commit کنید (``` git commit -m 'Add amazing feature' ```)

4.به شاخه خود Push کنید (``` git push origin feature/amazing-feature ```)

5.یک Pull Request باز کنید

---
# 📄 مجوز
این پروژه تحت مجوز MIT منتشر شده است.
---
# 📧 ارتباط با من
ایمیل:
hasan111bagher@gmail.com

گیت‌هاب:
https://github.com/0hasanbagheri0
---
### ✨ اگر این کتابخانه برای شما مفید بود، به آن یک ⭐ در گیت‌هاب بدهید!
------
