import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Practise7/part_1/data/data.csv', sep=';', encoding='utf-8')

print("Загружено строк:", len(df))

yearly_stats = df.groupby('year').agg({
    'ege_budg': 'mean',
    'wos': 'mean',
    'scopus': 'mean',
    'total_income': 'mean'
}).reset_index()

print("Средние показатели по годам:")
print(yearly_stats)

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 1. Горизонтальная столбчатая диаграмма
years = yearly_stats['year'].astype(str)
ege_values = yearly_stats['ege_budg']
colors = plt.cm.viridis(np.linspace(0, 1, len(years)))

axes[0, 0].barh(years, ege_values, color=colors)
axes[0, 0].set_xlabel('Средний балл ЕГЭ бюджетных студентов')
axes[0, 0].set_ylabel('Год')
axes[0, 0].set_title('1. Горизонтальная столбчатая диаграмма\nСредние баллы ЕГЭ по годам')
axes[0, 0].grid(axis='x', alpha=0.3)
for i, v in enumerate(ege_values):
    axes[0, 0].text(v, i, f' {v:.2f}', va='center')

# 2. Первый линейный график (WOS)
axes[0, 1].plot(yearly_stats['year'], yearly_stats['wos'], marker='o', linewidth=2, 
                color='blue', markersize=8)
axes[0, 1].set_xlabel('Год')
axes[0, 1].set_ylabel('Количество публикаций')
axes[0, 1].set_title('2. Линейный график\nПубликации в WOS (Web of Science)')
axes[0, 1].grid(True, alpha=0.3)
axes[0, 1].set_xticks(yearly_stats['year'])

# 3. Второй линейный график (Scopus)
axes[1, 0].plot(yearly_stats['year'], yearly_stats['scopus'], marker='s', linewidth=2, 
                color='red', markersize=8)
axes[1, 0].set_xlabel('Год')
axes[1, 0].set_ylabel('Количество публикаций')
axes[1, 0].set_title('3. Линейный график\nПубликации в Scopus')
axes[1, 0].grid(True, alpha=0.3)
axes[1, 0].set_xticks(yearly_stats['year'])

# 4. Диаграмма рассеивания
sample_df = df.sample(min(500, len(df)), random_state=42)
scatter = axes[1, 1].scatter(sample_df['total_income'], sample_df['rnd'], 
                            alpha=0.6, c=sample_df['year'], cmap='plasma', s=50)
axes[1, 1].set_xlabel('Общий доход (total_income)')
axes[1, 1].set_ylabel('Научно-исследовательские работы (rnd)')
axes[1, 1].set_title('4. Диаграмма рассеивания\nСвязь между доходом и научными работами')
plt.colorbar(scatter, ax=axes[1, 1], label='Год')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('Practise7/part_1/university_analysis.png', dpi=300, bbox_inches='tight')
print("Графики сохранены в файл 'university_analysis.png'")
plt.show()
