# 5
# class Translator:
#     dictionary = dict()
#
#     def add(self, eng, rus):
#         self.dictionary.setdefault(eng, [])
#         if rus not in self.dictionary[eng]:
#             self.dictionary[eng].append(rus)
#
#     def remove(self, eng):
#         self.dictionary.pop(eng, False)
#
#     def translate(self, eng):
#         return self.dictionary[eng]
#
#
# tr = Translator()
# tr= Translator()
# tr.add('tree', 'дерево')
# tr.add('car', 'машина')
# tr.add('car', 'автомобиль')
# tr.add('leaf', 'лист')
# tr.add('river', 'река')
# tr.add('go', 'идти')
# tr.add('go', 'ехать')
# tr.add('go', 'ходить')
# tr.add('milk', 'молоко')
# tr.remove('car')
# print(*tr.translate('go'))
# 4
import sys

sys.stdin = open('1.4.py.txt', 'r', encoding='utf-8')
# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def select(self, a, b):
        return self.lst_data[a:b + 1] if b + 1 < len(self.lst_data) else self.lst_data[a:]

    def insert(self, data):
        self.data = data
        for row in data:
            self.lst_data.append(
                dict(
                    zip(
                        self.FIELDS,
                        tuple(row.split())
                    )
                )
            )


db = DataBase()
db.insert(lst_in)
print(db.lst_data)
print(db.select(1, 1))
print(db.lst_data[1:1])
# 3
# import sys
#
#
# class StreamData:
#
#     def create(self, fields, lst_values):
#         self.fields = fields
#         self.lst_values = lst_values
#         if len(self.fields) != len(self.lst_values):
#             return False
#         self.__dict__ = dict(zip(self.fields, self.lst_values))
#         return True
#
#
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
#
#
# sr = StreamReader()
# data, result = sr.readlines()
# 2
# class Graph:
#     LIMIT_Y = [0, 10]
#
#     def set_data(self, data):
#         self.data = data
#
#     def draw(self):
#         a, b = self.LIMIT_Y
#         print(*filter(lambda x: a <= x <= b, self.data))
#
#
# graph_1 = Graph()
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph_1.draw()
# 1
# class MediaPlayer:
#     def open(self, file):
#         self.filename = file
#
#     def play(self):
#         print(f"Воспроизведение {self.filename}")
#
#
# media1 = MediaPlayer()
# media1.open('filemedia1')
# media1.play()
#
# media2 = MediaPlayer()
# media2.open('filemedia2')
# media2.play()
