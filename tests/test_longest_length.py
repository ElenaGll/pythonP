from brain_tasks.tasks.longest_length import find_longest_length


def test_find_longest_length():
    assert find_longest_length('jabcjdelg') == 8


def test_find_longest_length_for_empty_stryng():
    assert find_longest_length('') == 0
