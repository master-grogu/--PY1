list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
index_max = 0
max_value = list_numbers[0]
for index, value in enumerate(list_numbers):
    if value >= max_value:
        index_max, max_value = index, value
list_numbers[index_max], list_numbers[-1] = list_numbers[-1], list_numbers[index_max]
print(list_numbers)
