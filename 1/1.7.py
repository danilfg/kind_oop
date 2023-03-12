# 6
class Viber:
    messages = []

    @classmethod
    def add_message(cls, msg):
        cls.messages.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.messages.remove(msg)

    @staticmethod
    def set_like(message):
        if message.fl_like:
            message.fl_like = False
        else:
            message.fl_like = True

    @classmethod
    def show_last_message(cls, count):
        for message in cls.messages[-count:]:
            print(message.text)

    @classmethod
    def total_messages(cls):
        return len(cls.messages)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
print(Viber.total_messages())
Viber.show_last_message(1)
Viber.remove_message(msg)
# 5
# class AppStore:
#     def __init__(self):
#         self.apps = []
#
#     def add_application(self, app):
#         self.apps.append(app)
#
#     def remove_application(self, app):
#         self.apps.remove(app)
#
#     def block_application(self, app):
#         try:
#             self.apps[self.apps.index(app)].blocked = True
#         except ValueError:
#             print("App not found")
#
#     def total_apps(self):
#         return len(self.apps)
#
#
# class Application:
#     def __init__(self, name, blocked=False):
#         self.name = name
#         self.blocked = blocked
#
#
# store = AppStore()
# app_youtube = Application("Youtube")
# app_youtube1 = Application("11Youtube")
# store.add_application(app_youtube)
# print(store.total_apps())
# print(app_youtube.blocked)
# store.block_application(app_youtube)
# print(app_youtube.blocked)
# store.remove_application(app_youtube)
# print(store.total_apps())

# 4
# class Video:
#     def __init__(self):
#         self.name = None
#
#     def create(self, name):
#         self.name = name
#
#     def play(self):
#         print(f"воспроизведение видео {self.name}")
#
#
# class Youtube:
#     videos = []
#
#     @classmethod
#     def add_video(cls, video):
#         cls.videos.append(video)
#
#     @classmethod
#     def play(cls, video_indx):
#         cls.videos[video_indx].play()
#
#
# v1 = Video()
# v1.create("Python")
# v2 = Video()
# v2. create("Python ООП")
#
# Youtube.add_video(v1)
# Youtube.add_video(v2)
# Youtube.play(0)
# Youtube.play(1)

# 3
# from string import ascii_lowercase, digits
# CHARS_FOR_NAME = ascii_lowercase.upper() + digits
#
# class CardCheck:
#     CHARS_FOR_NAME = ascii_lowercase.upper() + digits
#
#     @staticmethod
#     def check_card_number(number):
#         try:
#             check_nums = number.split('-')
#             res = True if len(check_nums) == 4 and all([len(x) == 4 and x.isdigit() for x in check_nums]) else False
#         except ValueError:
#             res = False
#         return res
#
#     @classmethod
#     def check_name(cls, name):
#         try:
#             split_name = name.split()
#             res = all([char in cls.CHARS_FOR_NAME for s in split_name for char in s] + [len(split_name) == 2])
#         except ValueError:
#             res = False
#         return res
#
#
# nums1 = "1234-5678-9012-0000"
# print(CardCheck.check_card_number(nums1))
# is_name = CardCheck.check_name("SERGEI BALAKIREV")
# print(is_name)
# 2
# from string import ascii_lowercase, digits
#
#
# class PasswordInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#     MIN_LENGHT = 3
#     MAX_LENGHT = 50
#
#     def __init__(self, name, size=10):
#         self.check_name(name)
#         self.name = name
#         self.size = size
#
#     @classmethod
#     def check_name(cls, name):
#         if not cls.MIN_LENGHT <= len(name) <= cls.MAX_LENGHT:
#             raise ValueError("некорректное поле name")
#
#         if any([char not in cls.CHARS_CORRECT for char in name]):
#             raise ValueError("некорректное поле name")
#         # for char in name:
#         #     if char not in cls.CHARS_CORRECT:
#         #         raise ValueError("некорректное поле name")
#
#     def get_html(self):
#         return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
#
#
# class TextInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#     MIN_LENGHT = 3
#     MAX_LENGHT = 50
#
#     def __init__(self, name, size=10):
#         self.check_name(name)
#         self.name = name
#         self.size = size
#
#     @classmethod
#     def check_name(cls, name):
#         if not cls.MIN_LENGHT <= len(name) <= cls.MAX_LENGHT:
#             raise ValueError("некорректное поле name")
#
#         if any([char not in cls.CHARS_CORRECT for char in name]):
#             raise ValueError("некорректное поле name")
#         # for char in name:
#         #     if char not in cls.CHARS_CORRECT:
#         #         raise ValueError("некорректное поле name")
#
#     def get_html(self):
#         return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
#
#
# class FormLogin:
#     def __init__(self, lgn, psw):
#         TextInput.check_name(lgn.name)
#         PasswordInput.check_name(psw.name)
#         self.login = lgn
#         self.password = psw
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
#
#
# login = FormLogin(TextInput("Логин", 3), PasswordInput("Пароль", 4))
# html = login.render_template()
# print(html)
# TextInput.check_name("aa")
# 1
# class Factory:
#     @staticmethod
#     def build_sequence():
#         return []
#
#     @staticmethod
#     def build_number(string):
#         return int(string)
#
#
# class Loader:
#     @staticmethod
#     def parse_format(string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
#
# res = Loader.parse_format("4, 5, -6", Factory)
# print(res)
