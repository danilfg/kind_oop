# 8
class InputDigits:
    def __init__(self, func):
        self.__fn = func

    def __call__(self):
        res = self.__fn()
        return list(map(int, res.split()))


@InputDigits
def input_dg():
    return input()

t = input_dg()
print(t)

# # 7
# class Handler:
#     def __init__(self, methods):
#         self.__methods = methods

#     def __call__(self, func):
#         def wrapper(request, *args, **kwargs):
#             if request.setdefault('method', 'GET') and request["method"] in self.__methods:
#                 return self.__getattribute__(request['method'].lower())(func, request)
#             return
#         return wrapper

#     def get(self, func, request, *args, **kwargs):
#         return f"GET: {func(request)}"
        
#     def post(self, func, request, *args, **kwargs):
#         return f"POST: {func(request)}"
    
#     # def __getattribute__(self, item):
#     #     print(item)
#     #     if item == "_Handler__request":
#     #         print('__getattribute__')

#     #     return object.__getattribute__(self, item)

# @Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
# def contact(request):
#     return "Сергей Балакирев"

# res = contact({})
# print(res) # "POST: Сергей Балакирев"
# assert hasattr(Handler, 'get') and hasattr(Handler, 'post'), "класс Handler должен содержать методы get и post"

# @Handler(methods=('GET', 'POST'))
# def contact2(request):
#     return "контакты"

# assert contact2({"method": "POST"}) == "POST: контакты", "декорированная функция вернула неверные данные"
# assert contact2({"method": "GET"}) == "GET: контакты", "декорированная функция вернула неверные данные"
# assert contact2({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"
# assert contact2({}) == "GET: контакты", "декорированная функция вернула неверные данные при указании пустого словаря"

# @Handler(methods=('POST'))
# def index(request):
#     return "index"

# assert index({"method": "POST"}) == "POST: index", "декорированная функция вернула неверные данные"
# assert index({"method": "GET"}) is None, "декорированная функция вернула неверные данные"
# assert index({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"
# # 6
# class HandlerGET:
#     METHOD = "GET"

#     def __init__(self, func):
#         self.__fn = func

#     def __call__(self, request, *args, **kwargs):
#         return self.get(self.__fn, request)
        
#     def get(self, func, request, *args, **kwargs):
#         if request.setdefault('method', 'GET') and self.METHOD in request.values():
#             return f"GET: {func(request)}"
#         return None

# @HandlerGET
# def index(request):
#     return "главная страница сайта"

# res = index({"method": "GET"})
# assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
# res = index({"method": "POST"})
# assert res is None, "декорированная функция вернула неверные данные"
# res = index({"method": "POST2"})
# assert res is None, "декорированная функция вернула неверные данные"
# res = index({})
# assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"

# @HandlerGET
# def contact(request):
#     return "Сергей Балакирев"

# res = contact({"method": "POST", "url": "contact.html"})
# print(res)

# # 5
# class RenderList:
#     TYPES_LIST = ["ul", "ol"]
#     TYPES_ROW = ["li"]

#     def __init__(self, type_list):
#         self.__type_list = type_list if type_list in self.TYPES_LIST else self.TYPES_LIST[0]

#     def __call__(self, lst):
#         res = f"<{self.__type_list}>\n<li>"
#         res += f"</li>\n<li>".join(lst)
#         res += f"</li>\n</{self.__type_list}>"
#         return res


# lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
# lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
# render = RenderList("ol")
# html = render(lst) # возвращается многострочная строка с соответствующей HTML-разметкой
# print(html)
# # <ul>
# # <li>Пункт меню 1</li>
# # <li>Пункт меню 2</li>
# # <li>Пункт меню 3</li>
# # </ul>


# # 4
# import re


# class DigitRetrieve:
#     REGEX = "^-?[0-9]+$"
#     def __init__(self):
#         pass

#     def __call__(self, value):
#         pattern = re.compile(self.REGEX)
#         if pattern.search(value) is not None:
#             return int(value)

