import random
from .book_manager import get_books


def recommend_book():
    books = get_books()
    if not books:
        print('Нет доступных книг для рекомендации')
        return
    recommend = random.choice(books)
    print(f"Рекомендуемая книга: '{recommend['title']} автор: {recommend['author']}'")
