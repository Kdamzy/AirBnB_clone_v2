""" A module to hold utility functions"""


def list_to_dict(lst):
    """
    Converts a list to a dictionary where the keys are the indices of the list elements.
    e.g list = [name="destiny", age=23, height=160.3 ]

    Args:
        lst (list): The list to be converted.

    Returns:
        dict: A dictionary where the keys are the indices of the list elements and the values are the corresponding list elements.
    """
    result = {}
    for obj in lst:
        obj = obj.split("=")
        key = obj[0]
        value = obj[1]

        if value[0] == '"' and value[-1] == '"':
            value = value[1:-1]

        value = value.replace("_", " ")

        result[key] = value

    return result