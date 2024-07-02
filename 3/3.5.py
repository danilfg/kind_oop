# 8
class Box:
    def __init__(self):
        self.objs = []
    
    def add_thing(self, obj):
        self.objs.append(obj)
        
    def get_things(self):
        return self.objs
    
    @staticmethod
    def get_list_info(objs):
        res = []
        for obj in objs:
            res.append(obj.get_info())
        return res
    
    def __eq__(self, other):
        box1 = sorted(self.get_list_info(self.objs))
        box2 = sorted(self.get_list_info(other.objs))
        return box1 == box2
    
class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
        
    def __eq__(self, other):
        return all([self.name.lower() == other.name.lower(), self.mass == other.mass])

    def get_info(self):
        return [self.name, self.mass]

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))
t1 = Thing('тряпка', 200)
t2 = Thing('Мел', 100)
t3 = Thing('мел', 100)
print(t1 == t2)
print(t2 == t3)

res = b1 == b2 # True
print(res)
"""
Подвиг 10. Объявите в программе класс с именем Box (ящик), объекты которого должны создаваться командой:

box = Box()
А сам класс иметь следующие методы:

add_thing(self, obj) - добавление предмета obj (объект другого класса Thing) в ящик;
get_things(self) - получение списка объектов ящика.

Для описания предметов необходимо объявить еще один класс Thing. Объекты этого класса должны создаваться командой:

obj = Thing(name, mass)
где name - название предмета (строка); mass - масса предмета (число: целое или вещественное).
Объекты класса Thing должны поддерживать операторы сравнения:

obj1 == obj2
obj1 != obj2
Предметы считаются равными, если у них одинаковые названия name (без учета регистра) и массы mass.

Также объекты класса Box должны поддерживать аналогичные операторы сравнения:

box1 == box2
box1 != box2
Ящики считаются равными, если одинаковы их содержимое (для каждого объекта класса Thing одного ящика и можно найти ровно один равный объект из второго ящика).

Пример использования классов:

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
P.S. В программе только объявить классы, выводить на экран ничего не нужно.
"""
# # 7
# class Body:
#     def __init__(self, name, ro, volume):
#         self.name = name
#         self.ro = ro
#         self.volume = volume
        
#     def get_m(self):
#         return self.ro * self.volume
    
#     def __eq__(self, other):
#         other = other.get_m() if isinstance(other, Body) else other
#         return self.get_m() == other
    
#     def __lt__(self, other):
#         other = other.get_m() if isinstance(other, Body) else other
#         return self.get_m() < other
# # 6        
# class MoneyR:
#     def __init__(self, volume = 0):
#         self.__cb = None
#         self.__volume = volume
        
#     @property
#     def cb(self):
#         return self.__cb
    
#     @cb.setter
#     def cb(self, value):
#         self.__cb = value
        
#     @property
#     def volume(self):
#         return self.__volume
    

#     def __eq__(self, other):
#         if not self.cb or not other.cb:
#             raise ValueError("Неизвестен курс валют.")
#         wallet1 = self.__cb.curs_transfer(self)
#         wallet2 = self.__cb.curs_transfer(other)
#         return wallet1 <= wallet2 + wallet2 * 0.1
    
#     def __lt__(self, other):
#         if not self.cb or not other.cb:
#             raise ValueError("Неизвестен курс валют.")
#         wallet1 = self.__cb.curs_transfer(self)
#         wallet2 = self.__cb.curs_transfer(other)
#         return wallet1 < wallet2
    
#     def __le__(self, other):
#         return self.__volume <= other.__volume


# class MoneyD:
#     def __init__(self, volume = 0):
#         self.__cb = None
#         self.__volume = volume
        
#     @property
#     def cb(self):
#         return self.__cb
    
#     @cb.setter
#     def cb(self, value):
#         self.__cb = value
        
#     @property
#     def volume(self):
#         return self.__volume
    

#     def __eq__(self, other):
#         if not self.cb or not other.cb:
#             raise ValueError("Неизвестен курс валют.")
#         wallet1 = self.__cb.curs_transfer(self)
#         wallet2 = self.__cb.curs_transfer(other)
#         return wallet1 <= wallet2 + wallet2 * 0.1
    
#     def __lt__(self, other):
#         if not self.cb or not other.cb:
#             raise ValueError("Неизвестен курс валют.")
#         wallet1 = self.__cb.curs_transfer(self)
#         wallet2 = self.__cb.curs_transfer(other)
#         return wallet1 < wallet2
    
#     def __le__(self, other):
#         return self.__volume <= other.__volume


# class MoneyE:
#     def __init__(self, volume = 0):
#         self.__cb = None
#         self.__volume = volume
        
#     @property
#     def cb(self):
#         return self.__cb
    
#     @cb.setter
#     def cb(self, value):
#         self.__cb = value
        
#     @property
#     def volume(self):
#         return self.__volume

#     def __eq__(self, other):
#         if not self.cb or not other.cb:
#             raise ValueError("Неизвестен курс валют.")
#         wallet1 = self.__cb.curs_transfer(self)
#         wallet2 = self.__cb.curs_transfer(other)
#         return wallet1 <= wallet2 + wallet2 * 0.1
    
