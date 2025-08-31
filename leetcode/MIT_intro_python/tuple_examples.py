# Tuple examples: indexing and slicing

t = (10, 20, 30, (40, 50), "hello", [1, 2, 3], 99.9)

print("t[0]:", t[0])
print("t[3:]:", t[3:])
print("t[3][1]:", t[3][1])  # Accessing element inside nested tuple
print("t[4]:", t[4])
print("t[::-2]:", t[::-2])
print("t[:3]:", t[:3])
print("t[:1:-2]:", t[:1:-2])
# Accessing element inside list inside tuple
print("t[5][2]:", t[5][2])

def fancy_divide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i, _ in enumerate(list_of_numbers):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)

fancy_divide([0, 2, 41, 0], 3)
