#Реализовать структуру «Рейтинг», представляющую собой
#не возрастающий набор натуральных чисел.
#У пользователя необходимо запрашивать новый элемент рейтинга.Если в рейтинге существуют элементы с одинаковыми значениями,
#то новый элемент с тем же значением должен разместиться после них.

rating_list = [9,4,2,1]
rating = int(input('Enter rating: '))
inserted = False
for index, elem in enumerate(rating_list):
    if rating > elem:
        rating_list.insert(index, rating)
        inserted = True
        break

if not inserted:
    rating_list.append(rating)
print(rating_list)