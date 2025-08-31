COLORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def label(colors):
    """
    Calculate the resistance value of a resistor based on its color bands.
    """
    value = (COLORS[colors[0]] * 10 + COLORS[colors[1]]) * (10 ** COLORS[colors[2]])

    if value >= 10**9:
        return f"{value // 10**9} gigaohms"
    if value >= 10**6:
        return f"{value // 10**6} megaohms"
    if value >= 10**3:
        return f"{value // 10**3} kiloohms"
    return f"{value} ohms"