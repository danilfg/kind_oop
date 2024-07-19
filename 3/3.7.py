# # 6
# class Vector:
#     def __init__(self, *args):
#         self.coords = list(args)
    
#     @staticmethod
#     def check_len(s, o):
#         if len(s.coords) != len(o.coords):
#             raise ArithmeticError('размерности векторов не совпадают')
#         return True
    
#     def __add__(self, other):
#         if isinstance(other, int):
#             res = [item + other for item in self.coords]
#             return Vector(*res)
#         if self.check_len(self, other):
#             res = list(map(sum, zip(self.coords, other.coords)))
#             return Vector(*res)
            
#     def __iadd__(self, other):
#         if isinstance(other, int):
#             self.coords = [item + other for item in self.coords]
#             return self
#         if self.check_len(self, other):
#             self.coords = list(map(sum, zip(self.coords, other.coords)))
#             return self

#     def __sub__(self, other):
#         if isinstance(other, int):
#             res = [item - other for item in self.coords]
#             return Vector(*res)
#         if self.check_len(self, other):
#             res = [i - j for i, j in zip(self.coords, other.coords)]
#             return Vector(*res)
        
#     def __isub__(self, other):
#         if isinstance(other, int):
#             self.coords = [item - other for item in self.coords]
#             return self
#         if self.check_len(self, other): 
#             self.coords = [i - j for i, j in zip(self.coords, other.coords)]
#             return self

#     def __mul__(self, other):
#         res = [i * j for i, j in zip(self.coords, other.coords)]
#         return Vector(*res)

#     def __eq__(self, other):
#         return self.coords == other.coords
        


# v1 = Vector(1,2,3,4)
# v2 = Vector(4,3,2,1)
# v3 = v1 + v2
# v4 = v1 + 10
# print('v3', v3.coords)
# print('v4', v4.coords)


# 5
import random


class GamePole:
    __instance = None

    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.mines = tuple()
        self.__pole_cells = (())
        
    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    @property
    def pole(self):
        return self.__pole_cells
    
    def create_pole(self):
        self.__pole_cells = tuple()
        for _ in range(self.N):
            tmp = tuple()
            for _ in range(self.M):
                tmp += (Cell(),)
            self.__pole_cells += (tmp,)
    
    def create_ids_mines(self):
        for _ in range(self.total_mines):
            self.mines += ((random.randint(0, self.N - 1), random.randint(0, self.M - 1)),)

    def init_pole(self):
        self.create_pole()
        self.create_ids_mines()
        # print(self.mines)
        for i, j in self.mines:
            self.__pole_cells[i][j].is_mine = True
            if (i - 1 >= 0) and (j - 1 >= 0):
                self.__pole_cells[i - 1][j - 1].number += 1
            if i - 1 >= 0:
                self.__pole_cells[i - 1][j].number += 1
            if (i - 1 >= 0) and (j + 1 <= len(self.__pole_cells[0]) - 1):
                self.__pole_cells[i - 1][j + 1].number += 1
            if j - 1 >= 0:
                self.__pole_cells[i][j - 1].number += 1
            if j + 1 <= len(self.__pole_cells[0]) - 1:
                self.__pole_cells[i][j + 1].number += 1
            if (i + 1 <= len(self.__pole_cells) - 1) and (j - 1 >= 0):
                self.__pole_cells[i + 1][j - 1].number += 1
            if i + 1 <= len(self.__pole_cells) - 1:
                self.__pole_cells[i + 1][j].number += 1
            if (i + 1 <= len(self.__pole_cells) - 1) and (j + 1 <= len(self.__pole_cells[0]) - 1):
                self.__pole_cells[i + 1][j + 1].number += 1
    def open_cell(self, i, j):
        if (i > len(self.__pole_cells) - 1) or (j > len(self.__pole_cells[0]) - 1):
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.__pole_cells[i][j].is_open = True

    def show_pole(self):
        for row in self.__pole_cells:
            for c in row:
                if c.is_open:
                    if c.is_mine:
                        print('M', end=' ')
                    else:
                        print(c.number, end=' ')
                else:
                    print('+', end=' ')
            print()
            
    def show_pole_cheat(self):
        for row in self.__pole_cells:
            for c in row:
                if c.is_mine:
                    print('M', end=' ')
                else:
                    print(c.number, end=' ')
            print()
    