# dg = DigitRetrieve()
# st = ["123", "abc", "-56.4", "0", "-5", "5-", "--5"]
# digits = list(map(dg, st))  # [123, None, None, 0, -5]
# print(digits)

# # 3

# from string import ascii_lowercase, digits

# class LoginForm:
#     def __init__(self, name, validators=None):
#         self.name = name
#         self.validators = validators
#         self.login = ""
#         self.password = ""

#     def post(self, request):
#         self.login = request.get('login', "")
#         self.password = request.get('password', "")

#     def is_validate(self):
#         if not self.validators:
#             return True

#         for v in self.validators:
#             if not v(self.login) or not v(self.password):
#                 return False

#         return True


# class LengthValidator:
#     """Check len item"""
#     def __init__(self, min_length, max_length):
#         self.__min_length = min_length
#         self.__max_length = max_length

#     def __call__(self, item):
#         if self.__min_length <= len(item) <= self.__max_length:
#             return True
#         return False


# class CharsValidator:
#     """Check chars in item"""
#     def __init__(self, chars):
#         self.__chars = chars

#     def __call__(self, item):
#         for c in item:
#             if c not in self.__chars:
#                 return False
#         return True
#     # return set(string) <= set(self.chars) # Вариант 2
#     # return all([char in self.chars for char in string]) # Вариант 3


# lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
# lg.post({"login": "root", "password": "panda"})
# if lg.is_validate():
#     print("Дальнейшая обработка данных формы")


# # 2
# class ImageFileAcceptor:
#     def __init__(self, extensions):
#         self.__extensions = extensions

#     def __call__(self, filename):
#         extension = filename.split('.')[-1:][0]
#         if extension in self.__extensions:
#             return extension


# filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png", "my.html", "data.shtml"]
# extensions = ('jpg', 'bmp', 'jpeg')
# acceptor = ImageFileAcceptor(extensions)
# image_filenames = filter(acceptor, filenames)
# print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]

# # 1
# from random import choice, randint 


# class RandomPassword:
#     def __init__(self, psw_chars, min_length, max_length):
#         self.__psw_chars = psw_chars
#         self.__min_length = min_length
#         self.__max_length = max_length


#     def __call__(self, *argv, **kwargs):
#         n = randint(self.__min_length, self.__max_length)
#         return ''.join([choice(self.__psw_chars) for _ in range(n)])


# min_length = 5
# max_length = 20
# psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
# rnd = RandomPassword(psw_chars, min_length, max_length)
# lst_pass = [rnd() for _ in range(3)]
# print(lst_pass)


# 0.1
# class Counter:
#     def __init__(self):
#         self.__counter = 0

#     def __call__(self, step=1, *args, **kwds):
#         print("__call__")
#         self.__counter += step
#         return self.__counter
    
# c = Counter()
# c2 = Counter()
# c()
# c(2)
# res = c(10)
# res2 = c2(-5)
# print(res, res2)

# 0.2
# class StripChars:
#     def __init__(self, chars):
#         self.__counter = 0
#         self.__chars = chars

#     def __call__(self, *args, **kwds):
#         if not isinstance(args[0], str):
#             raise TypeError("Аргумент должен быть строкой")
        
#         return args[0].strip(self.__chars)


# s1 = StripChars("?:;!., ")
# s2 = StripChars(" ")
# res = s1(" Hello World! ")
# res2 = s2(" Hello World! ")
# print(res, res2, sep="\n")

# 0.2
# import math

# class Derivate:
#     def __init__(self, func):
#         self.__fn = func

#     def __call__(self, x, dx=0.0001, *args, **kwargs):
#         return (self.__fn(x + dx) - self.__fn(x)) / dx
        

# @Derivate
# def df_sin(x):
#     return math.sin(x)


# # df_sin = Derivate(df_sin)
# print(df_sin(math.pi/3))