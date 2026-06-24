# StarPatterns-Lib

تجسم الگوهای ریاضی و گرافیکی در ترمینال با استفاده از کاراکترهای ASCII

[![PyPI version](https://badge.fury.io/py/starpatters-lib.svg)](https://badge.fury.io/py/starpatters-lib)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📁 StarPatterns-Lib

کتابخانه‌ای برای تجسم الگوهای ریاضی و گرافیکی در ترمینال با استفاده از کاراکترهای ASCII.

## ✨ ویژگی‌ها

- **اشکال هندسی**: خط، مستطیل، دایره، مثلث
- **الگوهای تزیینی**: شبکه، شطرنجی، مورب، مارپیچ
- **فراکتال‌ها**: مثلث سیرپینسکی، دانه برف کخ
- **جلوه‌های بصری**: رنگ‌آمیزی متن، پاک کردن صفحه

## 📦 نصب

```bash
pip install starpatterns-lib

```
# 🚀 شروع سریع

python
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

# نمایش با رنگ
```bash
print(color_text("StarPatterns-Lib", "blue", bold=True))
```
# 📄 مجوز
MIT
