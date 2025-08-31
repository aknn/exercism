"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Can eat ghost only if power pellet is active and touching ghost."""
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """Scores if touching either a power pellet or a dot."""
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """Loses only if touching ghost and no power pellet is active."""
    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """
    Wins if all dots are eaten and either:
    - not touching a ghost, or
    - touching a ghost but power pellet is active
    """
    return has_eaten_all_dots and (not touching_ghost or power_pellet_active)
