import re

def find_sequences(string):
    pattern = '[a-z]+_[a-z]+'
    matches = re.findall(pattern, string)
    return matches

# Пример использования функции
print(find_sequences('this_is_a_test'))  # Вернет ['this_is', 'a_test']
