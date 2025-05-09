# 📊 Konkur Performance Reporter

**A sleek, fully Persian-supported desktop app for tracking, analyzing, and visualizing your Iranian Konkur exam results.**

---

## 🌟 Features

✅ **Enter Exam Data**
Input the number of questions, correct, incorrect, and unanswered items for each key subject:
`آمار و احتمال (Statistics & Probability), حسابان (Calculus), هندسه (Geometry), فیزیک (Physics), شیمی (Chemistry)`

✅ **Weighted Score Calculation**
Calculates your overall weighted percentage based on official subject weightings.

✅ **History Tracking**
All exam data is saved in `exam_results.json`, preserving your full test history.

✅ **Performance Visualization**
Interactive charts: line plots showing your overall trend and pie charts breaking down each test and subject.

✅ **Fully Persian-Friendly**
Handles right-to-left text, reshapes Arabic/Persian scripts, and displays Persian digits beautifully on charts.

✅ **Clean PyQt5 GUI**
User-friendly interface designed for easy data entry and powerful performance review.

---

## 💻 Installation

Make sure you have **Python 3.x** installed. Then, install the required libraries:

```bash
pip install PyQt5 matplotlib arabic_reshaper python-bidi
```

---

## 🚀 How to Run

```bash
python Script2.py
```

This will launch the desktop application. You can:

* **Add a new exam**: Fill in the number of questions, correct, and incorrect answers per subject.
* **View performance**: See your past exam scores, analyze trends, and inspect detailed per-subject stats.

All your exam data is saved locally in the file `exam_results.json`.

---

## 📂 Project Structure

```
📦 KonkurPerformanceReporter
├── Script2.py             # Main Python script (PyQt5 app)
├── exam_results.json      # JSON file storing all test data
└── README.md              # You're reading it!
```

---

## 📈 Screenshots (Optional)

*Here, you can add screenshots or GIFs showing the app in action.*

---

## 🛡 Future Improvements

* Add public/general subjects (e.g., Persian literature, Arabic, Religion)
* Export printable PDF report cards
* Cloud sync or backup of exam data
* Advanced analytics (weakness analysis, improvement suggestions)

---

## 📜 License

This project is open-source. Feel free to fork, improve, and share it (just give credit where credit's due 😉).

---

# 📊 گزارش‌گر عملکرد کنکور

**یک برنامه دسکتاپی شیک و تمام‌فارسی برای ثبت، تحلیل و نمایش نتایج آزمون‌های کنکور ایران.**

---

## 🌟 امکانات

✅ **ورود داده‌های آزمون**
ثبت تعداد سؤالات، درست، غلط و نزده برای هر درس کلیدی:
`آمار و احتمال، حسابان، هندسه، فیزیک، شیمی`

✅ **محاسبه میانگین وزنی**
محاسبه درصد کلی بر اساس ضرایب رسمی هر درس.

✅ **ذخیره تاریخچه**
تمام داده‌های آزمون‌ها در فایل `exam_results.json` ذخیره می‌شود.

✅ **نمایش عملکرد**
نمودارهای تعاملی: روند کلی به‌صورت خطی و تحلیل جزئی هر آزمون با نمودار دایره‌ای.

✅ **پشتیبانی کامل از فارسی**
نمایش متن راست‌به‌چپ و اعداد فارسی روی نمودارها.

✅ **رابط کاربری تمیز با PyQt5**
رابط کاربرپسند برای ورود داده‌ها و بازبینی عملکرد.

---

## 💻 نصب

مطمئن شوید **پایتون نسخه ۳** روی سیستم نصب است. سپس کتابخانه‌های مورد نیاز را نصب کنید:

```bash
pip install PyQt5 matplotlib arabic_reshaper python-bidi
```

---

## 🚀 نحوه اجرا

```bash
python Script2.py
```

این دستور برنامه را اجرا می‌کند. شما می‌توانید:

* **افزودن آزمون جدید**: وارد کردن تعداد سؤالات، درست و غلط برای هر درس.
* **مشاهده عملکرد**: مرور نمرات آزمون‌های قبلی، تحلیل روندها و مشاهده جزئیات هر درس.

تمام داده‌ها به‌صورت محلی در فایل `exam_results.json` ذخیره می‌شود.

---

## 📂 ساختار پروژه

```
📦 KonkurPerformanceReporter
├── Script2.py             # اسکریپت اصلی پایتون (برنامه PyQt5)
├── exam_results.json      # فایل JSON ذخیره‌سازی داده‌ها
└── README.md              # همین فایل توضیحات!
```

---

## 📈 تصاویر (اختیاری)

*اینجا می‌توانید اسکرین‌شات یا GIF از اجرای برنامه اضافه کنید.*

---

## 🛡 بهبودهای آینده

* افزودن دروس عمومی (ادبیات فارسی، عربی، دین و زندگی)
* خروجی گرفتن از کارنامه به‌صورت PDF قابل چاپ
* همگام‌سازی یا پشتیبان‌گیری ابری از داده‌ها
* تحلیل پیشرفته (شناسایی نقاط ضعف، پیشنهاد بهبود)


---

## 📜 مجوز

این پروژه متن‌باز است. آزادید فورک کنید، بهبود دهید و به اشتراک بگذارید (فقط یادتون نره حق سازنده رو رعایت کنید 😉).
