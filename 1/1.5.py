# 8
from random import randint
from random import seed


class Cell:
    def __init__(self, around_mines, mine):
        """
        Параметры клетки
        :param around_mines: число мин вокруг клетки (начальное значение 0);
        :param mine: наличие мины в текущей клетке (True/False);
        """
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.mines = None
        self.pole = None
        self.N = N
        self.M = M
        self.init()

    def getMines(self):
        mines = []
        for _ in range(self.M):
            # ----
            x = randint(0, self.N - 1)
            y = randint(0, self.N - 1)
            while (x, y) in mines:
                x = randint(0, self.N - 1)
                y = randint(0, self.N - 1)
                continue
            # ----
            # while (x := randint(0, self.N - 1),
            #        y := randint(0, self.N - 1)) in mines:
            #     continue
            mines.append((x, y))
        return mines

    def checkMines(self):
        self.pole = [[Cell(0, False)] * self.N] + self.pole + [[Cell(0, False)] * self.N]
        for i in range(len(self.pole)):
            self.pole[i] = [Cell(0, False)] + self.pole[i] + [Cell(0, False)]
        for y, row in enumerate(self.pole):
            for x, cell in enumerate(row):
                if isinstance(cell, Cell) and cell.mine:
                    self.pole[y - 1][x - 1].around_mines += 1
                    self.pole[y - 1][x].around_mines += 1
                    self.pole[y - 1][x + 1].around_mines += 1
                    self.pole[y][x - 1].around_mines += 1
                    self.pole[y][x + 1].around_mines += 1
                    self.pole[y + 1][x - 1].around_mines += 1
                    self.pole[y + 1][x].around_mines += 1
                    self.pole[y + 1][x + 1].around_mines += 1
                    continue
        self.pole = self.pole[1:-1]
        for i in range(len(self.pole)):
            self.pole[i] = self.pole[i][1:-1]

    def init(self):
        self.mines = self.getMines()
        self.pole = [[0] * self.N for _ in range(self.N)]
        for y, row in enumerate(self.pole):
            for x, cell in enumerate(row):
                if (x, y) in self.mines:
                    self.pole[y][x] = Cell(0, True)
                else:
                    self.pole[y][x] = Cell(0, False)
        self.checkMines()

    def show(self):
        for p in self.pole:
            for c in p:
                if c.mine and c.fl_open:
                    print("*", end=' ')
                elif c.fl_open:
                    print(c.around_mines, end=' ')
                else:
                    print("#", end=' ')
            print()


pole_game = GamePole(10, 12)
for p in pole_game.pole:
    for c in p:
        c.fl_open = True
pole_game.show()
# for i in pole.pole:
#     print('y')
#     for u in i:
#         print(u, 'x', end=" | ")
#     print()
# 7
# import sys
#
#
# class ListObject:
#
#     def __init__(self, data):
#         self.data = data
#         self.next_obj = None
#
#     def link(self, obj):
#         self.next_obj = obj
#
#
# with open('1.5.py.txt', 'r', encoding='utf-8') as sys.stdin:
#     lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# res = [ListObject(data) for data in lst_in]
#
# for i in range(len(res)):
#     if i == len(res) - 1:
#         break
#     res[i].link(res[i+1])
#
# head_obj = res[0]
#
# print(len(lst_in))
# print(len(res))
# class Cart:
#     def __init__(self):
#         self.goods = []
#
#     def add(self, gd):
#         self.goods.append(gd)
#
#     def remove(self, indx):
#         del self.goods[indx]
#
#     def get_list(self):
#         return [f'{good.name}: {good.price}' for good in self.goods]
#
#
# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class TV:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Notebook:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Cup:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# cart = Cart()
# cart.add(TV('ТВ "Самсунг"', 15600))
# cart.add(TV('ТВ "Панасоник"', 25100))
#
# cart.add(Table('Стол "Эргостол"', 50000))
#
# cart.add(Notebook('Ноутбук "Эппл"', 1000000))
# cart.add(Notebook('Ноутбук "Леново"', 100000))
#
# cart.add(Cup('Кружка "Two Girl And One Cup"', 1))

