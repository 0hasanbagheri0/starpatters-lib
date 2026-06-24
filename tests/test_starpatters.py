"""
تست جامع کتابخانه StarPatterns-Lib
"""

import time
from starpatterns import (
    Canvas, 
    draw_line, draw_rectangle, draw_circle, draw_triangle,
    draw_grid, draw_checkerboard, draw_diagonal, draw_spiral,
    sierpinski_triangle, koch_snowflake,
    clear_screen, color_text
)

def test_shapes():
    """تست اشکال هندسی"""
    print(color_text("\n=== تست اشکال هندسی ===", "cyan", bold=True))
    
    canvas = Canvas(60, 20)
    
    # خط
    line = draw_line(canvas, 2, 2, 50, 15, "*")
    line.draw()
    print(color_text("✅ خط با الگوریتم برزنهام", "green"))
    input("Enter برای ادامه...")
    
    # مستطیل
    canvas.clear()
    rect = draw_rectangle(canvas, 10, 5, 30, 10, "#")
    rect.draw()
    print(color_text("✅ مستطیل", "green"))
    input("Enter برای ادامه...")
    
    # دایره
    canvas.clear()
    circle = draw_circle(canvas, 30, 10, 8, "@")
    circle.draw()
    print(color_text("✅ دایره با الگوریتم نقطه‌میانی", "green"))
    input("Enter برای ادامه...")
    
    # مثلث
    canvas.clear()
    triangle = draw_triangle(canvas, 5, 18, 30, 2, 55, 18, "^")
    triangle.draw()
    print(color_text("✅ مثلث", "green"))
    input("Enter برای ادامه...")

def test_patterns():
    """تست الگوهای تزیینی"""
    print(color_text("\n=== تست الگوهای تزیینی ===", "cyan", bold=True))
    
    canvas = Canvas(60, 20)
    
    # شبکه
    grid = draw_grid(canvas, 5, "+")
    grid.draw()
    print(color_text("✅ شبکه (Grid)", "green"))
    input("Enter برای ادامه...")
    
    # شطرنجی
    canvas.clear()
    checker = draw_checkerboard(canvas, 4, "#", ".")
    checker.draw()
    print(color_text("✅ صفحه شطرنجی", "green"))
    input("Enter برای ادامه...")
    
    # مورب
    canvas.clear()
    diag = draw_diagonal(canvas, "/")
    diag.draw()
    print(color_text("✅ الگوی مورب", "green"))
    input("Enter برای ادامه...")
    
    # مارپیچ
    canvas.clear()
    spiral = draw_spiral(canvas, 30, 10, 20, "*")
    spiral.draw()
    print(color_text("✅ مارپیچ", "green"))
    input("Enter برای ادامه...")

def test_fractals():
    """تست فراکتال‌ها"""
    print(color_text("\n=== تست فراکتال‌ها ===", "cyan", bold=True))
    
    # مثلث سیرپینسکی
    canvas = Canvas(60, 20)
    print(color_text("در حال رسم مثلث سیرپینسکی (عمق ۳)...", "yellow"))
    triangle = sierpinski_triangle(canvas, 5, 18, 50, 3, "#")
    triangle.draw()
    print(color_text("✅ مثلث سیرپینسکی", "green"))
    input("Enter برای ادامه...")
    
    # دانه برف کخ
    canvas.clear()
    print(color_text("در حال رسم دانه برف کخ (عمق ۳)...", "yellow"))
    snowflake = koch_snowflake(canvas, 5, 15, 55, 15, 3, "*")
    snowflake.draw()
    print(color_text("✅ دانه برف کخ", "green"))
    input("Enter برای ادامه...")

def test_utils():
    """تست توابع کمکی"""
    print(color_text("\n=== تست توابع کمکی ===", "cyan", bold=True))
    
    # رنگ‌آمیزی
    print(color_text("متن قرمز", "red"))
    print(color_text("متن سبز", "green"))
    print(color_text("متن زرد", "yellow"))
    print(color_text("متن آبی", "blue"))
    print(color_text("متن بنفش", "magenta"))
    print(color_text("متن فیروزه‌ای", "cyan"))
    print(color_text("متن پررنگ سفید", "white", bold=True))
    
    print(color_text("✅ رنگ‌آمیزی متن با ۷ رنگ مختلف", "green"))
    input("Enter برای ادامه...")
    
    # پاک کردن صفحه
    print(color_text("در ۳ ثانیه صفحه پاک می‌شود...", "yellow"))
    time.sleep(3)
    clear_screen()
    print(color_text("✅ صفحه پاک شد!", "green"))

def main():
    """اجرای همه تست‌ها"""
    clear_screen()
    print(color_text("="*50, "cyan", bold=True))
    print(color_text("   تست جامع StarPatterns-Lib", "cyan", bold=True))
    print(color_text("="*50, "cyan", bold=True))
    print()
    
    try:
        test_shapes()
        test_patterns()
        test_fractals()
        test_utils()
        
        print(color_text("\n" + "="*50, "green", bold=True))
        print(color_text("✅ همه تست‌ها با موفقیت انجام شدند!", "green", bold=True))
        print(color_text("="*50, "green", bold=True))
        
    except KeyboardInterrupt:
        print(color_text("\n⚠️ تست توسط کاربر متوقف شد", "yellow"))
    except Exception as e:
        print(color_text(f"\n❌ خطا: {e}", "red"))

if __name__ == "__main__":
    main()