#     def __lt__(self, other):
#         if not self.cb or not other.cb:
#             raise ValueError("Неизвестен курс валют.")
#         wallet1 = self.__cb.curs_transfer(self)
#         wallet2 = self.__cb.curs_transfer(other)
#         return wallet1 < wallet2
    
#     def __le__(self, other):
#         return self.__volume <= other.__volume
    
    
# class CentralBank:
#     def __new__(cls, *args, **kwargs):
#         return None
    
#     def __init__(self):
#         self.__rates = None
        
#     @property
#     def rates(self):
#         return self.__rates
    
#     @rates.setter
#     def rates(self, value):
#         self.__rates = value
    
#     @classmethod
#     def register(cls, wallet):
#         wallet.cb = cls
        
#     @staticmethod
#     def curs_transfer(wallet):
#         if not wallet.cb or not CentralBank.rates:
#             raise ValueError("Неизвестен курс валют.")
#         if isinstance(wallet, MoneyR):
#             return wallet.volume
#         if isinstance(wallet, MoneyD):
#             return wallet.volume * wallet.cb.rates['rub']
#         if isinstance(wallet, MoneyE):
#             return wallet.volume * wallet.cb.rates['rub'] * wallet.cb.rates['euro']
        
        
# CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
# # print(CentralBank.rates)

# r = MoneyR(45000)
# d = MoneyD(500)

# CentralBank.register(r)
# CentralBank.register(d)
# # print('r', r.cb.rates['rub'])
# # print('d', d.cb.rates['rub'])

# if r > d:
#     print("неплохо")
# else:
#     print("нужно поднажать")
    

# # 5
# class FileAcceptor:
#     def __init__(self, *argv):
#         self.exts = argv 

#     def __call__(self, ext):
#         return True if ext.split('.')[-1] in self.exts else False
    
#     def __add__(self, other):
#         return FileAcceptor(*(self.exts + other.exts))


# filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]

# # acceptor1 = FileAcceptor("jpg", "jpeg", "png")
# # print(acceptor1('jpg'))
# # print('acceptor1', acceptor1.exts)


# # acceptor2 = FileAcceptor("png", "bmp")
# # print('acceptor2', acceptor2.exts)

# # acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
# # print('acceptor12', acceptor12.exts)
# acceptor_images = FileAcceptor("jpg", "jpeg", "png")
# # print('acceptor_images', acceptor_images.exts)

# acceptor_docs = FileAcceptor("txt", "doc", "xls")
# # print('acceptor_docs', acceptor_docs.exts)

# # filenames = list(filter(acceptor_images + acceptor_docs, filenames))
# # filenames1 = list(filter(acceptor_images, filenames))
# filenames1 = []
# for filename in filenames:
#     filenames1.append(acceptor_images(filename))

# print(filenames1)

# # 4
# import re

# class Morph:
#     def __init__(self, *argv):
#         self.words = argv
        
#     def add_word(self, word):
#         if word not in self.words:
#             self.words += (word,)
    
#     def get_words(self):
#         return self.words
        
#     def __eq__(self, other):
#         other = other.lower()
#         return True if other in self.words else False

# # --------------------------------------------------------------------
# # s = """- связь, связи, связью, связи, связей, связям, связями, связях
# # - формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
# # - вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
# # - эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
# # - день, дня, дню, днем, дне, дни, дням, днями, днях
# # """

# # dict_words = [Morph(*line.lstrip('- ').split(', ')) for line in s.splitlines()]
# # --------------------------------------------------------------------

# dict_words = []
# a = ['связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях']
# b = ['формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах']
# c = ['вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах']
# d = ['эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах']
# e = ['день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях']
# dict_words.append(Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'))
# dict_words.append(Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'))
# dict_words.append(Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'))
# dict_words.append(Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'))
# dict_words.append(Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'))



# # text = input()
# text = 'Мы будем устанавливать связь завтра днем.'

# text = re.sub("[^A-Za-zА-Яа-я ]", "", text.lower())
# text = text.split()

# res = 0
# for morph in dict_words:
#     for word in morph.get_words():
#         if word in text:
#             res += 1
# print(res)

# qw = Morph('связи', 'связью', 'связей', 'связям', 'связями', 'связях')
# print(qw.get_words())

# print(qw == 'связь')
# print('связь' == qw)

# qw.add_word('связь')
# print(qw.get_words())
# print(qw != 'связь')
# print('связь' == qw)
# # 3
# class StringText:
#     def __init__(self, lst_words):
#         self.__lst_words = lst_words
    
#     @property
#     def lst_words(self):
#         return self.__lst_words
    
#     def __str__(self):
#         return self.lst_words
    
#     def __le__(self, other):
#         return len(self.lst_words) <= len(other.lst_words)
    
#     def __lt__(self, other):
#         return len(self.lst_words) < len(other.lst_words)
    
#     def __len__(self):
#         return len(self.__lst_words)
    
