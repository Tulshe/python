# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_1 = ['apple', 'pear', 'melon', 'peach', 'mango', 'lemon']
fruit_2 = ['orange', 'melon', 'grapes', 'banana', 'plum', 'mango']

fruit_match = [i for i in fruit_1 if i in fruit_2]
print(fruit_match)
