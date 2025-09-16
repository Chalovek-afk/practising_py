cinema_db = [
    {
        'film_name': 'Интерстеллар',
        'actor_list': ['Мэттью Макконахи', 'Энн Хэтэуэй', 'Джессика Честейн'],
        'session_list': ['12:30', '15:45', '19:00', '22:15'],
        'ticket_price': 560,
        'rating': 5.0
    },
    {
        'film_name': 'Начало',
        'actor_list': ['Леонардо ДиКаприо', 'Марион Котийяр', 'Том Харди', 'Эллиот Пейдж'],
        'session_list': ['11:00', '14:20', '17:50', '21:10'],
        'ticket_price': 320,
        'rating': 4.2
    },
    {
        'film_name': 'Матрица',
        'actor_list': ['Киану Ривз', 'Лоуренс Фишбёрн', 'Кэрри-Энн Мосс'],
        'session_list': ['13:15', '16:30', '20:00'],
        'ticket_price': 330,
        'rating': 4.8
    },
    {
        'film_name': 'Паразиты',
        'actor_list': ['Сон Кан-хо', 'Ли Сон Гён', 'Чхве У Сик', 'Пак Со Дам'],
        'session_list': ['10:45', '14:00', '18:20', '21:30'],
        'ticket_price': 250,
        'rating': 3.2
    }
]

for item in cinema_db:
    print(cinema_db.index(item))
    print(f'Название: {item.get("name")}')
    print(f'Актёры: {item.get("actor_list")}')
    print(f'Сеансы: {item.get("session_list")}')
    print(f'Цена билета: {item.get("ticket_price")}')
    print(f'Рейтинг: {item.get("rating")}')