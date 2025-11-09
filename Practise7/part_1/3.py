import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Имя': ['Алексей', 'Мария', 'Дмитрий', 'Анна', 'Сергей'],
    'Возраст': [25, 28, 22, 30, 27],
    'Зарплата': [50000, 65000, 45000, 70000, 55000],
    'Опыт_работы': [3, 5, 2, 7, 4],
    'Рейтинг': [4.5, 4.8, 4.2, 4.9, 4.6]
}

df = pd.DataFrame(data)
print("Исходный DataFrame:")
print(df)

print("1. Название колонок:")
print(df.columns.tolist())

print("2. Индексация по столбцу 'Имя':")
print(df['Имя'])
print("Индексация по столбцу 'Зарплата':")
print(df['Зарплата'])

print("3. Применение метода loc:")
print("Первые 3 строки:")
print(df.loc[0:2])
print("Выборка по условию (Зарплата > 50000):")
print(df.loc[df['Зарплата'] > 50000])
print("Выборка конкретных строк и столбцов (loc[0:2, ['Имя', 'Зарплата']]):")
print(df.loc[0:2, ['Имя', 'Зарплата']])

df['Бонус'] = df['Зарплата'] * 0.1
print("4. Добавлен новый столбец 'Бонус':")
print(df)

print("5. Сравнение столбцов:")
comparison = df['Зарплата'] > df['Опыт_работы'] * 10000
print("Сравнение: Зарплата > Опыт_работы * 10000")
print(comparison)

comparison2 = df['Возраст'] >= 25
print("Сравнение: Возраст >= 25")
print(comparison2)

comparison3 = df['Зарплата'] > df['Бонус'] * 10
print("Сравнение: Зарплата > Бонус * 10")
print(comparison3)

data2 = {
    'Имя': ['Елена', 'Иван'],
    'Возраст': [26, 29],
    'Зарплата': [60000, 58000],
    'Опыт_работы': [4, 6],
    'Рейтинг': [4.7, 4.5],
    'Бонус': [6000, 5800]
}

df2 = pd.DataFrame(data2)

print("6. Объединение DataFrame:")
print("Второй DataFrame:")
print(df2)

df_vertical = pd.concat([df, df2], ignore_index=True)
print("Объединение по вертикали (concat):")
print(df_vertical)

data3 = {
    'Город': ['Москва', 'СПб', 'Казань', 'Москва', 'СПб'],
    'Отдел': ['IT', 'Маркетинг', 'IT', 'Продажи', 'IT']
}

df3 = pd.DataFrame(data3)
df_horizontal = pd.concat([df, df3], axis=1)
print("Объединение по горизонтали (concat axis=1):")
print(df_horizontal)

print("7. Метод describe (статистическое описание):")
print(df.describe())

print("8. Кумулятивная сумма:")
df['Кумулятивная_зарплата'] = df['Зарплата'].cumsum()
print("Кумулятивная сумма по столбцу 'Зарплата':")
print(df[['Имя', 'Зарплата', 'Кумулятивная_зарплата']])

df['Кумулятивный_опыт'] = df['Опыт_работы'].cumsum()
print("Кумулятивная сумма по столбцу 'Опыт_работы':")
print(df[['Имя', 'Опыт_работы', 'Кумулятивный_опыт']])
print()

print("9. Построение графиков:")
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.bar(df['Имя'], df['Зарплата'], color='skyblue')
plt.title('Зарплата по сотрудникам')
plt.xlabel('Имя')
plt.ylabel('Зарплата')
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
plt.plot(df['Имя'], df['Кумулятивная_зарплата'], marker='o', color='green')
plt.title('Кумулятивная сумма зарплаты')
plt.xlabel('Имя')
plt.ylabel('Кумулятивная зарплата')
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.savefig('Practise7/part_1/dataframe_plot.png')
print("Графики сохранены в файл 'dataframe_plot.png'")
plt.show()

print("Финальный DataFrame:")
print(df)

