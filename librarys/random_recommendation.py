import random
from .book_manager import get_books


def recommend_book():
    books = get_books()
    if not books:
        print('Нет доступных книг для рекомдации')
        return
    recommended = random.choice(books)
    print(f"Рекомендуемая книга: '{recommended['title']}'автор: {recommended['author']}")