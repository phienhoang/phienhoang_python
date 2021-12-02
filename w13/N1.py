import pickle

iter = range(8)
with open('data1.pickle', 'wb') as f:
    # Сериализация словаря data с использованием
    # последней доступной версии протокола.
    pickle.dump(iter, f, pickle.HIGHEST_PROTOCOL)

with open('data1.pickle', 'rb') as f:
    # Версия протокола определяется автоматически,
    # нет необходимости явно указывать его.
    data = pickle.load(f)
for i in data:
    print(i)


pr = abs(-20)

with open('data2.pickle', 'wb') as f:
    # Сериализация словаря data с использованием
    # последней доступной версии протокола.
    pickle.dump(pr, f, pickle.HIGHEST_PROTOCOL)


with open('data2.pickle', 'rb') as f:
    # Версия протокола определяется автоматически,
    # нет необходимости явно указывать его.
    data = pickle.load(f)
print(data)


from collections import deque 
      
queue = deque(['name','age','DOB'])  
      
with open('data3.pickle', 'wb') as f:
    # Сериализация словаря data с использованием
    # последней доступной версии протокола.
    pickle.dump(queue, f, pickle.HIGHEST_PROTOCOL)

with open('data3.pickle', 'rb') as f:
    # Версия протокола определяется автоматически,
    # нет необходимости явно указывать его.
    data = pickle.load(f)
print(data)


def cum(x,y):
    return x+y

with open('data4.pickle', 'wb') as f:
    # Сериализация словаря data с использованием
    # последней доступной версии протокола.
    pickle.dump(cum(5,3), f, pickle.HIGHEST_PROTOCOL)

with open('data4.pickle', 'rb') as f:
    # Версия протокола определяется автоматически,
    # нет необходимости явно указывать его.
    data = pickle.load(f)
print(data)



'''Что из этого можно сериализовать?  итераторы, встроенные функции, функции и классы (сами классы, а не их объекты!) из подключенных библиотек, самописные функции и классы.

Можно с этими объектами после их десериализации взаимодействовать так, как это бы делалось до сериализации. '''