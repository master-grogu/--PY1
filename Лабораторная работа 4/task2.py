def get_count_char(str_):
    alphabet = {}
    COUNT = 0
    for char in str_.lower():
        if char.isalpha():
            alphabet[char] = alphabet.get(char, COUNT) +1
    return alphabet

def get_percent(dict_): # вторая функция считающая процентрное соотношение
    dict_1 = {}
    for key in dict_.keys():
        dict_1[key] = dict_[key]/ sum(dict_.values()) * 100
    return dict_1

    # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
