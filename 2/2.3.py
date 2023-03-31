# 5
class TVProgram:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.ids = []

    def add_telecast(self, tl):
        self.items.append(tl)
        self.ids.append(tl.uid)

    def remove_telecast(self, indx):
        self.items.pop(self.ids.index(indx))
        self.ids.pop(self.ids.index(indx))

class Telecast:
    def __init__(self, id, name, duration):
        self.__uid = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__uid

    @uid.setter
    def uid(self, value):
        self.__uid = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value


pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
pr.remove_telecast(2)
for t in pr.items:
    print(f"{t.name}: {t.duration}")
# 4
#
# class Bag:
#     def __init__(self, max_weight):
#         self.max_weight = max_weight
#         self.__things = []
#         self.sum_weight = 0
#
#     def add_thing(self, thing):
#         if self.sum_weight + thing.weight <= self.max_weight:
#             self.__things.append(thing)
#             self.sum_weight += thing.weight
#
#     def remove_thing(self, indx):
#         self.__things.pop(indx)
#
#     def get_total_weight(self):
#         return self.sum_weight
#
#     @property
#     def things(self):
#         return self.__things
#
#
# class Thing:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#
# bag = Bag(1000)
# bag.add_thing(Thing("Книга по Python", 100))
# bag.add_thing(Thing("Котелок", 500))
# bag.add_thing(Thing("Спички", 20))
# bag.add_thing(Thing("Бумага", 100))
# bag.add_thing(Thing("Бумага21", 1000))
# bag.remove_thing(2)
# w = bag.get_total_weight()
#
# for t in bag.things:
#     print(f"{t.name}: {t.weight}")

# 3
# class SuperShop:
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
# class StringValue:
#     def __init__(self, min_length, max_length):
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if type(value) == str and self.min_length <= len(value) <= self.max_length:
#             setattr(instance, self.name, value)
#
#
# class PriceValue:
#     def __init__(self, max_value, min_value=0):
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if type(value) == int and self.min_value <= value <= self.max_value:
#             setattr(instance, self.name, value)
#
#
# class Product:
#     name = StringValue(2, 50)
#     price = PriceValue(10000)
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# shop = SuperShop("У Балакирева")
# shop.add_product(Product("Курс по Python", 0))
# shop.add_product(Product("Курс по Python ООП", 2000))
# for p in shop.goods:
#     print(f"{p.name}: {p.price}")
# 2
# class ValidateString:
#     def __init__(self, min_length, max_length):
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def validate(self, string):
#         res = True if type(string) == str and self.min_length <= len(string) <= self.max_length else False
#         return res
#
#
# class StringValue:
#     def __init__(self, validator):
#         self.validator = validator
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if self.validator.validate(value):
#             setattr(instance, self.name, value)
#             # instance.__dict__[self.name] = value
#
#
# class RegisterForm:
#     login = StringValue(ValidateString(3, 100))
#     password = StringValue(ValidateString(3, 100))
#     email = StringValue(ValidateString(3, 100))
#
#     def __init__(self, login, password, email):
#         self.login = login
#         self.password = password
#         self.email = email
#
#     def get_fields(self):
#         return [self.login, self.password, self.email]
#
#     def show(self):
#         print(f"""<form>
# Логин: {self.login}
# Пароль: {self.password}
# Email: {self.email}
# </form>""")
#
#
# form = RegisterForm("логин", "пароль", "email")
# print(form.get_fields())
# form.show()
# 1
# class FloatValue:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if type(value) == float:
#             instance.__dict__[self.name] = value
#         else:
#             raise TypeError("Присваивать можно только вещественный тип данных.")
#
#
# class Cell:
#     value = FloatValue()
#
#     def __init__(self, value):
#         self.value = value
#
#
# class TableSheet:
#
#     def __init__(self, N, M):
#         self.cells = [[Cell(0.0) for _ in range(M)] for _ in range(N)]
#
#
# table = TableSheet(5, 3)
# value = 1.0
# for row in table.cells:
#     for cell in row:
#         cell.value = value
#         value += 1
#
# for row in table.cells:
#     print(*[cell.value for cell in row])
# class Integer:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         print(f"__set__: {self.name} = {value}")
#         instance.__dict__[self.name] = value
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# pt = Point3D(1, 2, 3)
# print(pt.__dict__)
