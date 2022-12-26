def partition(items, left, right, pivot):
    while True:
        while items[left] < pivot:
            left += 1
        while items[right] > pivot:
            right -= 1
        if left >= right:
            return right + 1
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1


def sort(items, left, right):
    length = right - left + 1
    if length < 2:
        return
    pivot = items[left]
    split_index = partition(items, left, right, pivot)
    sort(items, left, split_index - 1)
    sort(items, split_index, right)


def solution(items):
    sort(items, 0, len(items) - 1)


items = [10, 20, 0, -1]
solution(items)
print(items)
