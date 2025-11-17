import re
import pandas as pd
from collections import Counter

with open('Practise8/part_1/text/file.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines() # чтение файла


text = ''.join(lines).lower() # приведение к нижнему регистру
words = re.findall(r'\b[а-яё]{2,}\b', text) # поиск всех слов


word_counts = Counter(words)
top10 = word_counts.most_common(10) # поиск 10 самых популярных

df = pd.DataFrame(top10, columns=['Слово', 'Частота'])
print(df) # вывод датафрейма

df.to_csv('Practise8/part_1/output/top10_words.csv', index=False, encoding='utf-8-sig')
df.to_excel('Practise8/part_1/output/top10_words.xlsx', index=False)
