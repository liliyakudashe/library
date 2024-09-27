import random
from .book_manager import get_books


def recommend_book():
    books = get_books()
    if not books:
        print(f'Нет доступных книг')
        return
    recommend = random.choice(books)
    print(f'Рекомендованная книга {recommend['title']}  автор {recommend['author']}')