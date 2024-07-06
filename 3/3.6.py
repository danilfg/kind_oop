# 6

# # 5
# class Dimensions:
#     def __init__(self, a, b, c):
#         self.a = int(a) if isinstance(a, int) else float(a)
#         self.b = int(b) if isinstance(b, int) else float(b)
#         self.c = int(c) if isinstance(c, int) else float(c)
        
#     def __setattr__(self, key, value):
#         if value <= 0:
#             raise ValueError("габаритные размеры должны быть положительными числами")
#         super().__setattr__(key, value)
        
#     def __hash__(self):
#         return hash((self.a, self.b, self.c,))
    
    
# # dim = Dimentions(2,0,4)
# # lst = input()

# # s_inp = "1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5"
# s_inp = s_inp.split('; ')
# # print(list(map(lambda x: x.split(), s_inp)))
# lst_dims = list(map(lambda x: Dimensions(*x.split()), s_inp))
# lst_dims = sorted(lst_dims, key=hash)

# 4
# import sys


# class BookStudy:
#     def __init__(self, name, author, year):
#         self.name = name
#         self.author = author
#         self.year = int(year)

#     def __hash__(self):
#         return hash((self.name.lower(), self.author.lower()))
    
#     def __eq__(self, other):
#         return hash((self.name.lower(), self.author.lower())) == hash((other.name.lower(), other.author.lower()))


# sys.stdin = open('3.6.4.py.txt', 'r', encoding='utf-8')
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока

# lst_bs = [BookStudy(*lst.split('; ')) for lst in lst_in]
# unique_books = len(set(lst_bs))
# print(unique_books)

# # 3
# import sys


# class DataBase:
#     def __init__(self, path):
#         self.path = path
#         self.dict_db = {}
        
#     def write(self, record):
#         if record in self.dict_db:
#             self.dict_db[record].append(record)
#         else:
#             self.dict_db[record] = [record]

#     def read(self, pk):
#         for item in self.dict_db:
#             if pk == item.pk:
#                 return item
            

# class Record:
#     id = 1
    
#     def __init__(self, fio, descr, old):
#         self.pk = Record.id
#         Record.id += 1
#         self.fio = fio
#         self.descr = descr
#         self.old = int(old)
    
#     def __hash__(self):
#         return hash((self.fio.lower(), self.old))
    
#     def __eq__(self, other):
#         return hash((self.fio.lower(), self.old)) == hash((other.fio.lower(), other.old))
    
# path = 'path'
# db = DataBase(path)
# # sys.stdin = open('3.6.3.py.txt', 'r', encoding='utf-8')
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
# for lst in lst_in:
#     db.write(Record(*(lst.split('; '))))
    
    
# print('db', db.dict_db)
# d = tuple(db.dict_db.values())[0][0]
# assert type(d.descr) == str and type(d.fio) == str and type(d.old) == int, "значениями словаря должен быть список из объектов класса Rect с набором атрибутов: descr (строка), fio (строка), old (целое число)"

# db22345 = DataBase('123')
# r1 = Record('fio', 'descr', 10)
# r2 = Record('fio', 'descr', 10)
# assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"

# db22345.write(r2)
# r22 = db22345.read(r2.pk)
# assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"

# assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

# fio = lst_in[0].split(';')[0].strip()
# print(fio)
# v = list(db.dict_db.values())
# if fio == "Балакирев С.М.":
#     print(v)
#     print(len(v[0]))
#     assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(v[3]) == 1, "неверно сформирован словарь dict_db"
    
# if fio == "Гейтс Б.":
#     assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(v[3]) == 1, "неверно сформирован словарь dict_db"
# # 2
# import sys


# class ShopItem:
#     def __init__(self, name, weight, price):
#         self.name = name
#         self.weight = weight
#         self.price = price
        
#     def __eq__(self, other):
#         return self.name == other.name and self.weight == other.weight and self.price == other.price
    
#     def __hash__(self):
#         return hash((self.name.lower(), self.weight, self.price))

        
# sys.stdin = open('3.6.2.py.txt', 'r', encoding='utf-8')
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока

# shop_items = {}
# for lst in lst_in:
#     obj = lst.split(':')[:1] + lst.split(':')[1].split()
#     tmp_item = ShopItem(obj[0], float(obj[1]), float(obj[2]))
#     # if tmp_item not in shop_items
#     shop_items[tmp_item] = [tmp_item, 1] if tmp_item not in shop_items else [tmp_item, shop_items[tmp_item][1] + 1]
    
    
    
# print(shop_items)
# # 1
# class Rect:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height

#     def __eq__(self, other):
#         return self.width == other.width and self.height == other.height
    
#     def __hash__(self):
#         return hash((self.width, self.height))
        
        
# r1 = Rect(10, 5, 100, 50)
# r2 = Rect(-10, 4, 100, 50)

# h1, h2 = hash(r1), hash(r2)   # h1 == h2

# print(h1 == h2)
# # 0
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
    
#     def __hash__(self):
#         return hash((self.x, self.y))
        
        
# p1 = Point(1, 2)
# p2 = Point(1, 2)

# print(hash(p1), hash(p2), sep="\n")

# d = {}
# d[p1] = 1
# d[p2] = 2
# print(d)