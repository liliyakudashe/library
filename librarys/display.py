def display_books(books):
    if not books:
        print('Книги не найдены')
        return
    print('Список книг:')
    for idx, book in enumerate(books, start=1):
        print(f"{idx}. '{book['title']} автор: {book['author']}'")