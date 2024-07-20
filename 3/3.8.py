# 2


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