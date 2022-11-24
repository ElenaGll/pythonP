from brain_tasks.tasks.longest_length import find_longest_length


if find_longest_length('jabcjdelg') != 8:
    raise Exception('Функция работает неверно!')

if find_longest_length('') != 0:
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')