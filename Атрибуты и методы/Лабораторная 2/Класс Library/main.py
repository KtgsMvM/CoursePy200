BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id: int, name: str, pages: int):
        if not isinstance(id, int):  # проверяем, что id_ типа int
            raise TypeError  # вызываем ошибку
        if id < 0:
            raise ValueError
        self.id = id
        if not isinstance(name, str):
            raise TypeError
        self.name = name
        if not isinstance(pages, int):
            raise TypeError
        if pages < 0:
            raise ValueError
        self.pages = pages


# TODO написать класс Library
class Library:
    def __int__(self, list_books: list = None):
        if list_books is None:
            self.books = []
        else:
            self.books = list_books

    def get_next_book_id(self, next_book_id: int):
        if next_book_id is None:
            if not self.books:
                return 1
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int):
        for index_book_in_books, book in enumerate(self.books):
            if book.id == book_id:
                return index_book_in_books
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
