"""
В файле содержится информация о беспилотных летательных аппаратах:
Наименование	|   Крейсерская скорость (км/ч)  |	Продолжительность полета (мин)

Разработать
программу, позволяющую получить характеристики по наименованию;
список БПЛА, способных достичь цели, находящейся на заданном расстоянии, не более чем за 10 минут.
Предусмотреть корректный ответ сервера при отсутствии требуемой информации.
"""
import socket

aircraft_info_file_path = ""
max_flight_time = 600


class server:
    def __init__(self, host='', port='1337'):
        self.srv_sock = socket.socket()
        self.srv_sock.bind((host, port))
        self.srv_sock.listen(1)
        self.conn, self.addr = self.srv_sock.accept()

    def wait_ask(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            self.conn.send(data)


class aircraft_info:
    def __init__(self):


class watcher:
    def __init__(self):
