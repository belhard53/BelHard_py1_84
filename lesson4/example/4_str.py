a = ""
b = "Hello Python"
print(type(a))



# l = len(a)

print(len(a), len(b))

# str = "123"
# print(str)
# print(str(123))

l = b.lower()
print(b.lower())

print("Python" in b)
print(b.find("l"))
print(b.find("l",3))
print(b.find("l",4))
print(b.rfind("l"))

f = b.find("l")
print(b.find("l", f + 1))

print(b.isalnum())
print(b.isdigit())
print(b.count("l"))


# ФОРМАТИРОВАНИЕ
name = "Vasya"
age = 22
print("Привет я %s мне %d года" % (name, age))
print("Привет я {} мне {} года".format(name, age))
print("Привет я {1} мне {0} года".format(age, name))
print("Привет я {name1} мне {age1} года".format(name1=name, age1=age))
print(f"Привет я {name} мне {age} года")
print(f"Привет я {name:*<15} мне {age} года") # дополнят * до 12 знаков
print(f"Привет я {name:=^15} мне {age} года")
b = 12345678
print(f"Сумма - {b:,}")
print(f"Сумма - {b:_}")
print(f"Сумма - {12.12162876:.3f}")
print(f"Сумма - {323123:010}") # дополнят нулями до 10 знаков
print(f"Сумма - {323123:010d}") # дополнят нулями до 10 знаков
print("{}:{:02}:{:02}".format(12, 1, 2)) # время

# a = "hello"
# print(b.capitalize())
# print(b.center(50,'*'))
# print(b.ljust(50,'*'))
# print(b.rjust(50,'*'))
# print(b.zfill(12)) 


a = "12311"
# print(a.isalpha())
# print(a.isalnum())
# print(a.isdigit())
# print(a.isnumeric())

# text = "Hello world"
# print(text.endswith("rld"))
# print(text.startswith("Hel", 1, 7))

# print(text.removeprefix("Hell"))
# print(text.removesuffix("rld"))

b = "Hello Python"
print(b.replace("l", "*"))
print(b.replace("l", ""))

# СРЕЗЫ
a = 1
b = 4
s = "0123456789"
print(s[3])
print(s[-3])
print(s[a:b])
print(s[0:7])
print(s[:7])
print(s[5:])
print(s[5:-1])
print(s[-3:-1])
print(s[0:10:2])
print(s[::2])
print(s[::-1])
print(s[9:5:-1])


a = "1,2,15"
b = a.split(",")
print(b)
print(int(b[1]))
# c = "/ - -  /".join(b) # собрать опять в строку
# print(c)
b = list(map(int, b))
print(b)
print(b[1])
max(b)
min(b)
sum(b)




print(ord("A"))
print(chr(65))



# множественная замена подстрок
a = "Однажды, в студеную зимнюю пору"
b = a.maketrans({"а":"А","у":"У","и":"И"})
b = a.translate(b)
print(b)




