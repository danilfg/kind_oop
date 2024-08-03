# 1
class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        
        
    def __getitem__(self, item):
        if item == 0:
            return self.fio
        elif item == 1:
            return self.job
        elif item == 2:
            return self.old
        elif item == 3:
            return self.salary
        elif item == 4:
            return self.year_job
        else:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        if key == 0:
            self.fio = value
        elif key == 1:
            self.job = value
        elif key == 2:
            self.old = value
        elif key == 3:
            self.salary = value
        elif key == 4:
            self.year_job = value
        else: 
            raise IndexError('неверный индекс')

    def __iter__(self):
        self.start = 0
        self.stop = 4
        self.values = [self.fio, self.job, self.old, self.salary, self.year_job]
        return self

    def __next__(self):
        if self.start <= self.stop:
            self.start += 1
            return self.values[self.start - 1]
        else:
            raise StopIteration
        
        
pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123 # IndexError
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