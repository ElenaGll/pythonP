def find_index(value, items):
    for index, item in enumerate(items):
        if item == value:
            return index


def find_longest_length(string):
    length = []
    for i in string:
        indexes = []
        iterator = iter(string)
        first_index = find_index(i, iterator)
        second_index = find_index(i, iterator)
        if second_index is None:
            continue
        indexes.append(first_index)
        indexes.append(second_index + first_index + 1)
        while iterator:
            other_index = find_index(i, iterator)
            if other_index is None:
                break
            else:
                indexes.append(other_index + indexes[-1] + 1)
        if len(indexes) == 2:
            first_l = abs(0 - indexes[1])
            second_l = abs(indexes[0] - len(string) + 1)
            length.append(max(first_l, second_l))
            break
        if 0 not in indexes:
            indexes.append(0)
        elif len(string) - 1 not in indexes:
            indexes.append(len(string) - 1)
        all_len = []
        for j in range(len(indexes) - 2):
            all_len.append(abs(indexes[j] - indexes[j + 2]))

        length.append(max(all_len))

    # return indexes
    print(max(length))
    # print(length)
