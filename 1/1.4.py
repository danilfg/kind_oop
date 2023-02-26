# 3
import sys


class StreamData:

    def create(self, fields, lst_values):
        self.fields = fields
        self.lst_values = lst_values
        if len(self.fields) != len(self.lst_values):
            return False
        self.__dict__ = dict(zip(self.fields, self.lst_values))
        return True


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
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
