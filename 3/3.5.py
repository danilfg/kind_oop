# 1
class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.path_way = tuple()
        self.dist = []

    def add_track(self, tr):
        if not self.path_way:
            self.path_way += (tr,)
            res = ((tr.to_x - self.start_x) ** 2 + (tr.to_y - self.start_y) ** 2) ** 0.5
            self.dist.append(res)
        else:
            res = ((tr.to_x - self.path_way[-1].to_x) ** 2 + (tr.to_y - self.path_way[-1].to_y) ** 2) ** 0.5
            self.path_way += (tr,)
            self.dist.append(res)
        
    def get_tracks(self):
        return self.path_way
    
    def __len__(self):
        return int(sum(self.dist))
    
    def __eq__(self, other):
        return len(self) == len(other)
    
    def __lt__(self, other):
        return len(self) < len(other)

class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track1 = Track(0, 0)
track2 = Track(0, 1)

# 1-й маршрут: (0; 0), (2; 4), (5; -4) и max_speed = 100
# 2-й маршрут: (0; 1), (3; 2), (10; 8) и max_speed = 90

max_speed1 = 100
max_speed2 = 80

track1.add_track(TrackLine(2, 4, max_speed1))
track1.add_track(TrackLine(5, -4, max_speed1))
track2.add_track(TrackLine(3, 2, max_speed2))
track2.add_track(TrackLine(10, 8, max_speed2))

res_eq = track1 == track2

print(len(track1), len(track2))
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