def get_unique_list_numbers() -> list[int]:
    # TODO написать функцию для получения списка уникальных целых чисел
    import random
    return random.sample(range(-10, 10), k=15, counts=None)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
