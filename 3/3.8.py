# 9
class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.table = {}
    
    def set_rows_cols(self):
        self.rows = max([x[0] for x in self.table.keys()]) + 1
        self.cols = max([x[1] for x in self.table.keys()]) + 1
    
    def add_data(self, row, col, data):
        self.table[(row, col)] = data
        self.set_rows_cols()
        
    def remove_data(self, row, col):
        if (row, col) not in self.table:
            raise IndexError('ячейка с указанными индексами не существует')
        self.table.pop((row, col), None)
        self.set_rows_cols()
    
    def __getitem__(self, item):
        if item not in self.table:
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.table[item]
    
    def __setitem__(self, key, value):
        self.table[key] = value
        row = key[0]
        col = key[1]
        self.set_rows_cols()
    
class Cell:
    def __init__(self, value):
        self.value = value

st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st[4, 7] = 132
assert st.rows == 5 and st.cols == 8, "неверные значения атрибутов rows и cols"

st.remove_data(4, 7)
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols, возможно, некорректно отработал метод remove_data"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"
    
try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"
# st = SparseTable()
# st.add_data(2, 5, Cell("cell_25"))
# st.add_data(0, 0, Cell("cell_00"))
# st[2, 5] = 25 # изменение значения существующей ячейки
# st[11, 7] = 'cell_117' # создание новой ячейки
# print(st[0, 0]) # cell_00
# st.remove_data(2, 5)
# print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
# # val = st[2, 5] # ValueError
# st.remove_data(12, 3) # IndexError
# # 8
# class Bag:
#     def __init__(self, max_weight):
#         self.max_weight = max_weight
#         self.things = []
#         self.total_weight = 0
        
        
#     def add_thing(self, thing):
#         if self.total_weight +  thing.weight > self.max_weight:
#             raise ValueError('превышен суммарный вес предметов')
#         self.things.append(thing)
#         self.total_weight += thing.weight

#     def __getitem__(self, item):
#         if not isinstance(item, int) or item >= len(self.things):
#             raise IndexError('неверный индекс')
#         return self.things[item]

#     def __delitem__(self, key):
#         del self.things[key]

#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key >= len(self.things):
#             raise IndexError('неверный индекс')
#         self.total_weight -= self.things[key].weight
#         if self.total_weight + value.weight > self.max_weight:
#             raise ValueError('превышен суммарный вес предметов')
        
#         self.total_weight += value.weight
#         self.things[key] = value
        
        

# class Thing:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
        
# b = Bag(700)
# b.add_thing(Thing('книга', 100))
# b.add_thing(Thing('носки', 200))

# try:
#     b.add_thing(Thing('рубашка', 500))
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"

# assert b[0].name == 'книга' and b[0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

# t = Thing('Python', 20)
# b[1] = t
# assert b[1].name == 'Python' and b[1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

# del b[0]
# assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

# try:
#     t = b[2]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"

    
# b = Bag(700)
# b.add_thing(Thing('книга', 100))
# b.add_thing(Thing('носки', 200))

# b[0] = Thing('рубашка', 500)

# try:
#     b[0] = Thing('рубашка', 800)
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"      
# bag = Bag(1000)
# bag.add_thing(Thing('книга', 100))
# bag.add_thing(Thing('носки', 200))
# bag.add_thing(Thing('рубашка', 500))
# # bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
# print(bag[2].name) # рубашка
# bag[1] = Thing('платок', 100)
# print(bag[1].name) # платок
# del bag[0]
# print(bag[0].name) # платок
# # t = bag[4] # генерируется исключение IndexError
        
# # 7
# class Cell:
#     def __init__(self):
#         self.is_free = True
#         self.value = 0 # 1 - крестик; 2 - нолик
        
#     def __bool__(self):
#         return self.is_free
    

    
# class TicTacToe:
#     def __init__(self):
#         self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
        
#     def clear(self):
#         self.__init__()
#         # self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
        
#     def __str__(self):
#         return f'\n'.join([f' '.join([str(cell.value) for cell in row]) for row in self.pole])
    
#     def __getitem__(self, item):
#         if isinstance(item[0], slice):
#             return self.pole[0][item[1]].value, self.pole[1][item[1]].value, self.pole[2][item[1]].value, 
#         elif isinstance(item[1], slice):
#             return self.pole[item[0]][0].value, self.pole[item[0]][1].value, self.pole[item[0]][2].value,
#         elif item[0] >= 3 or item[1] >= 3:
#             raise IndexError('неверный индекс клетки')
#         return self.pole[item[0]][item[1]].value
        
