def get_count_char(str_):
    str_ = str_.lower()  # в нижний регистр
    dict_count = {}
    for char in str_:  # явл ли символ буквой, если да, кидаем в словарь увеличивая на один
        if char.isalpha():
            if char in dict_count:
                dict_count[char] += 1
            else:
                dict_count[char] = 1
    return dict_count


def get_char_percent(dict_count):   # блок вычисления процентного отношения
    all_count = sum(dict_count.values())  # сумма всего символов
    char_percent = {}
    for char, count in dict_count.items():
        char_percent[char] = (count / all_count) * 100  # отношение символа к сумме
    return char_percent

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
dict_count = get_count_char(main_str)
print(dict_count)
