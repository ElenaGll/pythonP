def find_where(books, search):
    if search:
        if 'author' in search and 'year' in search:
            for book in books:
                if book['author'] == search['author'] and book['year'] == search['year']:
                    return book
            return None
        elif 'author' in search:
            for book in books:
                if book['author'] == search['author']:
                    return book
            return None
        elif 'year' in search:
            for book in books:
                if book['year'] == search['year']:
                    return book
            return None
        # elif 'author' or 'year' not in list(search.keys()):
        #     return None
        else:
            return None
    else:
        return books[0]