class Cell:
    
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False
    
    @property
    def is_mine(self):
        return self.__is_mine
    
    @is_mine.setter
    def is_mine(self, value):
        self.__is_mine = value
        
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, value):
        self.__number = value
    
    @property
    def is_open(self):
        return self.__is_open
    
    @is_open.setter
    def is_open(self, value):
        self.__is_open = value
        
    def __setattr__(self, key, value):
        if (key in ('_Cell__is_mine', '_Cell__is_open') and not isinstance(value, bool)) \
            or (key == '_Cell__number' and (not (0 <= value <= 8) or not isinstance(value, int))):
            raise ValueError("недопустимое значение атрибута")
        super().__setattr__(key, value)
    
    def __bool__(self):
        return not self.is_open

# pole = GamePole(N, M, total_mines)
# c1 = Cell()
# c1.is_mine = True
# # c1.number = 9

# print(c1.is_open)
# c1.is_open = True
# print(c1.is_open)

# c2 = Cell()
# pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
# pole.init_pole()
# pole.show_pole()
pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
# print(pole.pole[3][5])
if pole.pole[3][5]:
    pole.open_cell(3, 5)
# pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.open_cell(3, 5)
print(len(pole.mines))
# pole.show_pole_cheat()
# pole.show_pole()

# pole.show_pole()
# # 4
# class Ellipse:
#     def __init__(self, *args):
#         if args:
#             self.x1, self.y1, self.x2, self.y2 = args[0], args[1], args[2], args[3]
            
#     def __bool__(self):
#         return len(self.__dict__) == 4

#     def get_coords(self):
#         try:
#             return (self.x1, self.y1, self.x2, self.y2)
#         except:
#             raise AttributeError('нет координат для извлечения')


# lst_geom = [Ellipse(), Ellipse(), Ellipse(2, 3, 4, 5), Ellipse(2, 3, 4, 5)]

# for item in lst_geom:
#     if bool(item):
#         item.get_coords()

# a1 = Ellipse()
# print(a1.__dict__)

# a1 = Ellipse(2, 3, 4, 5)
# print(len(a1.__dict__))
# # 3
# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.x2 = x2
#         self.y1 = y1
#         self.y2 = y2
        
#     def __len__(self):
#         l = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5
#         return False if l < 1 else True

# line = Line(0, 0, 0.5, 0.5)
# print(bool(line))


# # 2
# import sys


# class MailBox:
#     def __init__(self):
#         self.inbox_list = []
    
#     def receive(self):
#         # sys.stdin = open('3.7.2.py.txt', 'r', encoding='utf-8')
#         lst_in = list(map(str.strip, sys.stdin.readlines()))
#         self.inbox_list += list(map(lambda x: MailItem(*x.split('; ')), lst_in))
        


        
# class MailItem:
#     def __init__(self, mail_from, title, content):
#         self.mail_from = mail_from
#         self.title = title
#         self.content = content
#         self.is_read = False
        
#     def set_read(self, fl_read):
#         self.is_read = fl_read
        
#     def __bool__(self):
#         return self.is_read
    
#     def __repr__(self):
#         return f"{self.mail_from}: {self.is_read}"
        
# mail = MailBox()
# mail.receive()
# mail.inbox_list[0].set_read(True)
# mail.inbox_list[-1].set_read(True)
# inbox_list_filtered = list(filter(bool, mail.inbox_list))
# print(*inbox_list_filtered, sep='\n')
# # 1
# import sys


# class Player:
#     def __init__(self, name, old, score):
#         self.name = name
#         self.old = int(old)
#         self.score = int(score)
        
#     def __bool__(self):
#         return self.score > 0
    
#     def __repr__(self):
#         return f"{self.name}: {self.score}"


# sys.stdin = open('3.7.1.py.txt', 'r', encoding='utf-8')
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# players = list(map(lambda x: Player(*x.split('; ')), lst_in))
# players_filtered = list(filter(bool, players))

# print(players)
# print(players_filtered)
# # 0
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __len__(self):
#         print("__len__")
#         return self.x * self.x + self.y * self.y
    
#     def __bool__(self):
#         print("__bool__")
#         return self.x == self.y


# p1 = Point(3, 4)
# p2 = Point(0, 0)
# print('p1', len(p1), bool(p1))
# print('p2', len(p2), bool(p2))

# # где используется

# if p1:
#     print("объект p1 дает True")
# else:
#     print("объект p1 дает False")
    