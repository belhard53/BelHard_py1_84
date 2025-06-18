
a = []
b = list()

print(a, type(a))

a = [1, 2, 3, 10, "Hello", True, "Python", 2.5]

print(a)

print(a[2])
print(a[2:5])
print(a[-1])

a = list("Hello Python")
print(a)
b = "---".join(a)
# b = "".join(a)
print(b, type(b))

a = ['1', '123', '12', '112121212']
b = list(map(len, a))
print(b)
print(0 in b)
print(0 not in b)

a = [1, 2, 3, 10, [], "Hello", True, 
      "Python", 2.5, [1, 2, ["qwerty", 1, [12, 13]], 3], 123]

print(a)
print(a[9])
print(a[9][2])
print(a[9][2][2])
print(a[9][2][2][0])

user = ['login4', 'password', 'name4', ['phone1', 'phone2']]
users = [
    ['login1', 'password', 'name1', ['phone1', 'phone2'], 12],
    ['login2', 'password', 'name2', ['phone1', 'phone2'], 9],
    ['login3', 'password', 'name3', ['phone1', 'phone2'], 3]
]
# users.append(user)

print(users[1][3])

# import pprint
from pprint import pprint
print(users)
pprint(users)
# pprint.pprint(a)

a = [1, 2, 3]
b = [8, 4, 0]
c = [1, 2, [1, 2]]
print(a + b)
print(a*3)
print(len(c))

a = []
a.append("123") # добавить элемент
a.append(123)
a.append("")
a.append([1, 2, 3])
print(a)

a.remove(123) # удалить по значению
print(a)
b = a.pop() # удалить последний
b = a.pop(0) # удалить по индексу
print(a, b)

a = [1,2,6, 9, 0, 15]
# a.sort() # меняет оригинал - возвращает None
b = sorted(a) # не меняет оригинал - возвращает отсортированную копию 
print(a, b)

# a.clear()
# print(a)

print(a.index(6)) # узнать индекс

a.insert(0, 99) # вставить в нужное место
print(a)

a.reverse()
# a = a[::-1]
print(a)

del a[0]
del a[0:3]
print(a)


# --------------- копии списков
a = [1, 2, 3, [4, 5]]
b = a # простая копия при которой не создается новый объект, a и b это один и тот же объект
print(a, b)
b.append(4) # добавиться и в 'а' т.к. это один и тот же объект
print(a, b)


c = a.copy() # поверхностная копия - создает новый объект, но не касается вложенных списков 
# c = list(a) # аналогично
# c = a[:] # аналогично
print(id(a), id(b), id(c))
print(a is b, a is c)
c.append(9) # добавится только в c
print(a, b, c)
c[3].append(99) # добавиться во все 
print(a, b, c)

import copy
e = copy.deepcopy(a) # глубокая копия - создает новый объект на всех уровнях вложенности
e[3].append(999)
print(a, b, c, e)



# -------------
a = [1, 2, 3]
a[1] = 9
# a[9] = 9 # ошибка
print(a)





