def if_palindrom(string):
    """
    This method checks if string palindrom.
    Args:
        string (str)
    Returns:
        (bool) if string is palindom returns True and False if it's not
    """
    return string == string[::-1]


def count_values_in_list(list, value):
    """
    This method returns count of value in list
    Args:
        list (list)
        value (int|str|bool and etc)
    Returns:
        (int)
    """
    return list.count(value)
