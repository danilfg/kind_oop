# 6
from math import sqrt


class RadiusVector:
    def __init__(self, *args):
        self.__vector = [0 for _ in range(*args)] if len(args) == 1 else list(args)

    def get_coords(self):
        return tuple(self.__vector)
    
    def set_coords(self, *args):
        iter_count = len(args) if len(args) <= len(self.__vector) else len(self.__vector)
        for i in range(iter_count):
            self.__vector[i] = args[i]

    def __len__(self):
        return len(self.__vector)
    
    def __abs__(self):
        res = 0
        for num in self.__vector:
            res += num * num
        return sqrt(res)


vector3D = RadiusVector(3)
print(vector3D.get_coords())
vector3D.set_coords(3, -5.6, 8)

a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)

print(res_len, res_abs, sep='\n')

# # 5
# from math import sqrt


# class Complex:
#     def __init__(self, real, img):
#         self.__real = real
#         self.__img = img

#     def check_num(self, num):
#         if isinstance(num, int) or isinstance(num, float):
#             return num
#         raise ValueError("Неверный тип данных.")

#     @property
#     def real(self):
#         return self.__real
    
#     @real.setter
#     def real(self, value):
#         self.__real = self.check_num(value)

#     @property
#     def img(self):
#         return self.__img
    
#     @img.setter
#     def img(self, value):
#         self.__img = self.check_num(value)

#     def __abs__(self):
#         return sqrt(self.__real * self.__real + self.__img * self.__img)


# cmp = Complex(7, 8)
# cmp.real = 3
# cmp.img = 4
# c_abs = abs(cmp)
# print(c_abs)
# # 4

# class ObjList:
#     def __init__(self, data):
#         self.__data = data
#         self.__prev = None
#         self.__next = None

#     @property
#     def prev(self):
#         return self.__prev
    
#     @prev.setter
#     def prev(self, value):
#         self.__prev = value

#     @property
#     def next(self):
#         return self.__next
    
#     @next.setter
#     def next(self, value):
#         self.__next = value

#     @property
#     def data(self):
#         return self.__data
    
#     @data.setter
#     def data(self, value):
#         self.__data = value


# class LinkedList:
#     def __init__(self):
#         self.__head = None
#         self.__tail = None
#         self.__linked_list = []

#     def add_obj(self, obj):
#         if len(self.__linked_list) == 0:
#             self.__linked_list.append(obj)
#             self.__head = obj
#             self.__tail = obj
#         else:
#             self.__linked_list.append(obj)
#             self.__tail = obj
#             self.__tail.prev = self.__linked_list[-2]
#             self.__linked_list[-2].next = self.__tail

#     @property
#     def head(self):
#         return self.__head

#     @property
#     def tail(self):
#         return self.__tail
            
#     def remove_obj(self, indx):
#         if len(self.__linked_list) == 0:
#             self.__tail = None
#             self.__head = None
#         elif len(self.__linked_list) and indx == 0:
#             self.__linked_list = []
#             self.__tail = None
#             self.__head = None
#         else:
#             if indx == len(self.__linked_list) - 1:
#                 self.__linked_list[indx - 1].next = None
#                 self.__tail = self.__linked_list[indx - 1]
#                 self.__linked_list.pop(indx)
#             elif indx == 0:
#                 self.__linked_list[indx + 1].prev = None
#                 self.__head = self.__linked_list[indx + 1]
#                 self.__linked_list.pop(indx)
#             else:
#                 self.__linked_list[indx].prev = self.__linked_list[indx - 2].data
#                 self.__linked_list[indx - 2].next = self.__linked_list[indx].data

#     def __len__(self):
#         return len(self.__linked_list)
    
#     def __call__(self, indx):
#         return self.__linked_list[indx].data

# ln = LinkedList()
# ln.add_obj(ObjList("Сергей"))
# ln.add_obj(ObjList("Балакирев"))
# ln.add_obj(ObjList("Python ООП"))
# ln.remove_obj(2)
# assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
# ln.add_obj(ObjList("Python"))
# assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
# assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
# assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"
# # print(type(ln.head))
# # print(isinstance(ln.head, ObjList))
# # print(ln)
# n = 0
# h = ln.head


# while h:
#     print(h)
#     assert isinstance(h, ObjList)
#     h = h._ObjList__next
#     n += 1

# assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

# n = 0
# h = ln.tail
# while h:
#     assert isinstance(h, ObjList)
#     h = h._ObjList__prev
#     n += 1

# assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"

# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# linked_lst.remove_obj(2)
# linked_lst.add_obj(ObjList("Python ООП"))
# n = len(linked_lst)  # n = 3
# s = linked_lst(1) # s = Balakirev
# print(n, s, sep='\n')
# while len(ln):
#     print(len(ln))
#     ln.remove_obj(0)
#     print(len(ln))
# print(ln.head)
# print(ln.tail)
# assert ln.head is None and ln.tail is None, "при удалении всех объектов ссылки head и tail должны быть равны None"

# # 3
# class WordString:
#     def __init__(self, string = None):
#         self.__string = string

#     def __len__(self):
#         return len(self.__string.split())

#     def __call__(self, i):
#         return self.__string.split()[i]

#     @property
#     def string(self):
#         return self.__string

#     @string.setter
#     def string(self, value):
#         self.__string = value


# words1 = WordString("Курс по Python ООП")


# words = WordString()
# words.string = "Курс по Python ООП"
# n = len(words)
# print(n)
# first = "" if n == 0 else words(0)
# print(words.string)
# print(f"Число слов: {n}; первое слово: {first}")
# # 2
# class Model:
#     def __init__(self):
#          self.__db = 'Model'

#     def query(self, *args, **kwargs):
#         self.__db += ': '
#         for key, value in kwargs.items():
#             self.__db += f'{key} = {value}'
#             self.__db += ', '
#         self.__db = self.__db[:-2]
    
#     def __str__(self):
#          return self.__db

# model = Model()
# # model.query(id=1, fio='Sergey', old=33)

# print(model) # "Model: id = 1, fio = Sergey, old = 33"

# # 1
# import sys

# class Book:
#     def __init__(self, title, author, pages):
#         self.__title = title
#         self.__author = author
#         self.__pages = pages


#     def __str__(self):
#         return f"Книга: {self.__title}; {self.__author}; {self.__pages}"

# sys.stdin = open('3.3.py.txt', 'r', encoding='utf-8')
# # программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока

# book = Book(*lst_in)
# print(book)

# # 0.2

# class Point():
#     def __init__(self, *args):
#         self.__coords = args

#     def __len__(self):
#         return len(self.__coords)
    
#     def __abs__(self):
#         return list(map(abs, self.__coords))
    

# p = Point(1, -2, -5)
# print(len(p))
# print(abs(p))
# print(p.__dict__)

# # 0.1

# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
    
#     def __str__(self):
#         return f"{self.name}"
    

# cat = Cat("Васька")
# print(cat)
# str(cat)