# 5


# # 4
# class Ellipse:
#     def __init__(self, *args):
#         if args:
#             self.x1, self.y1, self.x2, self.y2 = args[0], args[1], args[2], args[3]
            
#     def __bool__(self):
#         return len(self.__dict__) == 4

#     def get_coords(self):
#         try:
#             return (self.x1, self.y1, self.x2, self.y2)
#         except:
#             raise AttributeError('нет координат для извлечения')


# lst_geom = [Ellipse(), Ellipse(), Ellipse(2, 3, 4, 5), Ellipse(2, 3, 4, 5)]

# for item in lst_geom:
#     if bool(item):
#         item.get_coords()

# a1 = Ellipse()
# print(a1.__dict__)

# a1 = Ellipse(2, 3, 4, 5)
# print(len(a1.__dict__))
# # 3
# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.x2 = x2
#         self.y1 = y1
#         self.y2 = y2
        
#     def __len__(self):
#         l = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5
#         return False if l < 1 else True

# line = Line(0, 0, 0.5, 0.5)
# print(bool(line))


# # 2
# import sys


# class MailBox:
#     def __init__(self):
#         self.inbox_list = []
    
#     def receive(self):
#         # sys.stdin = open('3.7.2.py.txt', 'r', encoding='utf-8')
#         lst_in = list(map(str.strip, sys.stdin.readlines()))
#         self.inbox_list += list(map(lambda x: MailItem(*x.split('; ')), lst_in))
        


        
# class MailItem:
#     def __init__(self, mail_from, title, content):
#         self.mail_from = mail_from
#         self.title = title
#         self.content = content
#         self.is_read = False
        
#     def set_read(self, fl_read):
#         self.is_read = fl_read
        
#     def __bool__(self):
#         return self.is_read
    
#     def __repr__(self):
#         return f"{self.mail_from}: {self.is_read}"
        
# mail = MailBox()
# mail.receive()
# mail.inbox_list[0].set_read(True)
# mail.inbox_list[-1].set_read(True)
# inbox_list_filtered = list(filter(bool, mail.inbox_list))
# print(*inbox_list_filtered, sep='\n')
# # 1
# import sys


# class Player:
#     def __init__(self, name, old, score):
#         self.name = name
#         self.old = int(old)
#         self.score = int(score)
        
#     def __bool__(self):
#         return self.score > 0
    
#     def __repr__(self):
#         return f"{self.name}: {self.score}"


# sys.stdin = open('3.7.1.py.txt', 'r', encoding='utf-8')
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# players = list(map(lambda x: Player(*x.split('; ')), lst_in))
# players_filtered = list(filter(bool, players))

# print(players)
# print(players_filtered)
# # 0
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __len__(self):
#         print("__len__")
#         return self.x * self.x + self.y * self.y
    
#     def __bool__(self):
#         print("__bool__")
#         return self.x == self.y


# p1 = Point(3, 4)
# p2 = Point(0, 0)
# print('p1', len(p1), bool(p1))
# print('p2', len(p2), bool(p2))

# # где используется

# if p1:
#     print("объект p1 дает True")
# else:
#     print("объект p1 дает False")
    