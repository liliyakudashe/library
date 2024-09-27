from librarys.book_manager import add_book


def add_multiple_books():
    while True:
        title = input("Введите название книги (или 'exit' для завершения)")
        if title.lower() == 'exit':
            break
        author = input('Введите автора книги')
        add_book(title, author)