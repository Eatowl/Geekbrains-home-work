#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np 


# Задание №1
a = np.array([[1, 6],
			  [2, 8],
			  [3, 11],
			  [3, 10],
			  [1, 7]])

mean_a = np.mean(a, axis = 0)

print(mean_a)

# Вывод:
# [2.  8.4]


# Задание №2
a_centered = np.array([a[:, 0] - mean_a[0], a[:, 1] - mean_a[1]])

print(a_centered)

# Вывод:
# [[-1.   0.   1.   1.  -1. ]
# [-2.4 -0.4  2.6  1.6 -1.4]]


# Задание №3
a_centered_sp = np.dot(a_centered[0], a_centered[1])

print(a_centered_sp / (len(a_centered[1])-1))

# Вывод:
# 2.0


# Задание №4
print(np.cov(a.transpose()))

# Вывод:
# [[1.  2. ]
# [2.  4.3]]


import pandas as pd 

# Задание №1
authors = pd.DataFrame({
						'author_id': [1, 2, 3],
						'author_name': ['Тургенев', 'Чехов', 'Островский']
					   })

books = pd.DataFrame({
						'author_id': [1, 1, 1, 2, 2, 3, 3],
						'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
						'price': [450, 300, 350, 500, 450, 370, 290]
					})

print(authors) 

print(books)

# Вывод:
#    author_id author_name
# 0          1    Тургенев
# 1          2       Чехов
# 2          3  Островский
#    author_id            book_title  price
# 0          1           Отцы и дети    450
# 1          1                 Рудин    300
# 2          1     Дворянское гнездо    350
# 3          2      Толстый и тонкий    500
# 4          2       Дама с собачкой    450
# 5          3                 Гроза    370
# 6          3  Таланты и поклонники    290


# Задание №2
authors_price = pd.merge(authors, books, on="author_id", how="outer")

print(authors_price)

# Вывод:
#    author_id author_name            book_title  price
# 0          1    Тургенев           Отцы и дети    450
# 1          1    Тургенев                 Рудин    300
# 2          1    Тургенев     Дворянское гнездо    350
# 3          2       Чехов      Толстый и тонкий    500
# 4          2       Чехов       Дама с собачкой    450
# 5          3  Островский                 Гроза    370
# 6          3  Островский  Таланты и поклонники    290



# Задание №3
top5 = authors_price.sort_values(by="price").tail(5)
top5 = top5.reset_index(drop=True)
print(top5)

# Вывод:
#    author_id author_name         book_title  price
# 0          1    Тургенев  Дворянское гнездо    350
# 1          3  Островский              Гроза    370
# 2          1    Тургенев        Отцы и дети    450
# 3          2       Чехов    Дама с собачкой    450
# 4          2       Чехов   Толстый и тонкий    500

top5_v2 = authors_price.nlargest(5, 'price')
top5_v2 = top5_v2.reset_index(drop=True)

print(top5_v2)

# Вывод:
#    author_id author_name         book_title  price
# 0          2       Чехов   Толстый и тонкий    500
# 1          1    Тургенев        Отцы и дети    450
# 2          2       Чехов    Дама с собачкой    450
# 3          3  Островский              Гроза    370
# 4          1    Тургенев  Дворянское гнездо    350


# Задание №4
max_price = authors_price.groupby('author_name').agg({'price': 'max'}).rename(columns={'price':'max_price'})
min_price = authors_price.groupby('author_name').agg({'price': 'min'}).rename(columns={'price':'min_price'})
mean_price = authors_price.groupby('author_name').agg({'price': 'mean'}).rename(columns={'price':'mean_price'})

authors_stat = pd.merge(max_price, min_price, on="author_name", how="outer")
authors_stat = pd.merge(authors_stat, mean_price, on="author_name", how="outer")

print(authors_stat)

# Вывод:
#              max_price  min_price  mean_price
# author_name                                  
# Островский         370        290  330.000000
# Тургенев           450        300  366.666667
# Чехов              500        450  475.000000


# Задание №5
authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']

print(authors_price)

# Не готово, доделаю позже





















