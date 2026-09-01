

یک وب‌اپلیکیشن فروشگاهی (E-commerce) ساخته‌شده با **Django**.

> توضیح: این پروژه شامل بخش‌های مدیریت حساب کاربری، نمایش محصولات و فروشگاه آنلاین است.

## ✨ ویژگی‌ها

- 👤 مدیریت حساب کاربری (ثبت‌نام / ورود) — `account`
- 🛍️ نمایش و مدیریت محصولات — `products`
- 🛒 فروشگاه آنلاین — `shop`
- 🖼️ رسانه‌ها و تصاویر محصولات — `media/products`
- 🎨 قالب‌های HTML — `template`
- 📁 فایل‌های استاتیک (CSS/JS) — `static`

## 📂 ساختار پروژه

```
game2/
├── account/          # اپ مدیریت کاربران
├── config/           # تنظیمات اصلی پروژه‌ی Django
├── products/         # اپ محصولات
├── shop/             # اپ فروشگاه
├── static/           # فایل‌های استاتیک
├── template/         # قالب‌های HTML
├── media/products/   # تصاویر آپلود‌شده‌ی محصولات
├── manage.py
└── db.sqlite3
```

## ⚙️ پیش‌نیازها

- Python 3.x
- Django
- (در صورت وجود، سایر پکیج‌های داخل `requirements.txt`)

## 🚀 نصب و اجرا

```bash
# کلون کردن پروژه
git clone https://github.com/AmirAbbas908/game2.git
cd game2

# ساخت محیط مجازی (اختیاری ولی پیشنهادی)
python -m venv venv
source venv/bin/activate      # در ویندوز: venv\Scripts\activate

# نصب پکیج‌ها
pip install -r requirements.txt

# اجرای مایگریشن‌ها
python manage.py migrate

# اجرای سرور توسعه
python manage.py runserver
```

سپس در مرورگر به آدرس زیر بروید:

```
http://127.0.0.1:8000/
```




