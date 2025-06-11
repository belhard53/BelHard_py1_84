some_var = "Hello PythonHello PythonHello PythonHello PythonHello PythonHello PythonHello PythonHello PythonHello PythonHello PythonHello PythonHello Python"

user_name = "Petya" # str
user_age = 33 # int
a = 1.2 # float
ok = True # bool
name = None # none


# в названии перенных только - a-Z 0-9 _ 

# user_name - snake case
# userName - camel case

user2 = 1
#2user = 1 # нельзя

win_w = 500
win_h = 700



print(user_name)
print(win_w / 2)
print(some_var)

b = type(a) # определить тип переменной
print(b)
print(type(user_age))

print(1 + 1)
# print("1" + 1)

# перевод типов
#str()
#int()
#float()
#bool()

a = 1
b = "2"
c = "2.2"

f = None # пустота
ok = True # логический тип
ok = False

is_send = True

print(a + int(b))
print(a + float(c))
print(str(a) + b)
print(int(2.9))
print('---------bool---------')
print(bool(0), bool(1), bool(11), bool(-5), bool(5-5))
print(bool(""), bool("d"), bool("adasda"))


print(1+1)
print(1-1)
print(1/1)
print(1*1)
print(1**1) # степень
print(14/2) # 
print(15/2) # 
print(15//2) # целая часть
print(15%2) # остаток

print(2+2*2) # существует приоритет операций - остальные в презентации последняя страница
print((2+2)*2)

a = 1
a = 2
a = "python"

print1 = 123
print(print1)


a = 0
a = a + 1
a += 1 # тоже самое - увеличили а на 1

a = 10
a += 1 # a = a + 1
a -= 1 # a = a - 1
a /= 1
a *= 1


a =  b =  c = 10
print('----', a, b, c)
a, b, c = 10, 16, "hello"


print(a, b)
a, b = b, a
print(a, b)

a = "python"
b = 'hello'

print(a + b)
print(a + " - " + b)
print("-"*20, a, b)
print(a * 10)

print("тут " + a + "какой-то" + b + " текст")
print("тут {a} какой-то {b} текст")
print(f"тут {a} какой-то {b} текст") # форматная строка

print("hello \npython")
print("путь к папке с:\new_folder")
print(r"путь к папке с:\new_folder")
print("путь к папке с:\\new_folder")

a, b, c, d = 1, 2, 3, 4
print(a, b, c, d, sep=" - ")
print(a, b, c, d, sep="")

print(a, b, c, d, end="--\n--")
print(a, b, c, d, end="--\n--", sep='_-_')
print(a, b, c, d, sep='_-_', end="--\n--")
print(a, end="--\n--")
print(a, b, c, d)

a = 111**1111
# print(a)

a = 1_234_567_323_323 # для удобства
print(a)

a = 1.12121 + 1.32323 + 55.4234234234
print(round(a, 4))
print(a)

# для округления сложного
# import math
# math.floor() # округляет вниз
# math.ceil() # округляет вверх


b = a
b = 1
print(id(a)) # возвращает адрес переменной в памяти компа 
print(id(b))
print(a is b)


a = "очень длинная строка очень длинная строка очень длинная строка " + \
    "очень длинная строка очень длинная строка очень длинная строка "
print(a)    

a = "очень длинная строка очень длинная строка очень длинная строка " \
    "очень длинная строка очень длинная строка очень длинная строка "
print(a)    

a = ("очень длинная строка очень длинная строка очень длинная строка "
     "очень длинная строка очень длинная строка очень длинная строка ")
print(a)   


# многострочная строка    
b = '''
hello1
hello2
hello3
hello4
'''
print(b)


# ----------------------------

# ctrl+c - остановить программу в любой момент

name = input("Как твое имя: ")
# print("Привет", name)
age = int(input("Возраст: "))
print(age, type(age))
year = 2025 - age
print(f"Привет {name} тебе {age} лет. \nТы родился в {year} году.")










