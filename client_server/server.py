"""
В файле содержится информация о беспилотных летательных аппаратах:
Наименование	|   Крейсерская скорость (км/ч)  |	Продолжительность полета (мин)
Разработать
программу, позволяющую получить характеристики по наименованию;
список БПЛА, способных достичь цели, находящейся на заданном расстоянии, не более чем за 10 минут.
Предусмотреть корректный ответ сервера при отсутствии требуемой информации.
"""
from aircraft_analyze import solver
import socket

# max time for flight in minutes
max_flight_time = 10
data_path = "/Users/rokatyy/PycharmProjects/methods/client_server/aircraft_info.csv"

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 53210))
serv_sock.listen(10)

while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые
        # им данные и отправляем их обратно
        data = client_sock.recv(1024)
        result = solver(data, data_path)
        if not data:
            # Клиент отключился
            break
        client_sock.sendall(result)

    client_sock.close()