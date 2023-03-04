import unittest

from domain.entities import Book
from repository.book_repo import BookInMemoryRepository, BookFileRepository


class TestCaseBookMemoryRepo(unittest.TestCase):

    def setUp(self) -> None:
        self.__repo = BookInMemoryRepository()

        self.__repo.store(Book(0, "Biblioteca de la miezul noptii", "desc carte", "Matt Haig"))
        self.__repo.store(Book(1, "Despre Destin", "desc carte", "Andrei Plesu"))
        self.__repo.store(Book(2, "Gambitul Damei", "desc carte", "Walter Tevis"))
        self.__repo.store(Book(3, "Institutul", "desc carte", "Stephen King"))
        self.__repo.store(Book(4, "Exalare", "desc carte", "Ted Chiang"))

    def tearDown(self) -> None:
        self.__repo.delete_all()

    def test_store_book(self):

        b1 = Book(23, "Carte 1", "descriere 1", "autor 1")
        self.__repo.store(b1)
        self.assertEqual(len(self.__repo.get_booklist()), 6)

        b2 = Book(42, "Carte 2", "descriere 2", "autor 2")
        self.__repo.store(b2)
        self.assertEqual(len(self.__repo.get_booklist()), 7)

    def test_get_all_books(self):

        booklist = self.__repo.get_booklist()
        self.assertEqual(len(booklist), 5)

        self.__repo.store(Book(5, "Carte 1", "asd asd", "Autor 1"))
        self.__repo.store(Book(6, "Carte 2", "bla bla", "Autor 2"))


        booklist = self.__repo.get_booklist()
        self.assertEqual(len(booklist), 7)

        self.__repo.store(Book(6, "Carte 3", "asd asd", "Autor 3"))
        self.__repo.store(Book(6, "Carte 4", "bla bla", "Autor 4"))

        booklist = self.__repo.get_booklist()
        self.assertEqual(len(booklist), 9)

    def test_update_book(self):

        book_list = self.__repo.get_booklist()

        updated_book1 = Book(3, "Titlu nou", "descriere noua", "Autor nou")
        self.__repo.update_book(3, updated_book1)
        self.assertTrue(book_list[3].get_title() == "Titlu nou")
        self.assertTrue(book_list[3].get_desc() == "descriere noua")
        self.assertTrue(book_list[3].get_auth() == "Autor nou")

        updated_book2 = Book(4, "Titlu nou 1", "descriere noua 1", "Autor nou 1")
        self.__repo.update_book(4, updated_book2)
        self.assertTrue(book_list[4].get_title() == "Titlu nou 1")
        self.assertTrue(book_list[4].get_desc() == "descriere noua 1")
        self.assertTrue(book_list[4].get_auth() == "Autor nou 1")

    def test_delete_book(self):

        b1 = Book(0, "Carte 1", "asd asd", "Autor 1")
        self.__repo.store(b1)
        b2 = Book(1, "Carte 2", "asd asd", "Autor 2")
        self.__repo.store(b2)
        b3 = Book(2, "Carte 3", "asd asd", "Autor 3")
        self.__repo.store(b3)
        b4 = Book(3, "Carte 4", "asd asd", "Autor 4")
        self.__repo.store(b4)
        b5 = Book(4, "Carte 5", "asd asd", "Autor 5")
        self.__repo.store(b5)

        self.__repo.delete_book(b3)
        self.assertEqual(b5.get_id(), 8)
        self.assertEqual(len(self.__repo.get_booklist()), 9)

        self.__repo.delete_book(b1)
        self.assertEqual(b4.get_id(), 6)
        self.assertEqual(len(self.__repo.get_booklist()), 8)

    def test_get_book_with_id(self):

        book1 = self.__repo.get_book_with_id(1)
        self.assertTrue(book1.get_id() == 1)
        self.assertTrue(book1.get_title() == "Despre Destin")
        self.assertTrue(book1.get_auth() == "Andrei Plesu")

        book2 = self.__repo.get_book_with_id(4)
        self.assertTrue(book2.get_id() == 4)
        self.assertTrue(book2.get_title() == "Exalare")
        self.assertTrue(book2.get_auth() == "Ted Chiang")

        book3 = self.__repo.get_book_with_id(0)
        self.assertTrue(book3.get_id() == 0)
        self.assertTrue(book3.get_title() == "Biblioteca de la miezul noptii")
        self.assertTrue(book3.get_auth() == "Matt Haig")

    def test_delete_all(self):

        self.__repo.delete_all()
        self.assertTrue(self.__repo.get_booklist() == [])
        self.assertEqual(self.__repo.size(), 0)



