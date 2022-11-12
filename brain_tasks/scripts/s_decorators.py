# !/usr/bin/env python3


from brain_tasks.tasks.examples import f


def main():
    print(f(1))
    # => Calculating...
    # 10
    print(f(1))  # будет "вспомнено"
    # 10
    print(f(2))
    # => Calculating...
    # 20
    print(f(3))
    # => Calculating...
    # 30
    print(f(4))  # вытеснит запомненный результат для "1"
    # => Calculating...
    # 40
    print(f(1))  # будет перевычислено
    # => Calculating...
    # 10


if __name__ == '__main__':
    main()
