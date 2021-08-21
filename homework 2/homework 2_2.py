
#Для списка реализовать обмен значений соседних элементов.
#Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
#При нечётном количестве элементов последний сохранить на своём месте.
#Для заполнения списка элементов нужно использовать функцию input().

user_input = input('list: ')
input_list = user_input.split()
for i in range(len(input_list)//2):
    k1, k2 = 2*i, 2*i + 1
    input_list[k1], input_list[k2] = input_list[k2], input_list[k1]
print(input_list)