#     def __setitem__(self, key, value):
#         if key[0] >= 3 or key[1] >= 3:
#             raise IndexError('неверный индекс клетки')
#         if self.pole[key[0]][key[1]].is_free:
#             self.pole[key[0]][key[1]].value = value
#         else:
#             raise ValueError('клетка уже занята')

        
        
# game = TicTacToe()
# game.clear()
# # game[0, 0] = 1
# game[1, 0] = 2
# print(game)
# # формируется поле:
# # 1 0 0
# # 2 0 0
# # 0 0 0
# # game[3, 2] = 2 # генерируется исключение IndexError
# print('value', game[0, 0])
# if game[0, 0] == 0:
#     game[0, 0] = 2
#     print(game)
# v1 = game[0, :]  # 1, 0, 0
# print(v1)

# v2 = game[:, 0]  # 1, 2, 0
# print(v2)

# # 6
# class RadiusVector:
#     def __init__(self, *args):
#         self.coords = tuple(args)
        
#     def __getitem__(self, item):
#         # print(item)
#         # if item >= len(self.coords):
#         #     raise IndexError('неверный индекс')
#         return self.coords[item]
    
#     def __setitem__(self, key, value):
#         self.coords = list(self.coords)
#         self.coords[key] = value
#         self.coords = tuple(self.coords)
        

            
# v = RadiusVector(1, 1, 1, 1)
# print(v[1]) # 1
# v[:] = 1, 2, 3, 4
# print(v[2]) # 3
# print(v[1:]) # (2, 3, 4)
# v[0] = 10.5
# r1 = RadiusVector(1, 3.4, 6, 23)
# print(r1.coords)


# # 5
# class Stack:
#     def __init__(self):
#         self.__stack_objs = []
#         self.top = None
        
#     def push(self, obj):
#         if not self.top:
#             self.top = obj
#         else:
#             self.__stack_objs[-1].next = obj
#         self.__stack_objs.append(obj)
            
#     def pop(self):
#         res = self.__stack_objs[-1]
#         if self.__stack_objs:
#             self.__stack_objs = self.__stack_objs[:-1]
#         if not self.__stack_objs:
#             self.top = None
#         self.__stack_objs[-1].next = None
#         return res

#     def __len__(self):
#         return len(self.__stack_objs)
    
#     def __getitem__(self, item):
#         ≈
#         return self.__stack_objs[item]
    
#     def __setitem__(self, key, value):
#         if key >= len(self.__stack_objs) or not isinstance(key, int):
#             raise IndexError('неверный индекс')
#         self.__stack_objs[key] = value
#         if key != len(self.__stack_objs) - 1:
#             self.__stack_objs[key].next = self.__stack_objs[key + 1]
#         if key != 0:
#             self.__stack_objs[key - 1].next = self.__stack_objs[key]
            
        
#     def __str__(self):
#         return f'\n'.join([x.data for x in self.__stack_objs])

# class StackObj:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
        
#     @property
#     def data(self):
#         return self.__data
    
#     @data.setter
#     def data(self, value):
#         self.__data = value
#     @property
#     def next(self):
#         return self.__next
    
#     @next.setter
#     def next(self, value):
#         self.__next = value

# # st = Stack()
# # st.push(StackObj("obj1"))
# # st.push(StackObj("obj2"))
# # st.push(StackObj("obj3"))
# # st[1] = StackObj("new obj2")
# # print(st[2].data) # obj3
# # print(st[1].data) # new obj2
# # res = st[3] # исключение IndexError
# st = Stack()
# st.push(StackObj("obj11"))
# st.push(StackObj("obj12"))
# st.push(StackObj("obj13"))
# st[1] = StackObj("obj2-new")
# assert st[0].data == "obj11" and st[1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

# try:
#     obj = st[3]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"

# obj = st.pop()
# assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"
# print('2222222', st)
# n = 0
# h = st.top
# # print(n, h.data)
# while h:
#     assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
#     print(n, h.data)
#     n += 1
    
#     h = h.next
#     # print(n, h.data)
    
# # print(n, h)
# print('st2', len(st))
# print('n', n)
# assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"

# 4
# class IntegerValue: # дескриптор данных для работы с целыми числами.
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
        
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
    
#     def __set__(self, instance, value):
#         # print(f"__set__: {self.name} = {value}")
#         if not isinstance(value, int):
#             raise ValueError('возможны только целочисленные значения')
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
        
        
# class CellInteger: # для операций с целыми числами;
#     value = IntegerValue()
    
#     def __init__(self, start_value = 0):
#         self.value = start_value
    

# class TableValues: # для работы с таблицей в целом
#     def __init__(self, rows, cols, cell = False):
#         if not cell:
#             raise ValueError('параметр cell не указан') 
#         self.cells = tuple()
#         for _ in range(rows):
#             res = tuple(CellInteger() for _ in range(cols))
#             self.cells += res,

