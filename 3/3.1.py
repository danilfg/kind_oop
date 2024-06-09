# 8
# import time

# class GeyserClassic:
#     MAX_DATE_FILTER = 100

#     def __init__(self):
#         self.filter_class = ('Mechanical', 'Aragon', 'Calcium')
#         self.filters = {(1, self.filter_class[0]): None, 
#                         (2, self.filter_class[1]): None, 
#                         (3, self.filter_class[2]): None}

#     def add_filter(self, slot_num, filter):
#         key = (slot_num, filter.__class__.__name__)
#         if key in self.filters and not self.filters[key]:
#             self.filters[key] = filter

#     def remove_filter(self, slot_num):
#         if type(slot_num) == int and 1 <= slot_num <= 2:
#             key  = (slot_num, self.filter_class[slot_num - 1])
#             if key in self.filters:
#                 self.filters[key] = None

#     def get_filters(self):
#         return tuple(self.filters.values())

#     def water_on(self):
#         end = time.time()
#         for f in self.filters.values():
#                 if f is None:
#                     return False
#                 start = f.date
#                 if end - start > self.MAX_DATE_FILTER:
#                     return False
                
#         return True
    

# class Mechanical:
#     def __init__(self, date):
#         self.date = date

#     def __setattr__(self, key, value):
#         if key == 'date' and key in self.__dict__:
#             return
#         super().__setattr__(key, value) # чтобы создать элемент, если еще не создали

    
# class Aragon:
#     def __init__(self, date):
#         self.date = date

#     def __setattr__(self, key, value):
#         if key == 'date' and key in self.__dict__:
#             return
#         super().__setattr__(key, value) # чтобы создать элемент, если еще не создали


# class Calcium:
#     def __init__(self, date):
#         self.date = date

#     def __setattr__(self, key, value):
#         if key == 'date' and key in self.__dict__:
#             return
#         super().__setattr__(key, value) # чтобы создать элемент, если еще не создали


# my_water = GeyserClassic()
# my_water.add_filter(1, Mechanical(time.time()))
# my_water.add_filter(2, Aragon(time.time()))
# w = my_water.water_on() # False
# my_water.add_filter(3, Calcium(time.time()))
# w = my_water.water_on() # True
# f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
# my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
# my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно


# # 0
# from typing import Any


# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def set_coord(self, x, y):
#         if self.MIN_COORD <= x <= self.MAX_COORD:
#             self.x = x
#             self.y = y

#     def __getattribute__(self, item): # Вызывается при получении свойства класса с именем item
#         if item == "x":
#             raise ValueError("access error")
#         else:
#             # print("__getattribute__")
#             return object.__getattribute__(self, item)

#     def __setattr__(self, key, value): # Вызывается при изменении свойства key класса
#         if key == "z":
#             raise AttributeError("недлопустимое значение")
#         else:
#             # print("__setattr__")
#             object.__setattr__(self, key, value)
#             # self.__dict__[key] = value

#     def __getattr__(self, item): # Вызывается при получении несуществующего свойства item класса
#         # print("__getattr__: " + item)
#         return False

#     def __delattr__(self, item): # Вызывается при удалении свойства item (не выжно существует оно или нет)
#         print("__delattr__: " + item)
#         object.__delattr__(self, item)

# pt1 = Point(1, 2)
# pt2 = Point(10, 20)
# # a = pt1.x
# # pt1.z = 2
# print(pt1.yy)
# del pt1.x
# print(pt1.__dict__)



# # 7
# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 1000

#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     @property
#     def a(self):
#         return self.__a

#     @a.setter
#     def a(self, value):
#         if type(value) in (int, float) and self.check_dim(value):
#             self.__a = value

#     @property
#     def b(self):
#         return self.__b

#     @b.setter
#     def b(self, value):
#         if type(value) in (int, float) and self.check_dim(value):
#             self.__b = value

#     @property
#     def c(self):
#         return self.__c

#     @c.setter
#     def c(self, value):
#         if type(value) in (int, float) and self.check_dim(value):
#             self.__c = value

#     @classmethod
#     def check_dim(cls, value):
#         return True if cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION else False

#     def __setattr__(self, key, value):
#         if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
#             raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
#         object.__setattr__(self, key, value)


