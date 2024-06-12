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