# !/usr/bin/env python3


from operator import add, mul


from brain_tasks.tasks.reduce import reduce


def main():
    print(reduce(add, 0, [4, 5, 6, 7, 8]))
    # print(reduce(mul, 1, [4, 5, 6]))


if __name__ == '__main__':
    main()
