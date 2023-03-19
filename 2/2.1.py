

# 7
# from random import choice, randint
# from string import ascii_lowercase, digits
#
#
# class EmailValidator:
#     CHARS = ascii_lowercase + digits + '_.'
#     HOST = 'gmail.com'
#     MIN_LEN_EMAIL = 3
#     MAX_LEN_EMAIL = 7
#
#     def __new__(cls):
#         return None
#
#     @classmethod
#     def get_random_email(cls):
#         email = ''.join([choice(cls.CHARS) for _ in range(randint(cls.MIN_LEN_EMAIL, cls.MAX_LEN_EMAIL))])
#         email += '@' + cls.HOST
#         return email
#
#     @classmethod
#     def check_email(cls, email):
#         if cls.__is_email_str(email):
#             result = any(char in cls.CHARS for char in email)
#             try:
#                 idx = email.index('@')
#                 result = result and '.' in email[idx:]
#             except ValueError:
#                 return False
#
#             result = result and email.count('@') == 1
#             result = result and '..' not in email
#             result = result and len(email[:idx]) <= 100 and len(email[idx + 1:]) <= 100
#             return result
#
#     @staticmethod
#     def __is_email_str(email):
#         return type(email) == str
#
#
# print(EmailValidator.get_random_email())
# print(EmailValidator.check_email("sc_lib@list.ru"))  # True
# print(EmailValidator.check_email("pz@.2kO"))  # True

# print(EmailValidator.check_email("sc_lib@list_ru"))  # False)
# 6
# class LinkedList:
#     def __init__(self):
#         self.tail = None
#         self.head = None
#         self.linked_list = []
#
#     def add_obj(self, obj):
#         self.linked_list.append(obj)
#         self.tail = obj
#         if len(self.linked_list) == 1:
#             self.head = obj
#         else:
#             self.linked_list[-2].set_next(self.linked_list[-1])
#             self.linked_list[-1].set_prev(self.linked_list[-2])
#
#     def remove_obj(self):
#         if len(self.linked_list) > 0:
#             self.linked_list = self.linked_list[:-1]
#             if len(self.linked_list) > 1:
#                 self.linked_list[-1].set_next(None)
#                 self.tail = self.linked_list[-1]
#
#     def get_data(self):
#         return [x.get_data() for x in self.linked_list]
#
#
# class ObjList:
#     def __init__(self, data):
#         self.__data = None
#         self.__prev = None
#         self.__next = None
#         self.set_data(data)
#
#     def set_next(self, obj):
#         self.__next = obj
#
#     def set_prev(self, obj):
#         self.__prev = obj
#
#     def get_next(self):
#         return self.__next
#
#     def get_prev(self):
#         return self.__prev
#
#     def set_data(self, data):
#         self.__data = data
#
#     def get_data(self):
#         return self.__data
#
#
# lst = LinkedList()
# lst.add_obj(ObjList("данные 1"))
# lst.add_obj(ObjList("данные 2"))
# lst.add_obj(ObjList("данные 3"))
# lst.remove_obj()
# lst.remove_obj()
# lst.remove_obj()
# res = lst.get_data()  # ['данные 1', 'данные 2', 'данные 3']
# print(res)

# __next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
# __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
# __data - строка с данными.
#
# Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:
#
# set_next(self, obj) - изменение приватного свойства __next на значение obj;
# set_prev(self, obj) - изменение приватного свойства __prev на значение obj;
# get_next(self) - получение значения приватного свойства __next;
# get_prev(self) - получение значения приватного свойства __prev;
# set_data(self, data) - изменение приватного свойства __data на значение data;
# get_data(self) - получение значения приватного свойства __data.


# 5
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#
# class Rectangle:
#     def __init__(self, *args):
#         self.__ep = None
#         self.__sp = None
#         self.set_coords(*args if type(args[0]) == Point else [Point(args[0], args[1]), Point(args[2], args[3])])
#
#     def set_coords(self, sp, ep):
#         self.__sp = sp
#         self.__ep = ep
#
#     def get_coords(self):
#         return self.__sp, self.__ep
#
#     def draw(self):
#         print(f"Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}")
#
#
# x1, y1 = (0, 0)
# x2, y2 = (20, 34)
# rect = Rectangle(Point(x1, y1), Point(x2, y2))
# point = Point(1, 2)
# print(type(point) == Point)
#
#
# r1 = Rectangle(Point(x1, y1), Point(x2, y2))
# r2 = Rectangle(x1, y1, x2, y2)
# print(r1.get_coords())
# print(r2.get_coords())
# print(r1.draw())
# print(r2.draw())
# 4
# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.__y2 = None
#         self.__x2 = None
#         self.__y1 = None
#         self.__x1 = None
#         self.set_coords(x1, y1, x2, y2)
#
#     def set_coords(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
#
#     def get_coords(self):
#         return self.__x1, self.__y1, self.__x2, self.__y2
#
#     def draw(self):
#         print(self.__x1, self.__y1, self.__x2, self.__y2)
#
#
# x1 = 2
# y1 = 3
# x2 = 4
# y2 = 5
# line = Line(x1, y1, x2, y2)
# print(line.get_coords())
# line.set_coords(5, 6, 7, 8)
# line.draw()
# 3
# class Book:
#     def __init__(self, author, title, price):
#         self.__author = author
#         self.__title = title
#         self.__price = price
#
#     def set_title(self, title):
#         self.__title = title
#
#     def set_author(self, author):
#         self.__author = author
#
#     def set_price(self, price):
#         self.__price = price
#
#     def get_title(self):
#         return self.__title
#
#     def get_author(self):
#         return self.__author
#
#     def get_price(self):
#         return self.__price
#
# set_title(self, title) - запись в локальное приватное свойство __title объектов класса Book значения title;
# set_author(self, author) - запись в локальное приватное свойство __author объектов класса Book значения author;
# set_price(self, price) - запись в локальное приватное свойство __price объектов класса Book значения price;
# get_title(self) - получение значения локального приватного свойства __title объектов класса Book;
# get_author(self) - получение значения локального приватного свойства __author объектов класса Book;
# get_price(self) - получение значения локального приватного свойства __price объектов класса Book;
# 2
# class Money:
#     def __init__(self, money):
#         if self.__check_money(money):
#             self.set_money(money)
#
#     def set_money(self, money):
#         if self.__check_money(money):
#             self.__money = money
#
#     def get_money(self):
#         return self.__money
#
#     def add_money(self, mn):
#         self.__money += mn.get_money()
#
#     @staticmethod
#     def __check_money(money):
#         return type(money) == int and money >= 0
#
#
# mn_1 = Money(10)
# mn_2 = Money(20)
# mn_1.set_money(100)
# mn_2.add_money(mn_1)
# m1 = mn_1.get_money()    # 100
# m2 = mn_2.get_money()    # 120
# print(m1)
# print(m2)
# 1
# class Clock:
#     def __init__(self, time):
#         self.__time = 0
#         if self.__check_time(time):
#             self.__time = time
#
#     def set_time(self, tm):
#         if self.__check_time(tm):
#             self.__time = tm
#
#     def get_time(self):
#         return self.__time
#
#     @staticmethod
#     def __check_time(tm):
#         return type(tm) == int and 0 <= tm < 100000
#
#
# clock = Clock(4530)
#
# print(clock.get_time())
