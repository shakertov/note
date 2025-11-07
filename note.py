import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QMenu, QAction
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtGui import QFont

TEXT_FILE = "text.txt"
SETTINGS_FILE = "settings.txt"


class DesktopNote(QWidget):
    def __init__(self):
        super().__init__()
        self.opacity_level = 0.85  # прозрачность окна (1.0 — непрозрачно, 0.0 — полностью прозрачное)
        self.initUI()
        self.load_settings()
        self.load_text()

        # Автоматическое обновление текста каждые 3 секунды
        self.timer = QTimer()
        self.timer.timeout.connect(self.load_text)
        self.timer.start(3000)

    def initUI(self):
        # Настройки флагов окна
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |  # поверх всех окон
            Qt.Tool
        )

        # Главное: включаем полную прозрачность фона окна
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(self.opacity_level)

        # Создаём метку для текста
        self.label = QLabel("", self)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # Используем RGBA с прозрачностью фона и закруглёнными углами
        self.label.setStyleSheet("""
            QLabel {
                color: white;
                background-color: rgba(0, 0, 0, 160);
                padding: 12px;
                border-radius: 12px;
            }
        """)

        self.label.setFont(QFont("Segoe UI", 12))

        # Размещение
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.oldPos = None
        self.resize(300, 150)

    def load_text(self):
        if os.path.exists(TEXT_FILE):
            with open(TEXT_FILE, "r", encoding="utf-8") as f:
                self.label.setText(f.read())
        else:
            self.label.setText("(Создайте файл text.txt с вашим текстом)")

    # === Движение мышью ===
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.oldPos is not None:
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.save_settings()
            self.oldPos = None

    # === Контекстное меню ===
    def contextMenuEvent(self, event):
        menu = QMenu(self)

        edit_action = QAction("📝 Редактировать текст", self)
        edit_action.triggered.connect(self.edit_text)
        menu.addAction(edit_action)

        exit_action = QAction("❌ Выход", self)
        exit_action.triggered.connect(self.close_app)
        menu.addAction(exit_action)

        menu.exec_(event.globalPos())

    def edit_text(self):
        """Открывает text.txt в Блокноте"""
        if not os.path.exists(TEXT_FILE):
            with open(TEXT_FILE, "w", encoding="utf-8") as f:
                f.write("Введите сюда свой текст.")
        try:
            subprocess.Popen(["notepad.exe", TEXT_FILE])
        except Exception as e:
            print(f"Ошибка при открытии файла: {e}")

    def close_app(self):
        QApplication.quit()

    # === Сохранение и загрузка положения ===
    def resizeEvent(self, event):
        self.save_settings()

    def load_settings(self):
        if os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                data = f.read().split(",")
                if len(data) == 4:
                    self.move(int(data[0]), int(data[1]))
                    self.resize(int(data[2]), int(data[3]))

    def save_settings(self):
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            f.write(f"{self.x()},{self.y()},{self.width()},{self.height()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    note = DesktopNote()
    note.show()
    sys.exit(app.exec_())
