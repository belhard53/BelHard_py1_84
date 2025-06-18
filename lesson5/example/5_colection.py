# list() - списки
# tuple() - кортежи - защищенный список
# dict() - словари
# set() - множества
# frozenset()


# ------------------------ tuple
# 
a = (1, 2, 3)
cor = (22 , 55)
color_rgb = (123, 10, 200)
green = (0, 255, 0)

b = 1, 2, 3
c = (1,)
print(b, c, type(c), type(b))

a = [1, 2, 3]
a = tuple(a)
print(a)



# -------------------------------- dict

# {ключ:значение, ключ2:значение2}

a = {}
a = dict()

print(a)

user = {'login':'vasya', 'pas':'qwerty', 'age':33}
#key (ключи) - только неизменяемые типы данных
#value (значения) - любые типы данных

print(user['age']) # взять значение по ключу 'age'

user['login'] = "petya"
user['name'] = 'Petya'
print(user)

a = {1:11, 2:22, 3:"Hello"}
b = dict(a=11, b=22, c='Hello')
print(a, b)

sp = [("key1", "value1"), ("key2", "value2")]
# sp = [["key1", "value1"], ["key2", "value2"]]
c = dict(sp)
print(c)

d1 = dict.fromkeys(["key1", "key2"], "value")
d2 = dict.fromkeys(["key1", "key2"])
print(d1, d2)



user1 = {
    "name":"Vasya", 
    "login":"vvasiiiia", 
    "age":23, 
    "2":"1217628", 
    'phones':{
        'mts':'1212121', 
        'vel':'4203948230'
    }, 
    "child":[
        '1212', 
        2121]
}

print(user1['age'])
print(user1['phones'])
print(user1['phones']['mts'])
print(user1['child'][1])




users = [
    {"name":"Vasya1", "login":"vvasiiiia",  "age":23},    
    {"name":"Vasya2", "login":"vvasiiiia",  "age":23},    
    {"name":"Vasya3", "login":"vvasiiiia",  "age":23},    
    {"name":"Vasya4", "login":"vvasiiiia",  "age":23},    
    {"name":"Vasya5", "login":"vvasiiiia",  "age":23},    
    {"name":"Vasya6", "login":"vvasiiiia",  "age":23},    
    {"name":"Vasya7", "login":"vvasiiiia",  "age":23},    
    {"name":"Vasya8", "login":"vvasiiiia",  "age":23}
]

print(users[3])
print(users[3]['age'])



users1 = {
    1:{"name":"Vasya1", "login":"vvasiiiia",  "age":23},    
    2:{"name":"Vasya2", "login":"vvasiiiia",  "age":23},        
}

users2 = {
    "Vasechkin":{"name":"Vasya1", "login":"vvasiiiia",  "age":23},    
    # "Petechkin":{"name":"Vasya2", "login":"vvasiiiia",  "age":23},
    # "Petechkin":{"name":"Vasya2", "login":"vvasiiiia",  "age":23},
    "Petechkin":{"name":"Vasya2", "login":"vvasiiiia",  "age":23},            
}

print(users1[1]['age'])
print(users2['Vasechkin']['age'])

print(len(users1))

print(list(user1.keys()))
print(list(user1['phones'].keys()))
print(list(user1.values()))
print(list(user1.items()))
a = list(user1.items())
b = dict(a)
print(b)

print(user1['name']) # если нет ключа выдаст ошибку
print(user1.get('name1')) # если нет ключа выдаст None
print(user1.get('name1', "нет")) # если нет ключа выдаст "нет"



d1 = {"key1":"value1"}
d2 = {"key2":"value2"}
d3 = {"key3":"value3"}
d1.update(d2) # добавить к словарю второй словарь, меняет словарь d1
d5 = d2 | d3 # сложить два словаря - не меняет d1 d2 - возвращает объединенный
print(d1)
print(d5)



# ---------------------------------------------- SET
# коллекция из уникальных значений

a = [1, 2, 3, 1, 2, 5]

b = set(a)
print(a, b)

a = {1, 1, 2, 3, 3, 4}
print(a, type(a))


a = set("Hello Python")
print(a)

b = frozenset(a)
print(b, type(b))




a = {8, 3, 1, 5 }
# b = {6, 7, 8, 3}
b = {8, 1, 3}

# Включает ли set другой set
print(a.issubset(b)) # все элементы a принадлежат b.
print( a <= b )

print(a.issuperset(b)) # все элементы b принадлежат a.
print( a >= b )


#объединение и пересечение

print(a | b) # об] объединить
print(a.union(b)) # объединить

print(a.intersection(b)) # пересечение - только общие
print(a & b)

print(a.difference(b)) # разность - есть только в первом
print(a - b)

print(a.symmetric_difference(b)) # есть в обоих но не общие
print(a ^ b)


