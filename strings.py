def if_palindrom(string):
    """
    This method checks if string palindrom.
    Args:
        string (str)
    Returns:
        (bool) if string is palindom returns True and False if it's not
    """
    return string == string[::-1]


def count_values_in_list(_list, value):
    """
    This method returns count of value in list
    Args:
        _list (list)
        value (int|str|bool and etc)
    Returns:
        (int)
    """
    return _list.count(value)


def find_most_duplicate_value(_list):
    """
    This method finds most duplicate value from list
    Args:
        _list (list)
    Returns:
        (str/bool/int) - anything that list contains
    """
    return max(set(_list), key = _list.count)


