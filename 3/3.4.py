# 2
class ListMath:
    def __init__(self, lst: list = None):
        self.lst_math = self.check_list(lst if lst and type(lst) == list else [])
    
    @staticmethod
    def check_list(items):
        return [x for x in items if isinstance(x, (int, float)) and not isinstance(x, bool)]
    
    def __add__(self, other): #  Class + other
        return ListMath([x + other for x in self.lst_math])
    
    def __radd__(self, other): # other + Class
        return self + other
    
    def __iadd__(self, other): # Class += other
        self.lst_math = [x + other for x in self.lst_math]
        return self
    
    def __sub__(self, other): #  Class + other
        return ListMath([x - other for x in self.lst_math])
    
    def __rsub__(self, other): # other + Class
        return ListMath([other - x for x in self.lst_math])
    
    def __isub__(self, other): # Class += other
        self.lst_math = [x - other for x in self.lst_math]
        return self
    
    def __mul__(self, other): #  Class + other
        return ListMath([x * other for x in self.lst_math])
    
    def __rmul__(self, other): # other + Class
        return self * other
    
    def __imul__(self, other): # Class += other
        self.lst_math = [x * other for x in self.lst_math]
        return self

    def __truediv__(self, other): #  Class + other
        return ListMath([x / other for x in self.lst_math])
    
    def __rtruediv__(self, other): # other + Class
        if 0 in self.lst_math:
            raise ZeroDivisionError()
        return ListMath([other / x for x in self.lst_math])
    
    def __itruediv__(self, other): # Class += other
        self.lst_math = [x / other for x in self.lst_math]
        return self

lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]

lst = lst + 76 # сложение каждого числа списка с определенным числом
print(lst.__dict__)
lst = 6.5 + lst # сложение каждого числа списка с определенным числом
print(lst.__dict__)
lst += 76.7  # сложение каждого числа списка с определенным числом
print(lst.__dict__)
lst = lst - 76 # вычитание из каждого числа списка определенного числа
lst = 7.0 - lst # вычитание из числа каждого числа списка
lst -= 76.3
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0
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

