def foo():
    n = int(input())
    lst = []
    for _ in range(n):
        operation, *number = input().split()
        lst += [operation]
        lst += list(map(int, number))

    result = []
    i = 0
    while i < len(lst):
        if lst[i] == 'append':
            result.append(lst[i + 1])
            i += 2
        if lst[i] == 'insert':
            result.insert(lst[i + 1], lst[i + 2])
            i += 3
        if lst[i] == 'remove':
            result.remove(lst[i + 1])
            i += 2
        if lst[i] == 'pop':
            result.pop()
            i += 1
        if lst[i] == 'sort':
            result.sort()
            i += 1
        if lst[i] == 'reverse':
            result.reverse()
            i += 1
        if lst[i] == 'print':
            print(list(result))
            i += 1


foo()
