# 5 
class Cell:
    def __init__(self, data=0):
        self.__data = data
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        self.__data = value
    
    # def __repr__(self):
    #     return f'{self.__data}'
        
class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.table = tuple(tuple(Cell(type_data(0)) for _ in range(cols)) for _ in range(rows))
        
    def __getitem__(self, item):
        if (item[0] >= self.rows) or (item[1] >= self.cols):
            raise IndexError('неверный индекс')
        return self.table[item[0]][item[1]].data
    
    def __setitem__(self, key, value):
        if (key[0] >= self.rows) or (key[1] >= self.cols):
            raise IndexError('неверный индекс')
        if not isinstance(value, self.type_data):
            raise TypeError('неверный тип присваиваемых данных')
        self.table[key[0]][key[1]].data = value
        
    def __iter__(self):
        for row in self.table:
            yield iter(x.data for x in row)
        
table = TableValues(34, 12, int)

table[10, 10] = 10# запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[10, 10] # считывание значения из ячейки с индексами row, col
# print('value', value)
# print(table[10, 10])
# print(table[10, 11])
# print(table.table[10][11].data)

# for row in table:  # перебор по строкам
#     for value in row: # перебор по столбцам
#         print(value, end=' ')  # вывод значений ячеек в консоль
#     print()
# # 4
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
        
        
        
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.objs = []
        
#     def __len__(self):
#         return len(self.objs)
    
#     def push_back(self, obj):
#         if len(self) == 0:
#             self.top = obj
#         else:
#             self.objs[-1].next = obj
#         self.objs.append(obj)
            
#     def push_front(self, obj):
#         if len(self) > 0:
#             obj.next = self.objs[0]
#         self.objs = [obj] + self.objs
#         self.top = obj
        
#     def __getitem__(self, item):
#         if not isinstance(item,int) or not (0 <= item <= len(self.objs) - 1):
#             raise IndexError('неверный индекс')
#         return self.objs[item].data
    
#     def __setitem__(self, key, value):
#         if not isinstance(key,int) or not (0 <= key <= len(self.objs) - 1):
#             raise IndexError('неверный индекс')
#         self.objs[key].data = value
        
#     def __iter__(self):
#         for obj in self.objs:
#             yield obj

#     # def __str__(self):
#     #     return "\n".join([x.data for x in self.objs])
    
   
# st = Stack()
# st.push_back(StackObj("1"))
# st.push_front(StackObj("2"))
# # print(st)
# assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"
# for obj in st:
#     print(obj)
#     assert isinstance(obj, StackObj), "1111111111при переборе стека через цикл должны возвращаться объекты класса StackObj"
# st[0] = "0"
# assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

# for obj in st:
#     print(obj)
#     assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

# try:
#     a = st[3]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError" 
# # 3
# class IterColumn:
#     def __init__(self, lst, column):
#         self.lst = lst
#         self.column = column
        
#     def __iter__(self):
#         for row in self.lst:
#             yield row[self.column]
            

# lst = [['x11', 'x12', 'x1N'],
#        ['x21', 'x22', 'x2N'],
#        ['xM1', 'xM2', 'xMN']
#       ]

# it = IterColumn(lst, 0)

# for x in it:
#     print(x)
    
# it_iter = iter(it)
# x = next(it_iter)
# print(x)
# # 2
# class TriangleListIterator:
#     def __init__(self, lst):
#         self.lst = lst
        
#     def __iter__(self):
#         for i in range(len(self.lst)):
#             for j in self.lst[i]:
#                 yield j
#         # self.res = []
#         # for i in range(len(self.lst)):
#         #     for j in self.lst[i]:
#         #         self.res.append(j)
#         # return iter(self.res)


# lst = [['x00'], ['x10', 'x11'], ['x20', 'x21', 'x22'], ['x30', 'x31', 'x32', 'x33']]

# it = TriangleListIterator(lst)
# for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
#     print(x)
# it_iter = iter(it)
# x = next(it_iter)
# print(x)

# # 1
# class Person:
#     def __init__(self, fio, job, old, salary, year_job):
#         self.fio = fio
#         self.job = job
#         self.old = old
#         self.salary = salary
#         self.year_job = year_job
        
        
#     def __getitem__(self, item):
#         if item == 0:
#             return self.fio
#         elif item == 1:
#             return self.job
#         elif item == 2:
#             return self.old
#         elif item == 3:
#             return self.salary
#         elif item == 4:
#             return self.year_job
#         else:
#             raise IndexError('неверный индекс')

#     def __setitem__(self, key, value):
#         if key == 0:
#             self.fio = value
#         elif key == 1:
#             self.job = value
#         elif key == 2:
#             self.old = value
#         elif key == 3:
#             self.salary = value
#         elif key == 4:
#             self.year_job = value
#         else: 
#             raise IndexError('неверный индекс')

#     def __iter__(self):
#         self.start = 0
#         self.stop = 4
#         self.values = [self.fio, self.job, self.old, self.salary, self.year_job]
#         return self

#     def __next__(self):
#         if self.start <= self.stop:
#             self.start += 1
#             return self.values[self.start - 1]
#         else:
#             raise StopIteration
        
        
# pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# pers[0] = 'Балакирев С.М.'
# for v in pers:
#     print(v)
# pers[5] = 123 # IndexError
# # 0
# class FRange:
#     def __init__(self, start=0.0, stop=0.0, step=1.0):
#         self.start = start
#         self.stop = stop
#         self.step = step
#         self.value = self.start - self.step
        
#     def __iter__(self):
#         self.value = self.start - self.step
#         return self
        
#     def __next__(self): # next(fr)
#         if self.value + self.step < self.stop:
#             self.value += self.step
#             return self.value
#         else:
#             raise StopIteration
        

# class FRange2D:
#     def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
#         self.rows = rows
#         self.fr = FRange(start, stop, step)
        
#     def __iter__(self):
#         self.value = 0
#         return self
    
#     def __next__(self):
#         if self.value < self.rows:
#             self.value += 1
#             return iter(self.fr)
#         else:
#             raise StopIteration


# fr = FRange2D(0, 2, 0.5, 4)
# for row in fr:
#     for x in row:
#         print(x, end=" ")
#     print()

# # fr = FRange(0, 2, 0.5)
# # print(fr.__next__())
# # print(fr.__next__())
# # print(fr.__next__())
# # print(fr.__next__())
# # for x in fr: # работает потому что создали __iter__(self)
# #     print(x)

# # print(next(fr))
# # print(next(fr))
# # print(next(fr))
# # print(next(fr))