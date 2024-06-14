# # 7
# class PhoneNumber:
#     def __init__(self, number, fio):
#         self.number = number
#         self.fio = fio


# class PhoneBook:
#     def __init__(self):
#         self.phone_list = []

#     def add_phone(self, phone):
#         self.phone_list.append(phone)

#     def remove_phone(self, indx):
#         self.phone_list.pop(indx)

#     def get_phone_list(self):
#         return self.phone_list
# 6
# class LineTo:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class PathLines:
#     def __init__(self, *args):
#         self.lines = [x for x in args]
#
#     def add_line(self, line):
#         self.lines.append(line)
#
#     def get_path(self):
#         return self.lines
#
#     def get_length(self):
#         """
#         :return: L = sqrt((x1-x0)^2 + (y1-y0)^2)
#         """
#         res = 0
#         if self.lines:
#             for i, line in enumerate(self.lines):
#                 x0 = 0
#                 y0 = 0
#                 if i >= 1:
#                     x0 = self.lines[i - 1].x
#                     y0 = self.lines[i - 1].y
#                 res += ((line.x - x0) ** 2 + (line.y - y0) ** 2) ** 0.5
#         return res
#
#
# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
# dist = p.get_length()
# print(dist)
# p = PathLines(LineTo(1, 2))
# print(p.get_length())  # 2.23606797749979
# p.add_line(LineTo(10, 20))
# p.add_line(LineTo(5, 17))
# print(p.get_length())  # 28.191631669843197
# m = p.get_path()
# print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True
#
# h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
# print(h.get_length())  # 71.8992593599813
#
# k = PathLines()
# print(k.get_length())  # 0
# print(k.get_path())  # []
# class LineTo:
#     def __init__(self, x, y):
#         self.y0 = 0
#         self.x0 = 0
#         self.x = x
#         self.y = y
#         self.next = None
#
#     @staticmethod
#     def add_prev(line_start, line_end):
#         line_start.next = line_end
#         line_end.x0 = line_start.x
#         line_end.y0 = line_start.y
#
#
# class PathLines:
#     def __init__(self, *args):
#         self.top = None
#         self.last = None
#         if args:
#             for arg in args:
#                 self.add_line(arg)
#
#     def add_line(self, line):
#         if self.top is None:
#             self.top = line
#         else:
#             LineTo.add_prev(self.last, line)
#         self.last = line
#
#     def get_path(self):
#         temp = self.top
#         res = []
#         while temp:
#             res.append(temp)
#             temp = temp.next
#         return res
#
#     def get_length(self):
#         """
#         :return: L = sqrt((x1-x0)^2 + (y1-y0)^2)
#         """
#         temp = self.top
#         res = 0
#         while temp:
#             res += () ** 0.5
# 5
# class TreeObj:
#     def __init__(self, indx, value=None):
#         self.indx = indx
#         self.value = value
#         self.__left = None
#         self.__right = None
#
#     @property
#     def left(self):
#         return self.__left
#
#     @left.setter
#     def left(self, value):
#         self.__left = value
#
#     @property
#     def right(self):
#         return self.__right
#
#     @right.setter
#     def right(self, value):
#         self.__right = value
#
#
# class DecisionTree:
#     @classmethod
#     def predict(cls, root, x):
#         temp = root
#         for _ in x:
#             if temp.left is None or temp.right is None:
#                 break
#             temp = temp.left if x[temp.indx] else temp.right
#         return temp.value
#
#     @classmethod
#     def add_obj(cls, obj, node=None, left=True):
#         if node:
#             if left:
#                 node.left = obj
#             else:
#                 node.right = obj
#         return obj
#
# assert hasattr(DecisionTree, 'add_obj') and hasattr(DecisionTree, 'predict'), "в классе DecisionTree должны быть методы add_obj и predict"
#
# assert type(TreeObj.left) == property and type(TreeObj.right) == property, "в классе TreeObj должны быть объекты-свойства left и right"
#
# root = DecisionTree.add_obj(TreeObj(0))
# v_11 = DecisionTree.add_obj(TreeObj(1), root)
# v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
# DecisionTree.add_obj(TreeObj(-1, "программист"), v_11)
# DecisionTree.add_obj(TreeObj(-1, "кодер"), v_11, False)
# DecisionTree.add_obj(TreeObj(-1, "посмотрим"), v_12)
# DecisionTree.add_obj(TreeObj(-1, "нет"), v_12, False)
#
# print(DecisionTree.predict(root, [0, 1, 0]))

#
# root = DecisionTree.add_obj(TreeObj(0))
# v_11 = DecisionTree.add_obj(TreeObj(1), root)
# v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
# DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
# DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
# DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
# DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)
#
# x = [1, 1, 0]
# res = DecisionTree.predict(root, x)  # будет программистом
# print(res)
# 4
# class RadiusVector2D:
#     MIN_COORD = -100
#     MAX_COORD = 1024
#
#     def __init__(self, *args):
#         self.__x = args[0] if len(args) in (1, 2) and self.check_value(args[0]) else 0
#         self.__y = args[1] if len(args) == 2 and self.check_value(args[1]) else 0
#
#     @classmethod
#     def check_value(cls, value):
#         return True if type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD else False
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if self.check_value(value):
#             self.__x = value
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if self.check_value(value):
#             self.__y = value
#
#     @staticmethod
#     def norm2(vector):
#         return vector.x ** 2 + vector.y ** 2
#
#
#
# a = RadiusVector2D(1, 2)
# print(a.x, a.y)
# print(RadiusVector2D.norm2(a))

# 3
# class StackObj:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, n):
#         if isinstance(n, StackObj) or n is None:
#             self.__next = n
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, data):
#         self.__data = data
#
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.last = None
#
#     def push(self, stack_obj):
#         if self.last:
#             self.last.next = stack_obj
#         self.last = stack_obj
#         if self.top is None:
#             self.top = stack_obj
#
#     def pop(self):
#         h = self.top
#         if h is None:
#             return
#         while h and h.next != self.last:
#             h = h.next
#         if h:
#             h.next = None
#         last = self.last
#         self.last = h
#         if self.last is None:
#             self.top = None
#         return last
#
#     def get_data(self):
#         res = []
#         temp = self.top
#         while temp:
#             res.append(temp.data)
#             temp = temp.next
#         return res
#
#
# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st.pop()
# st.pop()
# st.pop()
# res = st.get_data()  # ['obj1', 'obj2']
# print(res)

# 2
# class WindowDlg:
#     def __init__(self, title, width, height):
#         self.__title = title
#         self.__width = width
#         self.__height = height
#
#     def show(self):
#         print(f"{self.__title}: {self.__width}, {self.__height}")
#
#     @staticmethod
#     def __check_param(param):
#         return 0 <= param <= 10000
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, width):
#         if self.__check_param(width):
#             self.__width = width
#             self.show()
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, height):
#         if self.__check_param(height):
#             self.__height = height
#             self.show()

# 1
# class Car:
#     def __init__(self):
#         self.__model = None

#     @property
#     def model(self):
#         return self.__model

#     @model.setter
#     def model(self, model):
#         self.__model = model if isinstance(model, str) and 2 <= len(model) <= 100 else self.__model


# car = Car()
# car.model = "Toyota"
# print(car.model)
# car.model = "T"
# print(car.model)
