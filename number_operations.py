def odd_sum(numbers_list):
    """
    This method gets list of numbers and returns sum of odd numbers
    Args:
        numbers_list (list) - list of numbers
    Returns:
        (int) - sum of all odda numbers form list
    """
    try:
        return sum([i for i in range(min(numbers_list), max(numbers_list)) if i % 2])
    except Exception as e:
        print("Impossible to calculate. Error: {}".format(e))


def even_sum(numbers_list):
    """
    This method gets list of numbers and returns sum of even numbers
    Args:
        numbers_list (list) - list of numbers
    Returns:
        (int) - sum of all odd numbers form list
    """
    try:
        return sum([i for i in range(min(numbers_list), max(numbers_list)) if i % 2])
    except Exception as e:
        print("Impossible to calculate. Error: {}".format(e))


def generate_list(a, b):
    """
    This method generates list of numbers from a to b. In case of a > b returns Exeption
    Args:
         a (int)
         b (int)
    Returns:a
        (list) - list of numbers from a to b
    """
    try:
        gener_list = [i for i in range(a, b + 1)]
        return gener_list
    except Exception as e:
        print("Impossible to create list. Error: {}".format(e))


def find_max_value(numbers_list):
    """
    This method returns max value from list.
    Args:
        numbers_list (list)
    Returns:
        (int/float) number - max value from input list
    """
    try:
        return max(numbers_list)
    except Exception as e:
        print("Impossible to create list. Error: {}".format(e))


def find_min_value(numbers_list):
    """
    This method returns min value from list.
    Args:
        numbers_list (list)
    Returns:
        (int/float) number - min value from input list
    """
    try:
        return min(numbers_list)
    except Exception as e:
        print("Impossible to create list. Error: {}".format(e))
