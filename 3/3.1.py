# 3
class Course:
    pass


class Module:
    pass


class LessonItem:
    pass



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