# d = Dimensions(10.5, 20.1, 30)
# d.a = 8
# d.b = 15
# a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
# d.MAX_DIMENSION = 10  # исключение AttributeError
# 6
# class Circle:
#     def __init__(self, x, y, radius):
#         self.x = x
#         self.y = y
#         self.radius = radius
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if type(value) not in (int, float):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         else:
#             self.__x = value
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if type(value) not in (int, float):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         else:
#             self.__y = value
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if type(value) not in (int, float):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         else:
#             self.__y = value
#
#     @property
#     def radius(self):
#         return self.__radius
#
#     @radius.setter
#     def radius(self, value):
#         if type(value) not in (int, float):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         elif value > 0:
#             self.__radius = value
#
#     def __getattr__(self, item):
#         return False
#
#
# circle = Circle(10.5, 7, 22)
# circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
# x, y = circle.x, circle.y
# res = circle.name # False, т.к. атрибут name не существует
# 5
# class SmartPhone:
#     def __init__(self, model):
#         self.model = model
#         self.apps = []
#
#     def add_app(self, app):
#         if all([type(app) != type(x) for x in self.apps]):
#             self.apps.append(app)
#
#     def remove_app(self, app):
#         self.apps.remove(app)
#
#
# class AppVK:
#     def __init__(self):
#         self.name = "ВКонтакте"
#
#
# class AppYouTube:
#     def __init__(self, memory_max):
#         self.memory_max = memory_max
#         self.name = "YouTube"
#
#
# class AppPhone:
#     def __init__(self, phone_list):
#         self.phone_list = phone_list
#         self.name = "Phone"
#
#
# sm = SmartPhone("Honor 1.0")
# sm.add_app(AppVK())
# sm.add_app(AppVK())  # второй раз добавляться не должно
# sm.add_app(AppYouTube(2048))
# for a in sm.apps:
#     print(a.name)

# 4
# class Museum:
#     def __init__(self, name):
#         self.name = name
#         self.exhibits = []
#
#     def add_exhibit(self, obj):
#         self.exhibits.append(obj)
#
#     def remove_exhibit(self, obj):
#         self.exhibits.remove(obj)
#
#     def get_info_exhibit(self, indx):
#         return f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}"
#
#
# class Picture:
#     def __init__(self, name, author, descr):
#         self.name = name
#         self.author = author
#         self.descr = descr
#
#
# class Mummies:
#     def __init__(self, name, location, descr):
#         self.name = name
#         self.location = location
#         self.descr = descr
#
#
# class Papyri:
#     def __init__(self, name, date, descr):
#         self.name = name
#         self.date = date
#         self.descr = descr
#
#
# mus = Museum("Эрмитаж")
# mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
# mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
# p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
# mus.add_exhibit(p)
# print(mus.get_info_exhibit(2))
# for x in mus.exhibits:
#     print(x.descr)
# 3
# class Course:
#     def __init__(self, name):
#         self.name = name
#         self.modules = []
#
#     def add_module(self, module):
#         self.modules.append(module)
#
#     def remove_module(self, indx):
#         self.modules.pop(indx)
#
#
# class Module:
#     def __init__(self, name):
#         self.name = name
#         self.lessons = []
#
#     def add_lesson(self, lesson):
#         self.lessons.append(lesson)
#
#     def remove_lesson(self, indx):
#         self.lessons.pop(indx)
#
#
# class LessonItem:
#     def __init__(self, title, practices, duration):
#         self.title = title
#         self.practices = practices
#         self.duration = duration
#
#     def __setattr__(self, key, value):
#         if key == 'title' and not isinstance(value, str):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         elif key in ('practices', 'duration') and (type(value) != int or value <= 0):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         else:
#             object.__setattr__(self, key, value)
#
#     def __getattr__(self, item):
#         return False
#
#     def __delattr__(self, item):
#         if item not in ('title', 'practices', 'duration'):
#             object.__delattr__(self, item)
#
#
# course = Course("Python ООП")
# module_1 = Module("Часть первая")
# module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
# module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
# module_1.add_lesson(LessonItem("Урок 3", 5, 800))
# course.add_module(module_1)
# module_2 = Module("Часть вторая")
# module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
# module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
# course.add_module(module_2)
# 2
# class Shop:
#     def __init__(self, name):
#         self.name = name
#         self.goods = []
#
#     def add_product(self, product):
#         self.goods.append(product)
#
#     def remove_product(self, product):
#         self.goods.remove(product)
#
#
# class Product:
#     ID = 0
#
#     def __new__(cls, *args, **kwargs):
#         cls.ID += 1
#         return super().__new__(cls)
#
#     def __init__(self, name, weight, price):
#         self.id = Product.ID
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def __setattr__(self, key, value):
#         if key == 'name' and type(value) != str:
#             raise TypeError("Неверный тип присваиваемых данных.")
#         elif key in ('weight', 'price') and (type(value) not in (int, float) or value < 0):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         else:
#             object.__setattr__(self, key, value)
#
#     def __delattr__(self, item):
#         if item == 'id':
#             raise AttributeError("Атрибут id удалять запрещено.")
#         else:
#             object.__delattr__(self, item)
#
#
# shop = Shop("Балакирев и К")
# book = Product("Python ООП", 100, 1024)
# shop.add_product(book)
# shop.add_product(Product("Python", 150, 512))
# for p in shop.goods:
#     print(f"{p.id}, {p.name}, {p.weight}, {p.price}")

# 1
# class Book:
#     def __init__(self, title='', author='', pages=0, year=0):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.year = year
#
#     def __setattr__(self, key, value):
#         if key in ('title', 'author') and type(value) != str:
#             raise TypeError("Неверный тип присваиваемых данных.")
#         elif key in ('pages', 'year') and type(value) != int:
#             raise TypeError("Неверный тип присваиваемых данных.")
#         else:
#             object.__setattr__(self, key, value)
#
#
# book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
#
# print(book.__dict__)
