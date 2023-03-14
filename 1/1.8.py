# class Server:
#     ip = 0
#
#     @classmethod
#     def get_ip_server(cls):
#         cls.ip += 1
#         return cls.ip
#
#     def __init__(self):
#         self.ip = self.get_ip_server()
#         self.buffer = []
#         self.router = None
#
#     def send_data(self, data):
#         if self.router:
#             self.router.buffer.append(data)
#
#     def get_data(self):
#         b = self.buffer[:]
#         self.buffer.clear()
#         return b
#
#     def get_ip(self):
#         return self.ip
#
#
# class Router:
#
#     def __init__(self):
#         self.servers = {}
#         self.buffer = []
#
#     def link(self, server):
#         self.servers[server.ip] = server
#         server.router = self
#
#     def unlink(self, server):
#         s = self.servers.pop(server.ip, False)
#         if s:
#             s.router = None
#
#     def send_data(self):
#         for data in self.buffer:
#             if data.ip in self.servers:
#                 self.servers[data.ip].buffer.append(data)
#         self.buffer.clear()
#
#
# class Data:
#     def __init__(self, data, ip):
#         self.data = data
#         self.ip = ip
#
#
# serv1 = Server()
# serv2 = Server()
# print(serv1.ip)
# print(serv2.ip)
# router = Router()
# router.link(serv2)
# router = Router()
# sv_from = Server()
# sv_from2 = Server()
# router.link(sv_from)
# router.link(sv_from2)
# router.link(Server())
# router.link(Server())
# sv_to = Server()
# router.link(sv_to)
# sv_from.send_data(Data("Hello", sv_to.get_ip()))
# sv_from2.send_data(Data("Hello", sv_to.get_ip()))
# sv_to.send_data(Data("Hi", sv_from.get_ip()))
# router.send_data()
# msg_lst_from = sv_from.get_data()
# msg_lst_to = sv_to.get_data()