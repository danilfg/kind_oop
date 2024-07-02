# 2
import sys


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        
    def __eq__(self, other):
        return self.name == other.name and self.weight == other.weight and self.price == other.price
    
    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

        
sys.stdin = open('3.6.2.py.txt', 'r', encoding='utf-8')
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока

shop_items = {}
for lst in lst_in:
    obj = lst.split(':')[:1] + lst.split(':')[1].split()
    tmp_item = ShopItem(obj[0], float(obj[1]), float(obj[2]))
    # if tmp_item not in shop_items
    shop_items[tmp_item] = [tmp_item, 1] if tmp_item not in shop_items else [tmp_item, shop_items[tmp_item][1] + 1]
    
    
    
print(shop_items)
# # 1
# class Rect:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height

#     def __eq__(self, other):
#         return self.width == other.width and self.height == other.height
    
#     def __hash__(self):
#         return hash((self.width, self.height))
        
        
# r1 = Rect(10, 5, 100, 50)
# r2 = Rect(-10, 4, 100, 50)

# h1, h2 = hash(r1), hash(r2)   # h1 == h2

# print(h1 == h2)
# # 0
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
    
#     def __hash__(self):
#         return hash((self.x, self.y))
        
        
# p1 = Point(1, 2)
# p2 = Point(1, 2)

# print(hash(p1), hash(p2), sep="\n")

# d = {}
# d[p1] = 1
# d[p2] = 2
# print(d)