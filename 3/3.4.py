# 6
class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
        
    def __add__(self, other):
        return Box3D(self.width + other.width, self.height + other.height, self.depth + other.depth)

    def __mul__(self, other):
        return Box3D(self.width * other, self.height * other, self.depth * other)
    
    def __rmul__(self, other):
        return self * other
    
    def __sub__(self, other):
        return Box3D(self.width - other.width, self.height - other.height, self.depth - other.depth)
    
    def __floordiv__(self, other):
        return Box3D(self.width // other, self.height // other, self.depth // other)
    
    def __mod__(self, other):
        return Box3D(self.width % other, self.height % other, self.depth % other)
        
# # 5
# class Budget:
#     def __init__(self):
#         self.__items = []
        
#     def add_item(self, it):
#         self.__items.append(it)
        
#     def remove_item(self, indx):
#         self.__items.pop(indx)
        
#     def get_items(self):
#         return self.__items
    

    
    
# class Item:
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
        
#     def __add__(self, other):
#         s = self.money + other.money
#         return s
    
#     def __radd__(self, other):
#         return other + self.money

# my_budget = Budget()
# my_budget.add_item(Item("Курс по Python ООП", 2000))
# my_budget.add_item(Item("Курс по Django", 5000.01))
# my_budget.add_item(Item("Курс по NumPy", 0))
# my_budget.add_item(Item("Курс по C++", 1500.10))

# # вычисление общих расходов
# s = 0
# for x in my_budget.get_items():
#     s = s + x
# # 4
# class Lib:
#     def __init__(self):
#         self.book_list = []
    
#     def __add__(self, other):
#         self.book_list.append(other)
#         return self
    
#     def __sub__(self, other):
#         if isinstance(other, int):
#             self.book_list.pop(other)
#         else:
#             self.book_list.remove(other)
#         return self
    
#     def __len__(self):
#         return len(self.book_list)
    
    
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
        


# lib = Lib()

# lib = lib + book # добавление новой книги в библиотеку
# lib += book
# lib = lib - book # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
# lib -= book

# lib = lib - indx # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
# lib -= indx

# # 3
# class Stack:
#     def __init__(self):
#         self.__stack_objs = []
#         self.top = None
        
#     def push_back(self, obj):
#         if not self.top:
#             self.top = obj
#         else:
#             self.__stack_objs[-1].next = obj
#         self.__stack_objs.append(obj)
            
#     def pop_back(self):
#         if self.__stack_objs:
#             self.__stack_objs = self.__stack_objs[:-1]
#         if not self.__stack_objs:
#             self.top = None
#         self.__stack_objs[-1].next = None
        
#     def __add__(self, other):
#         self.push_back(other)
#         return self
    
#     def __mul__(self, others):
#         for other in others:
#             self.push_back(StackObj(other))
#         return self

#     def __len__(self):
#         return len(self.__stack_objs)

# class StackObj:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
        
#     @property
#     def next(self):
#         return self.__next
    
#     @next.setter
#     def next(self, value):
#         self.__next = value


# assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

# st = Stack()
# top = StackObj("1")
# st.push_back(top)
# assert st.top == top, "неверное значение атрибута top"
# print('GAVNO', st._Stack__stack_objs[0]._StackObj__data)
# st = st + StackObj("2")
# print('GAVNO', st._Stack__stack_objs[0]._StackObj__data)
# st = st + StackObj("3")
# obj = StackObj("4")
# st += obj
# st = st * ['data_1', 'data_2']
# st *= ['data_3', 'data_4']
# st += StackObj("225")
# st.pop_back()
# print(st.__dict__)
# d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']

# h = top
# print(h.__dict__)
# i = 0
# print(len(st))
# print(len(d))
# print(st._Stack__stack_objs[0]._StackObj__data)
# # print(h.__dict__)
# while h:
#     print(h.__dict__)
    
#     assert h._StackObj__data == d[i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
#     h = h._StackObj__next
#     i += 1
    
# # print(i)

    
# assert i == len(d), "неверное число объектов в стеке"

# obj = StackObj('data')
# # добавление нового объекта класса StackObj в конец односвязного списка st
# st = Stack()
# print(1, len(st))
# st.push_back(StackObj('123'))
# print(2, len(st))
# st = st + obj
# print(3, len(st))
# st.pop_back()
# print(4, st.__dict__)
# print(4, len(st))
# st += obj
# print(5, len(st))

# # добавление нескольких объектов в конец односвязного списка
# st = st * ['data_1', 'data_2', 'data_N']
# print(6, len(st))

# st *= ['data_1', 'data_2', 'data_N']
# print(7, len(st))


# # 2
# class ListMath:
#     def __init__(self, lst: list = None):
#         self.lst_math = self.check_list(lst if lst and type(lst) == list else [])
    
#     @staticmethod
#     def check_list(items):
#         return [x for x in items if isinstance(x, (int, float)) and not isinstance(x, bool)]
    
#     def __add__(self, other): #  Class + other
#         return ListMath([x + other for x in self.lst_math])
    
#     def __radd__(self, other): # other + Class
#         return self + other
    
#     def __iadd__(self, other): # Class += other
#         self.lst_math = [x + other for x in self.lst_math]
#         return self
    
#     def __sub__(self, other): #  Class + other
#         return ListMath([x - other for x in self.lst_math])
    
#     def __rsub__(self, other): # other + Class
#         return ListMath([other - x for x in self.lst_math])
    
#     def __isub__(self, other): # Class += other
#         self.lst_math = [x - other for x in self.lst_math]
#         return self
    
#     def __mul__(self, other): #  Class + other
#         return ListMath([x * other for x in self.lst_math])
    
#     def __rmul__(self, other): # other + Class
#         return self * other
    
#     def __imul__(self, other): # Class += other
#         self.lst_math = [x * other for x in self.lst_math]
#         return self

#     def __truediv__(self, other): #  Class + other
#         return ListMath([x / other for x in self.lst_math])
    
#     def __rtruediv__(self, other): # other + Class
#         if 0 in self.lst_math:
#             raise ZeroDivisionError()
#         return ListMath([other / x for x in self.lst_math])
    
#     def __itruediv__(self, other): # Class += other
#         self.lst_math = [x / other for x in self.lst_math]
#         return self

# lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]

# lst = lst + 76 # сложение каждого числа списка с определенным числом
# print(lst.__dict__)
# lst = 6.5 + lst # сложение каждого числа списка с определенным числом
# print(lst.__dict__)
# lst += 76.7  # сложение каждого числа списка с определенным числом
# print(lst.__dict__)
# lst = lst - 76 # вычитание из каждого числа списка определенного числа
# lst = 7.0 - lst # вычитание из числа каждого числа списка
# lst -= 76.3
# lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
# lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
# lst *= 5.54
# lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
# lst = 3 / lst # деление числа на каждый элемент списка
# lst /= 13.0
# # 1
# class NewList:
#     def __init__(self, items: list = []):
#         self.__new_list = items

#     def get_list(self):
#         return self.__new_list
    
#     def __sub__(self, other):
#         a = self.__new_list
#         b = other
#         if isinstance(other, NewList):
#                 b = other.__new_list
#         a = [str(x) if isinstance(x, bool) else x for x in a]
#         b = [str(x) if isinstance(x, bool) else x for x in b]
#         for x in b:
#             if x in a:
#                 a.remove(x)
#         a = [True if x == 'True' else False if x in ('True', 'False') else x for x in a]
#         return NewList(a)
        
#     def __rsub__(self, other): # for Class = 100 + Class
#         return NewList(other) - self

# lst = NewList()
# lst1 = NewList([0, 1, -3.4, "abc", True])
# lst2 = NewList([1, 0, True])

# assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"

# res1 = lst1 - lst2
# res2 = lst1 - [0, True]
# print()
# res3 = [1, 2, 3, 4.5] - lst2
# lst1 -= lst2

# assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
# assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
# assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
# assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

# lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
# lst_2 = NewList([10, True, False, True, 1, 7.87])
# res = lst_1 - lst_2
# assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
# assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"
# lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
# lst2 = NewList([0, 1, 2, 3, True])
# res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
# lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
# res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
# res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]

# # 0
# class Clock:
#     __DAY = 86400
    
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError("Seconds must be integer")
#         self.seconds = seconds % self.__DAY
        
#     def get_time(self):
#         s = self.seconds % 60
#         m = (self.seconds // 60) % 60
#         h = (self.seconds // 3600) % 24
#         return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"
        
#     @classmethod
#     def __get_formatted(cls, x):
#         return str(x).rjust(2, "0")
    
#     def __add__(self, other): # for Class = Class + 100 or Class + Class
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError("Operand must be integer or class Clock")
#         sc = other
#         if isinstance(other, Clock):
#                 sc = other.seconds
#         return Clock(self.seconds + sc)
    
#     def __radd__(self, other): # for Class = 100 + Class
#         return self + other
    
#     def __iadd__(self, other): # for Class += 100, without this will create new Class
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError("Operand must be integer or class Clock")
#         sc = other
#         if isinstance(other, Clock):
#                 sc = other.seconds
#         self.seconds += sc
#         return self
    
# c1 = Clock(1000)
# c1 = c1 + 1000 # для def __add__(self, other), где other то что справа от плюса
# c2 = Clock(1000)
# c3 = c1 + c2
# print(c3.get_time())
# c4 = 100 + c1
# print(c4.get_time())
# c4 = 100 + c1
# print(c1.get_time())

