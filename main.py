from librarys.book_manager import get_books, edit_book, remove_book
from librarys.search import search_by_author
from librarys.display import display_books
from librarys.random_recommendation import recommend_book
from book_operations import add_multiple_books


def main():

    while True:
        print('1. Добавить книги')
        print('2. Показать все книги')
        print('3. Найти книги по автору')
        print('4. Рекомендовать случайную книгу')
        print('5. Редактировать книгу')
        print('6. Удалить книгу')
        print('7. Выход')

        choice = input('Выберите действие: ')

        if choice == '1':
            add_multiple_books()

        elif choice == '2':
            display_books(get_books())

        elif choice == '3':
            author = input('Введите имя автора для поиска: ')
            result = search_by_author(author)
            display_books(result)

        elif choice == '4':
            recommend_book()

        elif choice == '5':
            old_title = input('Введите текущее название книги для редактирования: ')
            new_title = input('Введите новое название книги: ')
            new_author = input('Введите нового автора книги: ')
            edit_book(old_title, new_title, new_author)

        elif choice == '6':
            title = input('Введите название книги для удаления: ')
            remove_book(title)

        elif choice == '7':
            print('Выход из программы')
            break

        else:
            print('Неверный ввод, попробуйте снова')


main()


