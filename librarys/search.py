from .book_manager import get_books


def search_by_author(author):
    books = get_books()
    results = []
    for book in books:
        if author.lower() in book['author'].lower():
            results.append(book)
    return results
