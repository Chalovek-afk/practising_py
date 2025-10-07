import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QPushButton,
    QCalendarWidget, QTableWidget, QTableWidgetItem,
    QHeaderView, QTimeEdit
)
from PyQt5.QtCore import QDate, QTime


class EventPlanner(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Планировщик событий")
        self.resize(900, 600)

        # === Левая панель: ввод данных ===
        input_layout = QVBoxLayout()
        input_layout.setSpacing(10)

        # Название
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Название события")

        # Тип события
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Встреча", "Напоминание", "Дедлайн", "Прочее"])

        # Календарь
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setSelectedDate(QDate.currentDate())

        # Время
        self.time_edit = QTimeEdit()
        self.time_edit.setTime(QTime.currentTime())
        self.time_edit.setDisplayFormat("HH:mm")

        # Кнопки
        self.add_btn = QPushButton("Добавить событие")
        self.add_btn.clicked.connect(self.add_event)

        self.del_btn = QPushButton("Удалить выбранное")
        self.del_btn.clicked.connect(self.delete_event)

        # Собираем левую панель
        input_layout.addWidget(QLabel("Название:"))
        input_layout.addWidget(self.title_input)
        input_layout.addWidget(QLabel("Тип:"))
        input_layout.addWidget(self.type_combo)
        input_layout.addWidget(QLabel("Дата:"))
        input_layout.addWidget(self.calendar)
        input_layout.addWidget(QLabel("Время:"))
        input_layout.addWidget(self.time_edit)
        input_layout.addWidget(self.add_btn)
        input_layout.addWidget(self.del_btn)
        input_layout.addStretch()

        input_widget = QWidget()
        input_widget.setLayout(input_layout)

        # === Правая панель: таблица событий ===
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["Название", "Дата", "Время", "Тип"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(self.table.SelectRows)
        self.table.setSelectionMode(self.table.SingleSelection)

        # === Главный макет ===
        main_layout = QHBoxLayout()
        main_layout.addWidget(input_widget, stretch=1)
        main_layout.addWidget(self.table, stretch=2)
        self.setLayout(main_layout)

    def add_event(self):
        title = self.title_input.text().strip()
        if not title:
            return

        event_type = self.type_combo.currentText()
        date = self.calendar.selectedDate().toString("dd.MM.yyyy")
        time = self.time_edit.time().toString("HH:mm")

        row = self.table.rowCount()
        self.table.insertRow(row)

        self.table.setItem(row, 0, QTableWidgetItem(title))
        self.table.setItem(row, 1, QTableWidgetItem(date))
        self.table.setItem(row, 2, QTableWidgetItem(time))
        self.table.setItem(row, 3, QTableWidgetItem(event_type))

        # Очистка полей
        self.title_input.clear()
        self.title_input.setFocus()

    def delete_event(self):
        current = self.table.currentRow()
        if current >= 0:
            self.table.removeRow(current)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EventPlanner()
    window.show()
    sys.exit(app.exec_())