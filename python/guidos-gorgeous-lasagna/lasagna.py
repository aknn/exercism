EXPECTED_BAKE_TIME = 40  # in minutes
PREPARATION_TIME = 2     # in minutes per layer

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(layers):
    """Calculate preparation time based on number of layers.

    :param layers: int - number of lasagna layers.
    :return: int - total preparation time (in minutes), assuming each layer takes `PREPARATION_TIME` minutes.
    """
    return layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total time spent in kitchen.

    :param number_of_layers: int - number of lasagna layers.
    :param elapsed_bake_time: int - time lasagna has already been baking.
    :return: int - total time spent (prep + baking so far).
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
