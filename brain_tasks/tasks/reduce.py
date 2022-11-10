def reduce(operation, initial_value, items):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)
    return acc
