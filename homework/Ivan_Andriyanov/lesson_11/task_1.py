class Book:
    material_page = "Бумага"
    existence_text = True

    def __init__(self, book_name, author, page_book, isbn,
                 reserved_book=False):
        self.book_name = book_name
        self.author = author
        self.page_book = page_book
        self.isbn = isbn
        self.reserved_book = reserved_book

    def __str__(self):
        result = f'Название: {self.book_name}, Автор: {self.author},\
              страниц: {self.page_book}, материал: {self.material_page}'
        if self.reserved_book:
            result += ", зарезервирована"
        return result


book1 = Book('Идиот', 'Достаевский', 12313, 500)
book2 = Book('Русалочка', 'Андерсен', 12313, 100)
book3 = Book('Война и мир', 'Толстой', 123123, 5000)
book4 = Book('Голый король', 'Андерсен', 13131313, 100)
book5 = Book('Дориан Грей', 'Уайльд', 1231313, 500)

book3.reserved_book = True

for book in [book1, book2, book3, book4, book5]:
    print(book)


class School_subject(Book):
    def __init__(
        self,
        book_name,
        author,
        page_book,
        isbn,
        reserved_book=False,
        subject=None,
        school_class=None,
        availability_task=False
    ):
        super().__init__(book_name, author, page_book, isbn, reserved_book)
        self.subject = subject
        self.school_class = school_class
        self.availability_task = availability_task

    def __str__(self):
        result = f'Название: {self.book_name}, Автор: {self.author},\
              страниц: {self.page_book}, материал: {self.material_page},\
                  предмет: {self.subject}, класс: {self.school_class}'
        if self.reserved_book:
            result += ", зарезервирована"
        return result


subject_scholl1 = School_subject(
    'Алгебра', 'Иванов', 500, isbn="978-MATH-9",
    reserved_book=True, subject='Математика', school_class=9
)

subject_scholl2 = School_subject(
    'Алгебра', 'Иванов', 500, isbn="978-MATH-9",
    reserved_book=False, subject='Математика', school_class=9
)

for school_book in [subject_scholl1, subject_scholl2]:
    print(school_book)