# stich = ["Я к вам пишу – чего же боле?",
#         "Что я могу еще сказать?",
#         "Теперь, я знаю, в вашей воле",
#         "Меня презреньем наказать.",
#         "Но вы, к моей несчастной доле",
#         "Хоть каплю жалости храня,",
#         "Вы не оставите меня."]

# symb = "–?!,.;"

# stich_temp = stich

# for y in list(symb):
#     stich_temp = list(map(lambda x: x.replace(y, ""), stich_temp))
# stich_temp = [x.split() for x in stich_temp]
# lst_text = []
# for lst_words in stich_temp:
#     lst_text.append(StringText(lst_words))
    
# lst_text_sorted = sorted(lst_text, key=lambda x: len(x), reverse=True)
# lst_text_sorted = list(' '.join(x.lst_words) for x in lst_text_sorted)
# # lst_text_sorted.reverse()
# print(lst_text_sorted)
# # 2
# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 10000
    
#     def __init__(self, a, b, c):
#         self.__a = a
#         self.__b = b
#         self.__c = c
    
#     def __setattr__(self, key, value):
#             if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
#                 object.__setattr__(self, key, value)
    
#     @property
#     def a(self):
#         return self.__a
    
#     @a.setter
#     def a(self, value):
#         self.__a = value

#     @property
#     def b(self):
#         return self.__b
    
#     @b.setter
#     def b(self, value):
#         self.__b = value 
        
#     @property
#     def c(self):
#         return self.__c
    
#     @c.setter
#     def c(self, value):
#         self.__c = value
    
#     @classmethod
#     def cube(csl, obj):
#         return obj.a * obj.b * obj.c
    

#     def __le__(self, other):
#         return self.cube(self) <= self.cube(other)
    
#     def __lt__(self, other):
#         return self.cube(self) < self.cube(other)
    
    
# class ShopItem:
#     def __init__(self, name, price, dim):
#         self.name = name
#         self.price = price
#         self.dim = dim
        
    

# a = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
# b = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
# c = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
# d = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
# lst_shop = [a, b, c, d]
# lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.cube(x.dim))

# # 1
# class Track:
#     def __init__(self, start_x, start_y):
#         self.start_x = start_x
#         self.start_y = start_y
#         self.path_way = tuple()
#         self.dist = []

#     def add_track(self, tr):
#         if not self.path_way:
#             self.path_way += (tr,)
#             res = ((tr.to_x - self.start_x) ** 2 + (tr.to_y - self.start_y) ** 2) ** 0.5
#             self.dist.append(res)
#         else:
#             res = ((tr.to_x - self.path_way[-1].to_x) ** 2 + (tr.to_y - self.path_way[-1].to_y) ** 2) ** 0.5
#             self.path_way += (tr,)
#             self.dist.append(res)
        
#     def get_tracks(self):
#         return self.path_way
    
#     def __len__(self):
#         return int(sum(self.dist))
    
#     def __eq__(self, other):
#         return len(self) == len(other)
    
#     def __lt__(self, other):
#         return len(self) < len(other)

# class TrackLine:
#     def __init__(self, to_x, to_y, max_speed):
#         self.to_x = to_x
#         self.to_y = to_y
#         self.max_speed = max_speed


# track1 = Track(0, 0)
# track2 = Track(0, 1)

# # 1-й маршрут: (0; 0), (2; 4), (5; -4) и max_speed = 100
# # 2-й маршрут: (0; 1), (3; 2), (10; 8) и max_speed = 90

# max_speed1 = 100
# max_speed2 = 80

# track1.add_track(TrackLine(2, 4, max_speed1))
# track1.add_track(TrackLine(5, -4, max_speed1))
# track2.add_track(TrackLine(3, 2, max_speed2))
# track2.add_track(TrackLine(10, 8, max_speed2))

# res_eq = track1 == track2

# print(len(track1), len(track2))
# # 0
# class Clock:
#     __DAY = 86400 # seconds in day
    
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError("Seconds must be INTEGER")
#         self.seconds = seconds % self.__DAY
    
#     @classmethod
#     def __verify_data(cls, other):
#         if not isinstance(other, (int, Clock)):
#             raise TypeError("operand have problem")
        
#         return other if isinstance(other, int) else other.seconds

#     def __eq__(self, other):
#         sc = self.__verify_data(other)
#         return self.seconds == other
    
#     def __lt__(self, other):
#         sc = self.__verify_data(other)
#         return self.seconds < other
    
#     def __gt__(self, other):
#         sc = self.__verify_data(other)
#         return self.seconds > other
    
#     def __le__(self, other):
#         sc = self.__verify_data(other)
#         return self.seconds > other
    
#     def __ge__(self, other):
#         
#         sc = self.__verify_data(other)
#         return self.seconds > other
        
# c1 = Clock(1000)
# c2 = Clock(1000)
# print(c1 == c2) # def __eq__(self, other)
# print(c1 < c2) # def __lt__(self, other)
# print(c1 > c2) # def __gt__(self, other)
# print(c1 <= c2) # def __le__(self, other)
# print(c1 >= c2) # def __ge__(self, other)