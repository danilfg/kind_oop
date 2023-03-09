# 5
class Factory:
    def build_sequence(self):
        return []

    def build_number(self, string):
        return float(string)

class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
ld = Loader()
s = input()
res = ld.parse_format(s, Factory())
# 4
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def clone(self):
#         return Point(self.x, self.y)
#
#     # def clone(self):
#     #     new_clone = super().__new__(type(self))
#     #     new_clone.__dict__.update(self.__dict__)
#     #     return new_clone
#
#
# x = 2
# y = 3
# pt = Point(x, y)
# pt_clone = pt.clone()
# print(id(pt), pt.__dict__)
# print(id(pt_clone), pt.__dict__)
# 3
# TYPE_OS = 1  # 1 - Windows; 2 - Linux
#
#
# class DialogWindows:
#     name_class = "DialogWindows"
#
#
# class DialogLinux:
#     name_class = "DialogLinux"
#
#
# class Dialog:
#
#     def __new__(cls, *args, **kwargs):
#         if TYPE_OS == 1:
#             res = DialogWindows()
#         elif TYPE_OS == 2:
#             res = DialogLinux()
#         setattr(res, 'name', args[0])
#         return res
#
#
# dlg = Dialog("Test")
# print(dlg.name)
# 2
# class SingletonFive:
#     __instance = []
#
#     def __new__(cls, *args, **kwargs):
#         if len(cls.__instance) <= 4:
#             cls.__instance.append(super().__new__(cls))
#         return cls.__instance[-1]
#
#     def __init__(self, name):
#         self.name = name
#
#
# objs = [SingletonFive(str(n)) for n in range(10)]
#
# for obj in objs:
#     print(id(obj))

# 1
# class AbstractClass:
#
#     def __new__(cls, *args, **kwargs):
#         err = "Ошибка: нельзя создавать объекты абстрактного класса"
#         return err
#
#
# obj = AbstractClass()
# print(obj)
