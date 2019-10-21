def odd_sum(number_list):
    """
    This method gets list of numbers and returns sum of odd numbers
    Args:
        number_list (list) - list of numbers
    Returns:
        (int) - sum of all odd numbers form list
    """
    return sum([i for i in range(min(number_list), max(number_list)) if i % 2])


def even_sum(number_list):
    """
    This method gets list of numbers and returns sum of even numbers
    Args:
        number_list (list) - list of numbers
    Returns:
        (int) - sum of all odd numbers form list
    """
    return sum([i for i in range(min(number_list), max(number_list)) if i % 2])
