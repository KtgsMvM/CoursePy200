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


class Book:
    def __init__(self, id_: int, name_: str, pages_: int):
           if not isinstance(id_, int):# проверяем, что id_ типа int
               raise TypeError # вызываем ошибку
           if id_ < 0:
               raise ValueError
           self.id = id_
           if not isinstance(name_, str):
               raise TypeError
           self.name = name_
           if not isinstance(pages_, int):
               raise TypeError
           if pages_ < 0:
               raise ValueError
           self.pages = pages_

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name={self.name!r}, pages={self.pages})"

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_= book_dict["id"], name_= book_dict["name"], pages_= book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
