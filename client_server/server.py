"""
В файле содержится информация о беспилотных летательных аппаратах:
Наименование	|   Крейсерская скорость (км/ч)  |	Продолжительность полета (мин)
Разработать
программу, позволяющую получить характеристики по наименованию;
список БПЛА, способных достичь цели, находящейся на заданном расстоянии, не более чем за 10 минут.
Предусмотреть корректный ответ сервера при отсутствии требуемой информации.
"""

from pandas import read_csv
import socket

# max time for flight in minutes
max_flight_time = 10
data_path = "/Users/rokatyy/PycharmProjects/methods/client_server/aircraft_info.csv"


def get_data_from_file(file_path):
    """
    This method returns data from file
    Args:
        file_path (str) - full file path
    Returns:
        data (DataFrame object)
    """
    data = read_csv(file_path)
    return reformat_aircraft_info(data)


def solver(distance, data):
    """
    This method gets distance and returns name of aircraft depends on it, IF there is no suitable aircraft method returns None
    Args:
        distance (int)
        data (DataFrame object) - data about aircrafts (name, speed, time)
    Returns:
        result_name (str) - name of aircraft
    """
    data = reformat_aircraft_info(data)
    result_name = [i for i in data if data[i] >= distance]
    return bool(result_name) and result_name or 'No such aircraft'


def get_max_distance(speed, time):
    return speed * int(time)


def reformat_aircraft_info(data):
    """
    This method changes the type and structure of the given data.
    Returns a dictionary from the name and maximum range of the aircraft.
    Args:
        data (DataFrame object)
    Returns:
        distance_info (dict) where:
                keys -- names
                values -- max flight distance in kilometers
    """
    distance_info = dict.fromkeys(data['Name'].to_list(), 0)
    names = data['Name'].to_list()
    speed = data['speed'].to_list()
    time = data['time'].to_list()
    for i in range(len(speed)):
        speed[i] = int(speed[i]) / 60
        distance_info[names[i]] = get_max_distance(speed[i], time[i])
    return distance_info
