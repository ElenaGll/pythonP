# !/usr/bin/env python3


from brain_tasks.tasks.find_where import find_where


def main():
    books = [
        {'title': 'Book of Fooos', 'author': 'Foo', 'year': 1111},
        {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611},
        {'title': 'The Tempest', 'author': 'Shakespeare', 'year': 1611},
        {'title': 'Book of Foos Barrrs', 'author': 'FooBar', 'year': 2222},
        {'title': 'Still foooing', 'author': 'FooBar', 'year': 333},
        {'title': 'Happy Foo', 'author': 'FooBar', 'year': 4444},
    ]

    print(find_where(books, books[2])) #books[2]


if __name__ == '__main__':
    main()
