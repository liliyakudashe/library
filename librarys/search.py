from .book_manager import get_books


def search_by_author(author):
    books = get_books()
    result = []
    for book in books:
        if author.lower() in book['author'].lower():
            result.append(book)
    return result

