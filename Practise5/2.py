import sys

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QComboBox, QListWidget, QPushButton,
    QDialog, QLineEdit, QFormLayout, QMessageBox
)


class AddMovieDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить фильм")

        self.title_edit = QLineEdit()
        self.year_edit = QLineEdit()
        self.director_edit = QLineEdit()

        layout = QFormLayout()
        layout.addRow("Название:", self.title_edit)
        layout.addRow("Год выпуска:", self.year_edit)
        layout.addRow("Режиссёр:", self.director_edit)

        button_box = QHBoxLayout()
        ok_button = QPushButton("ОК")
        cancel_button = QPushButton("Отмена")
        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        button_box.addWidget(ok_button)
        button_box.addWidget(cancel_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addLayout(button_box)
        self.setLayout(main_layout)

    def get_data(self):
        return (
            self.title_edit.text().strip(),
            self.year_edit.text().strip(),
            self.director_edit.text().strip()
        )


class MovieCatalogApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Каталог фильмов")
        self.resize(500, 400)

        self.movies = {
            "Комедия": [
                ("1+1", "2011", "Оливье Накаш"),
                ("Маска", "1994", "Чак Рассел"),
                ("Один дома", "1990", "Крис Коламбус"),
                ("Большой куш", "2000", "Гай Ричи"),
                ("Суперперцы", "2010", "Пол Кинг")
            ],
            "Драма": [
                ("Побег из Шоушенка", "1994", "Фрэнк Дарабонт"),
                ("Зелёная миля", "1999", "Фрэнк Дарабонт"),
                ("Форрест Гамп", "1994", "Роберт Земекис"),
                ("Список Шиндлера", "1993", "Стивен Спилберг"),
                ("1+1", "2011", "Оливье Накаш")
            ],
            "Боевик": [
                ("Крёстный отец", "1972", "Фрэнсис Форд Коппола"),
                ("Терминатор 2: Судный день", "1991", "Джеймс Кэмерон"),
                ("Матрица", "1999", "Лана и Лилли Вачовски"),
                ("Джон Уик", "2014", "Чад Стахелски"),
                ("Мстители", "2012", "Джосс Уидон")
            ]
        }

        self.genre_combo = QComboBox()
        self.movie_list = QListWidget()
        self.add_button = QPushButton("Добавить фильм")

        self.genre_combo.addItems(self.movies.keys())

        self.genre_combo.currentTextChanged.connect(self.update_movie_list)
        self.movie_list.itemDoubleClicked.connect(self.show_movie_info)
        self.add_button.clicked.connect(self.add_movie)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Выберите жанр:"))
        layout.addWidget(self.genre_combo)
        layout.addWidget(QLabel("Фильмы:"))
        layout.addWidget(self.movie_list)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

        self.update_movie_list()

    def update_movie_list(self):
        genre = self.genre_combo.currentText()
        self.movie_list.clear()
        for title, year, director in self.movies.get(genre, []):
            self.movie_list.addItem(title)

    def show_movie_info(self, item):
        genre = self.genre_combo.currentText()
        title = item.text()
        for t, year, director in self.movies[genre]:
            if t == title:
                info = f"Название: {title}\nГод: {year}\nРежиссёр: {director}"
                QMessageBox.information(self, "Информация о фильме", info)
                break

    def add_movie(self):
        dialog = AddMovieDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            title, year, director = dialog.get_data()
            if not title or not year or not director:
                QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены!")
                return
            if not year.isdigit():
                QMessageBox.warning(self, "Ошибка", "Поле Year должно быть числовым!")
                return

            genre = self.genre_combo.currentText()
            self.movies[genre].append((title, year, director))
            self.update_movie_list()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MovieCatalogApp()
    window.show()
    sys.exit(app.exec_())
