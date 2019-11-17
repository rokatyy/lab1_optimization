from pandas import read_csv


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


def solver(distance, file_path):
    """
    This method gets distance and returns name of aircraft depends on it, IF there is no suitable aircraft method returns None
    Args:
        distance (int)
        file_path (str) - fill file path
    Returns:
        result_name (str) - name of aircraft
    """
    try:
        distance = int(distance.decode('utf-8', errors = 'ignore').replace('\\r\\n',''))
        data = get_data_from_file(file_path)
        result_name = [i for i in data if data[i] >= distance]
        return bool(result_name) and 'Aircrafts:\n'+'\n'.join(result_name) or 'No such aircraft'
    except:
        pass


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
    names = data['Name'].to_list()
    distance_info = dict.fromkeys(names, 0)
    speed = data['speed'].to_list()
    time = data['time'].to_list()
    for i in range(len(speed)):
        speed[i] = int(speed[i]) / 60
        distance_info[names[i]] = get_max_distance(speed[i], time[i])
    return distance_info
