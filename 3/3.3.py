# 2
class Model:
    def __init__(self):
         self.__db = 'Model'

    def query(self, *args, **kwargs):
         self.__db += ': '
         for arg in args:
            self.__db += arg
            self.__db += ', '

    def __str__(self):
         
         return()

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