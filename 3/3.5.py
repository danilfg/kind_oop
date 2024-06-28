# 3
class StringText:
    def __init__(self, lst_words):
        self.__lst_words = lst_words
    
    @property
    def lst_words(self):
        return self.__lst_words
    
    def __str__(self):
        return self.lst_words
    
    def __le__(self, other):
        return len(self.lst_words) <= len(other.lst_words)
    
    def __lt__(self, other):
        return len(self.lst_words) < len(other.lst_words)
    
    def __len__(self):
        return len(self.__lst_words)
    
stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

symb = "–?!,.;"

stich_temp = stich

for y in list(symb):
    stich_temp = list(map(lambda x: x.replace(y, ""), stich_temp))
stich_temp = [x.split() for x in stich_temp]
lst_text = []
for lst_words in stich_temp:
    lst_text.append(StringText(lst_words))
    
lst_text_sorted = sorted(lst_text, key=lambda x: len(x), reverse=True)
lst_text_sorted = list(' '.join(x.lst_words) for x in lst_text_sorted)
# lst_text_sorted.reverse()
print(lst_text_sorted)
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
#         sc = self.__verify_data(other)
#         return self.seconds > other
        
# c1 = Clock(1000)
# c2 = Clock(1000)
# print(c1 == c2) # def __eq__(self, other)
# print(c1 < c2) # def __lt__(self, other)
# print(c1 > c2) # def __gt__(self, other)
# print(c1 <= c2) # def __le__(self, other)
# print(c1 >= c2) # def __ge__(self, other)