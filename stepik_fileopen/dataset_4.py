with open('dataset_3363_4.txt', 'r') as f:
    text = f.read().strip().split()

d = {}  # создаем словарь
for i in text:
    lst = i.split(';')
    d[lst[0]] = lst[1:]  # добавляем ключи(имена) и значения(список оценок)

for value in d.values():
    print((int(value[0]) + int(value[1]) + int(value[2]))/3)  # принтим среднее значение оценок

item1, item2, item3 = [], [], []  # создаем три пустых списка

for value in d.values():
    # добавляем оценки в списки по индексам
    item1.append(int(value[0]))
    item2.append(int(value[1]))
    item3.append(int(value[2]))

# выводим среднее по предмету
print(str(sum(item1)/len(item1)), str(sum(item2)/len(item2)), str(sum(item3)/len(item3)))
