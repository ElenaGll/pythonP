def find_longest_length(string):
    word = ''
    length = [0]
    i = 0
    while i < len(string):
        if string[i] not in word:
            if i == len(string) - 1:
                word += string[i]
                length.append(len(word))
            else:
                word += string[i]
                i += 1
        else:
            length.append(len(word))
            start_i = string.find(word)
            i = string.find(string[i], start_i) + 1
            word = ''
    return max(length)