#     def __getitem__(self, item):
#         if item[0] >= len(self.cells) or item[1] >= len(self.cells[0]):
#             raise ValueError('ячейки не существует')
#         return self.cells[item[0]][item[1]].value
    
#     def __setitem__(self, key, value):
#         if key[0] >= len(self.cells) or key[1] >= len(self.cells[0]):
#             raise ValueError('ячейки не существует')
#         self.cells[key[0]][key[1]].value = value
    
    
# table = TableValues(2, 3, cell=CellInteger)
# print(table[0, 1])
# table[1, 1] = 10
# # table[0, 0] = 1.45 # генерируется исключение ValueError

# # вывод таблицы в консоль
# for row in table.cells:
#     for x in row:
#         print(x.value, end=' ')
#     print()


# # 3
# class Array:
#     def __init__(self, max_lenght, cell):
#         self.array = [cell(0) for _ in range(max_lenght)]
        
#     def __getitem__(self, item):
#         if item > len(self.array) - 1:
#             raise IndexError('неверный индекс для доступа к элементам массива')
#         return self.array[item].value
    
#     def __setitem__(self, key, value):
#         if key > len(self.array) - 1:
#             raise IndexError('неверный индекс для доступа к элементам массива')
#         self.array[key].value = value
    
#     def __str__(self):
#         res = [str(x.value) for x in self.array]
#         return " ".join(res)
        
        
# class Integer:
#     def __init__(self, start_value):
#         self.__value = start_value
        
#     @property
#     def value(self):
#         return self.__value
    
#     @value.setter
#     def value(self, val):
#         if isinstance(val, int):
#             self.__value = val
#         else:
#             raise ValueError('должно быть целое число')

        
# ar_int = Array(10, cell=Integer)
# print(ar_int[3])
# print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
# ar_int[1] = 10
# # ar_int[1] = 10.5 # должно генерироваться исключение ValueError
# ar_int[10] = 1 # должно генерироваться исключение IndexError
# # 2
# class Track:
#     def __init__(self, start_x, start_y):
#         self.track = []
#         # self.track.append([(start_x, start_y), 0])
        
#     def add_point(self, x, y, speed):
#         self.track.append([(x, y), speed])
        
#     def __getitem__(self, item):
#         if item > len(self.track) - 1 and isinstance(item, int):
#             raise IndexError('некорректный индекс')
#         return self.track[item][0], self.track[item][1]
     
#     def __setitem__(self, key, value):
#         if key > len(self.track) - 1 and isinstance(key, int):
#             raise IndexError('некорректный индекс')
#         self.track[key][1] = value


# tr = Track(10, -5.4)
# tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
# tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
# tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

# tr[2] = 60
# c, s = tr[2]
# print(c, s)

# res = tr[3] # IndexError
# # 1
# class Record:
#     def __init__(self, *args, **kwargs):
#         self.__dict__.update(kwargs)

#     def __getitem__(self, item):
#         if (not isinstance(item, int) or item < 0) or (item > len(self.__dict__) - 1):
#             raise IndexError('неверный индекс поля')
#         for k in self.__dict__:
#             if item == 0:
#                 return self.__dict__[k]
#             item -= 1
            
            
#     def __setitem__(self, key, value):
#         if (not isinstance(key, int) or key < 0) or key > len(self.__dict__):
#             raise IndexError('неверный индекс поля')
#         for k in self.__dict__:
#             if key == 0:
#                 self.__dict__[k] = value
#                 break
#             key -= 1
    
        
# r = Record(pk=1, title='Python ООП', author='Балакирев')
# # print(r.pk) # 1
# # print(r.title) # Python ООП
# # print(r.author) # Балакирев


# print(r.__dict__)
# r[0] = 2 # доступ к полю pk
# r[1] = 'Супер курс по ООП' # доступ к полю title
# r[2] = 'Балакирев С.М.' # доступ к полю author
# print(r[1]) # Супер курс по ООП
# # r[3] # генерируется исключение IndexError
# print(r.__dict__)
# 0

# class Student:
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
        
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Wrong index")
        
#     def __setitem__(self, key,value): # key - ключ 
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Index must be positive integer")
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
            
#         self.marks[key] = value
    
#     def __delitem__(self, key):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Index must be positive integer")
#         del self.marks[key]
        
# s1 = Student("Сергей", [5, 5, 3, 2, 5])

# print(s1.marks[2])
# print(s1[2]) # __getitem__


# print(s1.marks)
# s1[6] = 4 # __setitem__
# print(s1.marks)

# del s1[2] # __delitem__
# print(s1.marks)