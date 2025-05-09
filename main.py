import sys
import json
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem, 
                             QMessageBox, QFrame)
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
from arabic_reshaper import reshape
from bidi.algorithm import get_display

# تنظیم فونت برای matplotlib
matplotlib.rcParams["font.family"] = ["DejaVu Sans"]  # فونت پیش‌فرض
matplotlib.rcParams["axes.unicode_minus"] = False

# ضرایب دروس اختصاصی رشته ریاضی
SUBJECTS = {
    "حسابان": 4,
    "هندسه": 2,
    "فیزیک": 3,
    "شیمی": 2
}
TOTAL_WEIGHT = sum(SUBJECTS.values())

# تابع تبدیل اعداد انگلیسی به فارسی
def en_to_fa(num, formatter='%1.1f%%'):
    num_as_string = formatter % num
    mapping = dict(zip('0123456789.%', '۰۱۲۳۴۵۶۷۸۹.%'))
    return ''.join(mapping.get(digit, digit) for digit in num_as_string)

# تابع ذخیره در JSON
def save_to_json(data):
    try:
        with open("exam_results.json", "r", encoding="utf-8") as file:
            history = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []
    exam_number = len(history) + 1
    data["name"] = f"آزمون {exam_number}"
    history.append(data)
    with open("exam_results.json", "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=4)

# تابع خواندن از JSON
def load_from_json():
    try:
        with open("exam_results.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# کلاس اصلی برنامه
class ExamApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("کارنامه‌ساز کنکور")
        self.setGeometry(100, 100, 1000, 700)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        self.show_input_page()

    def show_input_page(self):
        self.clear_layout()
        self.layout.addWidget(QLabel("ورود اطلاعات آزمون", alignment=Qt.AlignCenter))
        
        self.entries = {}
        for subject in SUBJECTS:
            frame = QFrame()
            frame_layout = QHBoxLayout(frame)
            frame_layout.addWidget(QLabel(f"{subject} (ضریب {SUBJECTS[subject]})"))
            
            q = QLineEdit("25")
            c = QLineEdit("0")
            w = QLineEdit("0")
            frame_layout.addWidget(QLabel("سؤالات:"))
            frame_layout.addWidget(q)
            frame_layout.addWidget(QLabel("درست:"))
            frame_layout.addWidget(c)
            frame_layout.addWidget(QLabel("غلط:"))
            frame_layout.addWidget(w)
            self.entries[subject] = {"questions": q, "correct": c, "wrong": w}
            self.layout.addWidget(frame)
        
        submit_btn = QPushButton("ثبت آزمون")
        submit_btn.clicked.connect(self.submit)
        perf_btn = QPushButton("مشاهده عملکرد")
        perf_btn.clicked.connect(self.show_performance_page)
        
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(submit_btn)
        btn_layout.addWidget(perf_btn)
        self.layout.addLayout(btn_layout)
        self.layout.addStretch()

    def show_performance_page(self):
        self.clear_layout()
        history = load_from_json()
        
        if not history:
            self.layout.addWidget(QLabel("هیچ آزمونی ثبت نشده!", alignment=Qt.AlignCenter))
            back_btn = QPushButton("بازگشت به ورود داده")
            back_btn.clicked.connect(self.show_input_page)
            self.layout.addWidget(back_btn, alignment=Qt.AlignCenter)
            return
        
        # نمودار خطی عملکرد کلی
        fig, ax = plt.subplots(figsize=(8, 3))
        names = [exam["name"] for exam in history]
        persian_names = [get_display(reshape(name)) for name in names]
        weighted_percents = [self.calculate_weighted_percent(exam) for exam in history]
        ax.plot(persian_names, weighted_percents, marker='o', color='#2196F3')
        ax.set_title("Overall Performance Trend")
        ax.set_xlabel("Exam")
        ax.set_ylabel("Weighted Percentage")
        plt.xticks(rotation=45)
        plt.tight_layout()
        canvas = FigureCanvas(fig)
        self.layout.addWidget(canvas)
        
        # لیست آزمون‌ها
        self.exam_list = QListWidget()
        for exam in history:
            item = QListWidgetItem(f"{exam['name']} ({exam['date']})")
            self.exam_list.addItem(item)
        self.exam_list.itemClicked.connect(self.show_exam_details)
        self.layout.addWidget(self.exam_list)
        
        back_btn = QPushButton("بازگشت به ورود داده")
        back_btn.clicked.connect(self.show_input_page)
        self.layout.addWidget(back_btn, alignment=Qt.AlignCenter)

    def clear_layout(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def submit(self):
        data = {"date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        try:
            for subject in SUBJECTS:
                q = int(self.entries[subject]["questions"].text())
                c = int(self.entries[subject]["correct"].text())
                w = int(self.entries[subject]["wrong"].text())
                u = q - (c + w)
                if u < 0:
                    QMessageBox.warning(self, "خطا", f"جمع درست و غلط در {subject} بیشتر از تعداد سؤالات است!")
                    return
                data[subject] = {"questions": q, "correct": c, "wrong": w, "unanswered": u}
            save_to_json(data)
            QMessageBox.information(self, "موفقیت", "آزمون با موفقیت ثبت شد!")
        except ValueError:
            QMessageBox.warning(self, "خطا", "لطفاً اعداد معتبر وارد کنید!")

    def calculate_weighted_percent(self, exam):
        weighted_percent = 0
        for subject, weight in SUBJECTS.items():
            values = exam[subject]
            percent = (values["correct"] / values["questions"]) * 100
            weighted_percent += percent * weight
        return weighted_percent / TOTAL_WEIGHT

    def show_exam_details(self, item):
        history = load_from_json()
        exam_name = item.text().split(" (")[0]
        exam = next(ex for ex in history if ex["name"] == exam_name)
        
        self.clear_layout()
        self.layout.addWidget(QLabel(f"کارنامه {exam['name']} ({exam['date']})", alignment=Qt.AlignCenter))
        
        # میانگین وزنی
        weighted_avg = self.calculate_weighted_percent(exam)
        self.layout.addWidget(QLabel(f"میانگین وزنی درصد: {weighted_avg:.2f}%", alignment=Qt.AlignCenter))
        
        # نمودار دایره‌ای کلی
        total_q = sum(exam[s]["questions"] for s in SUBJECTS)
        total_c = sum(exam[s]["correct"] for s in SUBJECTS)
        total_w = sum(exam[s]["wrong"] for s in SUBJECTS)
        total_u = total_q - (total_c + total_w)
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.pie([total_c, total_w, total_u], 
               labels=[get_display(reshape("درست")), get_display(reshape("غلط")), get_display(reshape("نزده"))],
               autopct=en_to_fa, colors=['#4CAF50', '#F44336', '#FFC107'])
        ax.set_title("Overall Performance")
        canvas = FigureCanvas(fig)
        self.layout.addWidget(canvas)
        
        # نمودارهای دروس
        fig, axes = plt.subplots(2, 2, figsize=(10, 10))
        axes = axes.ravel()
        for i, subject in enumerate(SUBJECTS):
            values = exam[subject]
            correct_p = (values["correct"] / values["questions"]) * 100
            wrong_p = (values["wrong"] / values["questions"]) * 100
            unanswered_p = (values["unanswered"] / values["questions"]) * 100
            axes[i].pie([correct_p, wrong_p, unanswered_p], 
                        labels=[get_display(reshape("درست")), get_display(reshape("غلط")), get_display(reshape("نزده"))],
                        autopct=en_to_fa, colors=['#4CAF50', '#F44336', '#FFC107'])
            axes[i].set_title(get_display(reshape(subject)))
        canvas = FigureCanvas(fig)
        self.layout.addWidget(canvas)
        
        back_btn = QPushButton("بازگشت به عملکرد")
        back_btn.clicked.connect(self.show_performance_page)
        self.layout.addWidget(back_btn, alignment=Qt.AlignCenter)

# اجرای برنامه
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExamApp()
    window.show()
    sys.exit(app.exec_())