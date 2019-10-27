"""
В файле содержится информация о беспилотных летательных аппаратах:
Наименование	|   Крейсерская скорость (км/ч)  |	Продолжительность полета (мин)

Разработать
программу, позволяющую получить характеристики по наименованию;
список БПЛА, способных достичь цели, находящейся на заданном расстоянии, не более чем за 10 минут.
Предусмотреть корректный ответ сервера при отсутствии требуемой информации.
"""
import socket
from pandas import read_csv

aircraft_info_file_path = "/Users/rokatyy/PycharmProjects/methods/client_server/aircraft_info.csv"
max_flight_time = 600
keyword = 'secret'


class server:
    def __init__(self, host='127.0.0.1', port=1337):
        self.srv_sock = socket.socket()
        self.srv_sock.bind((host, port))
        self.srv_sock.listen(1)
        self.conn, self.addr = self.srv_sock.accept()

    def wait_ask(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            elif data == keyword:
                secret_info = aircraft_info().data
                self.conn.send(data)


class aircraft_info:
    def __init__(self, file_path):
        self.data = []
        self.file_path = file_path

    def read_secret_file(self):
        self.data = read_csv(self.file_path)


a = aircraft_info(aircraft_info_file_path)
a.read_secret_file()

server().wait_ask()
