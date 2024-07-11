# 2
import sys


class MailBox:
    def __init__(self):
        self.inbox_list = []
    
    def receive(self):
        # sys.stdin = open('3.7.2.py.txt', 'r', encoding='utf-8')
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        self.inbox_list += list(map(lambda x: MailItem(*x.split('; ')), lst_in))
        


        
class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False
        
    def set_read(self, fl_read):
        self.is_read = fl_read
        
    def __bool__(self):
        return self.is_read
    
    def __repr__(self):
        return f"{self.mail_from}: {self.is_read}"
        
mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)
inbox_list_filtered = list(filter(bool, mail.inbox_list))
print(*inbox_list_filtered, sep='\n')
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
    