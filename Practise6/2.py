import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel,
    QVBoxLayout, QWidget, QFileDialog, QMessageBox
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PIL import Image, ImageOps
import numpy as np

class ImageEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Простой редактор изображений")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.load_button = QPushButton("Загрузить изображение")
        self.grayscale_button = QPushButton("Черно-белый фильтр")
        self.save_button = QPushButton("Сохранить")

        self.load_button.clicked.connect(self.load_image)
        self.grayscale_button.clicked.connect(self.apply_grayscale)
        self.save_button.clicked.connect(self.save_image)

        layout.addWidget(self.load_button)
        layout.addWidget(self.grayscale_button)
        layout.addWidget(self.save_button)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)

        self.original_pil_image = None
        self.current_pil_image = None
        self.current_qpixmap = None

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выберите изображение", "", "Изображения (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_path:
            try:
                self.original_pil_image = Image.open(file_path).convert("RGB")
                self.current_pil_image = self.original_pil_image.copy()
                self.display_image(self.current_pil_image)
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить изображение:\n{e}")

    def apply_grayscale(self):
        if self.current_pil_image is None:
            QMessageBox.warning(self, "Предупреждение", "Сначала загрузите изображение.")
            return
        self.current_pil_image = ImageOps.grayscale(self.current_pil_image).convert("RGB")
        self.display_image(self.current_pil_image)

    def display_image(self, pil_image):
        data = np.array(pil_image)
        height, width, channel = data.shape
        bytes_per_line = 3 * width
        qimage = QImage(data.data, width, height, bytes_per_line, QImage.Format_RGB888)
        self.current_qpixmap = QPixmap.fromImage(qimage)
        self.image_label.setPixmap(self.current_qpixmap.scaled(
            self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
        ))

    def save_image(self):
        if self.current_pil_image is None:
            QMessageBox.warning(self, "Предупреждение", "Нет изображения для сохранения.")
            return
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Сохранить изображение", "", "PNG (*.png);;JPEG (*.jpg *.jpeg)"
        )
        if file_path:
            try:
                self.current_pil_image.save(file_path)
                QMessageBox.information(self, "Успех", "Изображение успешно сохранено!")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить изображение:\n{e}")

    def resizeEvent(self, event):
        if self.current_qpixmap:
            self.image_label.setPixmap(self.current_qpixmap.scaled(
                self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            ))
        super().resizeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageEditor()
    window.show()
    sys.exit(app.exec_())