# 5
class Stack:
    def __init__(self):
        self.__stack_objs = []
        self.top = None
        
    def push(self, obj):
        if not self.top:
            self.top = obj
        else:
            self.__stack_objs[-1].next = obj
        self.__stack_objs.append(obj)
            
    def pop(self):
        res = self.__stack_objs[-1]
        if self.__stack_objs:
            self.__stack_objs = self.__stack_objs[:-1]
        if not self.__stack_objs:
            self.top = None
        self.__stack_objs[-1].next = None
        return res

    def __len__(self):
        return len(self.__stack_objs)
    
    def __getitem__(self, item):
        if item >= len(self.__stack_objs) or not isinstance(item, int):
            raise IndexError('неверный индекс')
        return self.__stack_objs[item]
    
    def __setitem__(self, key, value):
        if key >= len(self.__stack_objs) or not isinstance(key, int):
            raise IndexError('неверный индекс')
        self.__stack_objs[key] = value
        if key != len(self.__stack_objs) - 1:
            self.__stack_objs[key].next = self.__stack_objs[key + 1]
        if key != 0:
            self.__stack_objs[key - 1].next = self.__stack_objs[key]
            
        
    def __str__(self):
        return f'\n'.join([x.data for x in self.__stack_objs])

class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        self.__data = value
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, value):
        self.__next = value

# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st[1] = StackObj("new obj2")
# print(st[2].data) # obj3
# print(st[1].data) # new obj2
# res = st[3] # исключение IndexError
st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
st[1] = StackObj("obj2-new")
assert st[0].data == "obj11" and st[1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st.pop()
assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"
print('2222222', st)
n = 0
h = st.top
# print(n, h.data)
while h:
    assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
    print(n, h.data)
    n += 1
    
    h = h.next
    # print(n, h.data)
    
# print(n, h)
print('st2', len(st))
print('n', n)
assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"

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