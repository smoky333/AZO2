# Представьте, что у вас есть таблица из 10 учеников с оценками учеников по 5 разным предметам.
# Вам нужно выполнить несколько шагов, чтобы проанализировать эти данные:
# Самостоятельно создайте DataFrame с данными
# Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
# Вычислите среднюю оценку по каждому предмету
# Вычислите медианную оценку по каждому предмету
# Вычислите Q1 и Q3 для оценок по математике:
# Q1_math = df['Математика'].quantile(0.25)
# Q3_math = df['Математика'].quantile(0.75)
# можно также попробовать рассчитать IQR
# Вычислите стандартное отклонение

import pandas as pd

data = {
    'Ученик': ['Иван', 'Ника', 'Натия', 'Роман', 'Георгий', 'Натали', 'Иван', 'Петр', 'Анна', 'Лука'],
    'Математика': [5, 4, 5, 4, 5, 4, 3, 4, 5, 4],
    'Русский язык': [5, 4, 3, 4, 5, 4, 5, 4, 3, 4],
    'Физика': [5, 4, 5, 4, 4, 4, 5, 4, 5, 4],
    'Химия': [5, 4, 4, 4, 5, 4, 3, 4, 5, 2],
    'Биология': [5, 4, 5, 4, 5, 4, 5, 4, 5, 4],
    'География': [5, 4, 3, 4, 3, 4, 5, 3, 5, 4],
    'Английский язык': [5, 3, 5, 4, 2, 4, 5, 2, 5, 4],
    }

df = pd.DataFrame(data)

print(df.head())
average_scores = df.mean(numeric_only=True)
print(f'\nСредняя оценка по каждому предмету:')
print(average_scores)

median_scores = df.median(numeric_only=True)
print(f'\nМедианная оценка по каждому предмету:')
print(median_scores)

q1_math = df['Математика'].quantile(0.25)
q3_math = df['Математика'].quantile(0.75)
print(f'\nQ1_math = {q1_math}')
print(f'Q3_math = {q3_math}')

iqr_math = q3_math - q1_math
print(f'\nIQR для оценок по математике:')
print(iqr_math)

std_deviation_math = iqr_math / 2
print(f'\nСтандартное отклонение для оценок по математике:')
print(std_deviation_math)


