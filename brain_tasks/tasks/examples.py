def sort_by_ext(files):
    new_files = []
    for file in files:
        new_files.append(file.split('.'))
    sorted_files = sorted(new_files)

    len_files = []
    for file in sorted_files:
        len_files.append(len(file))
    sorted_len = sorted(set(len_files))

    result = []
    for i in sorted_len:
        for file in sorted_files:
            if len(file) == i:
                result.append(file)

    result_files = []
    for file in result:
        result_files.append('.'.join(file))

    return result_files