class TestCaseBookFileRepo(unittest.TestCase):

    def setUp(self) -> None:
        self.__repo = BookFileRepository("test_book_repo.txt")
        self.__repo.delete_all()

        self.__repo.store(Book(0, "Biblioteca de la miezul noptii", "desc carte", "Matt Haig"))
        self.__repo.store(Book(1, "Despre Destin", "desc carte", "Andrei Plesu"))
        self.__repo.store(Book(2, "Gambitul Damei", "desc carte", "Walter Tevis"))
        self.__repo.store(Book(3, "Institutul", "desc carte", "Stephen King"))
        self.__repo.store(Book(4, "Exalare", "desc carte", "Ted Chiang"))

    def tearDown(self) -> None:
        self.__repo.delete_all()

    def test_store_book(self):

        b1 = Book(23, "Carte 1", "descriere 1", "autor 1")
        self.__repo.store(b1)
        self.assertEqual(len(self.__repo.get_booklist()), 6)

        b2 = Book(42, "Carte 2", "descriere 2", "autor 2")
        self.__repo.store(b2)
        self.assertEqual(len(self.__repo.get_booklist()), 7)

    def test_get_all_books(self):

        booklist = self.__repo.get_booklist()
        self.assertEqual(len(booklist), 5)

        self.__repo.store(Book(5, "Carte 1", "asd asd", "Autor 1"))
        self.__repo.store(Book(6, "Carte 2", "bla bla", "Autor 2"))


        booklist = self.__repo.get_booklist()
        self.assertEqual(len(booklist), 7)

        self.__repo.store(Book(6, "Carte 3", "asd asd", "Autor 3"))
        self.__repo.store(Book(6, "Carte 4", "bla bla", "Autor 4"))

        booklist = self.__repo.get_booklist()
        self.assertEqual(len(booklist), 9)

    def test_update_book(self):

        book_list = self.__repo.get_booklist()

        updated_book1 = Book(3, "Titlu nou", "descriere noua", "Autor nou")
        self.__repo.update_book(3, updated_book1)
        self.assertTrue(book_list[3].get_title() == "Titlu nou")
        self.assertTrue(book_list[3].get_desc() == "descriere noua")
        self.assertTrue(book_list[3].get_auth() == "Autor nou")

        updated_book2 = Book(4, "Titlu nou 1", "descriere noua 1", "Autor nou 1")
        self.__repo.update_book(4, updated_book2)
        self.assertTrue(book_list[4].get_title() == "Titlu nou 1")
        self.assertTrue(book_list[4].get_desc() == "descriere noua 1")
        self.assertTrue(book_list[4].get_auth() == "Autor nou 1")

    def test_delete_book(self):

        b1 = Book(0, "Carte 1", "asd asd", "Autor 1")
        self.__repo.store(b1)
        b2 = Book(1, "Carte 2", "asd asd", "Autor 2")
        self.__repo.store(b2)
        b3 = Book(2, "Carte 3", "asd asd", "Autor 3")
        self.__repo.store(b3)
        b4 = Book(3, "Carte 4", "asd asd", "Autor 4")
        self.__repo.store(b4)
        b5 = Book(4, "Carte 5", "asd asd", "Autor 5")
        self.__repo.store(b5)

        self.__repo.delete_book(b3)
        self.assertEqual(len(self.__repo.get_booklist()), 9)

        self.__repo.delete_book(b1)
        self.assertEqual(len(self.__repo.get_booklist()), 8)

    def test_get_book_with_id(self):

        book1 = self.__repo.get_book_with_id(1)
        self.assertTrue(book1.get_id() == 1)
        self.assertTrue(book1.get_title() == "Despre Destin")
        self.assertTrue(book1.get_auth() == "Andrei Plesu")

        book2 = self.__repo.get_book_with_id(4)
        self.assertTrue(book2.get_id() == 4)
        self.assertTrue(book2.get_title() == "Exalare")
        self.assertTrue(book2.get_auth() == "Ted Chiang")

        book3 = self.__repo.get_book_with_id(0)
        self.assertTrue(book3.get_id() == 0)
        self.assertTrue(book3.get_title() == "Biblioteca de la miezul noptii")
        self.assertTrue(book3.get_auth() == "Matt Haig")

    def test_delete_all(self):

        self.__repo.delete_all()
        self.assertTrue(self.__repo.get_booklist() == [])
        self.assertEqual(self.__repo.size(), 0)
