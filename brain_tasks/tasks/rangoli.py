def print_rangoli():
    s = input()
    size = int(s)
    chars = 'abcdefghijklmnopqrstuvwxyz'
    chars = chars.upper()
    i = size - 1
    while i >= 0:
        print('-'.join(list(chars[(size - 1):i:-1] +
                            chars[i:size])).center((size * 4 - 3), '-'))
        i -= 1
    i += 2
    while i < size:
        print('-'.join(list(chars[(size - 1):i:-1] +
                            chars[i:size])).center((size * 4 - 3), '-'))
        i += 1


print_rangoli()
