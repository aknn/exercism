def proverb(*items, qualifier=None):
    if not items:
        return []

    lines = []
    for i in range(len(items) - 1):
        lines.append(f"For want of a {items[i]} the {items[i+1]} was lost.")

    first_item = items[0]
    if qualifier:
        final_line = f"And all for the want of a {qualifier} {first_item}."
    else:
        final_line = f"And all for the want of a {first_item}."

    lines.append(final_line)

    return lines