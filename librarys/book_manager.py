books = []


def add_book(title, author):
    books.append({'title': title, 'author': author})
    print(f'Книга {title} добавлена')


def get_books():
    return books


def edit_book(old_title, new_title, new_author):
    for book in books:
        if book['title'] == old_title:
            book['title'] = new_title
            book['author'] = new_author
            print(f'Книга {old_title} обновилась на {new_title}')
            return
        print(f'Книга {old_title} не найдена')


def remove_book(title):
    global books
    new_books = []
    inital_len = len(books)
    for book in books:
        if book['title'] != title:
            new_books.append(book)
    books = new_books
    if len(books) < inital_len:
        print(f'Книга {title} удалена')
    else:
        print(f'Книга {title} не найдена')


