
#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна,
#лето, осень).
#Напишите решения через list и через dict.

n_monht = input('введите номер месяца: ')
a , b , c , d = 'winter', 'spring', 'summer', 'autumn'
monht_dict = {'1': a, '2': a, '3': b, '4': b, '5': b, '6': c, '7' : c, '8' :c, '9' : d, '10' : d,'11' : d, '12' : a}
print(monht_dict[n_monht])
#season_list = [a,a,b,b,b,c,c,c,d,d,d,a]
#print (season_list[int(n_monht)-1])