# print(cart.get_list())
# 6
# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
#
#
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
#
#
# class MotherBoard:
#     def __init__(self, name, cpu, *mem_slots):
#         self.name = name
#         self.cpu = cpu
#         self.total_mem_slots = 4
#         self.mem_slots = mem_slots
#
#     def get_config(self):
#         memory = 'Память: '
#         for mem_slot in self.mem_slots:
#             memory += f'{mem_slot.name} - {mem_slot.volume}; '
#         memory = memory[:-2]
#         res = [f'Материнская плата: {self.name}',
#                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
#                f'Слотов памяти: {self.total_mem_slots}',
#                memory]
#         return res
#
#
# mb = MotherBoard('ASUS', CPU('Celeron', 1000), Memory('Kingstone', '2Gb'), Memory('Kingstone', '2Gb'))
# ("".join(mb.get_config())).replace(" ", "")
# mb.get_config()
# 5
# class Graph:
#     def __init__(self, data, is_show=True):
#         self.data = data[:]
#         self.is_show = is_show
#
#     def set_data(self, data):
#         self.data.append(data)
#
#     def show_table(self):
#         print(' '.join(list(map(str, self.data))) if self.is_show else "Отображение данных закрыто")
#
#     def show_graph(self):
#         print("Графическое отображение данных: " if self.is_show else "Отображение данных закрыто")
#
#     def show_bar(self):
#         print("Столбчатая диаграмма: " + ' '.join(
#             list(map(str, self.data))) if self.is_show else "Отображение данных закрыто")
#
#     def set_show(self, fl_show):
#         self.is_show = fl_show
#
#
# data_graph = list(map(int, "8 11 10 -32 0 7 18".split()))
# gr = Graph(data_graph)
# gr.show_bar()
# gr.set_show(fl_show=False)
# gr.show_table()
# 4
# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if not all(list(map(lambda x: ((type(x) == int)
#                                        or (type(x) == float))
#                                       and (x > 0),
#                             [self.a, self.b, self.c]))):
#             return 1
#         elif self.a + self.b < self.c \
#                 or self.a + self.c < self.b \
#                 or self.b + self.c < self.a:
#             return 2
#         else:
#             return 3
#
#
# a, b, c = map(int, input().split())
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())

# 3
# from random import random, choice, seed
# seed(1)
#
# class Line:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b,)
#         self.ep = (c, d,)
#
#     def set_zero(self):
#         self.sp = (0, 0,)
#         self.ep = (0, 0,)
#
#
# class Rect:
#     def __init__(self, a, b, c, d):
#         sp = (a, b,)
#         ep = (c, d,)
#
#
# class Ellipse:
#     def __init__(self, a, b, c, d):
#         sp = (a, b,)
#         ep = (c, d,)
#
#
# classes = [Line(random, random, random, random),
#            Rect(random, random, random, random),
#            Ellipse(random, random, random, random)]
# elements = [choice(classes) for _ in range(217)]
#
# for element in elements:
#     if isinstance(element, Line):
#         element.set_zero()
# print(len(elements))
# print(elements[:10])
# print(str(elements[0].sp))
# 2
# class Point:
#     def __init__(self, x, y, color='black'):
#         self.x = x
#         self.y = y
#         self.color = color
#
#
# points = []
#
# for i in range(1, 2000, 2):
#     if i == 3:
#         points.append(Point(i, i, 'yellow'))
#     else:
#         points.append(Point(i, i))
#
# print(points[1].color)
# print(len(points))
# 1
# class Money:
#
#     def __init__(self, money):
#         self.money = money
#
#
# my_money = Money(100)
# your_money = Money(1000)
# print(my_money.__dict__)
# print(your_money.__dict__)
