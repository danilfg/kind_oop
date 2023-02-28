# 5
class Graph:
    def __init__(self, data, is_show=True):
        self.data = data[:]
        self.is_show = is_show

    def set_data(self, data):
        self.data.append(data)

    def show_table(self):
        print(' '.join(list(map(str, self.data))) if self.is_show else "Отображение данных закрыто")

    def show_graph(self):
        print("Графическое отображение данных: " if self.is_show else "Отображение данных закрыто")

    def show_bar(self):
        print("Столбчатая диаграмма: " + ' '.join(
            list(map(str, self.data))) if self.is_show else "Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show


data_graph = list(map(int, "8 11 10 -32 0 7 18".split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(fl_show=False)
gr.show_table()
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
