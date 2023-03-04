import unittest
from domain.validators import BookValidator
from repository.book_repo import BookInMemoryRepository
from service.book_service import BookService


class TestCaseBookService(unittest.TestCase):

    def setUp(self) -> None:
        repo = BookInMemoryRepository()
        validator = BookValidator()
        self.__book_srv = BookService(repo, validator)

        self.__book_srv.add_book("Biblioteca de la miezul noptii", "desc carte", "Matt Haig")
        self.__book_srv.add_book("Despre Destin", "desc carte", "Andrei Plesu")
        self.__book_srv.add_book("Gambitul Damei", "desc carte", "Walter Tevis")
        self.__book_srv.add_book("Institutul", "desc carte", "Stephen King")
        self.__book_srv.add_book("Exalare", "desc carte", "Ted Chiang")

    def tearDown(self) -> None:
        self.__book_srv.clear_repo()

    def test_add_book(self):

        new_book1 = self.__book_srv.add_book("Carte 1", "asd asd", "Autor 1")
        self.assertTrue(new_book1.get_title() == "Carte 1")
        self.assertTrue(new_book1.get_desc() == "asd asd")
        self.assertTrue(new_book1.get_auth() == "Autor 1")
        self.assertTrue(new_book1.get_id() == 5)
        self.assertEqual(len(self.__book_srv.get_all_books()), 6)

        new_book2 = self.__book_srv.add_book("Carte 2", "bla bla", "Autor 2")
        self.assertTrue(new_book2.get_title() == "Carte 2")
        self.assertTrue(new_book2.get_desc() == "bla bla")
        self.assertTrue(new_book2.get_auth() == "Autor 2")
        self.assertTrue(new_book2.get_id() == 6)
        self.assertEqual(len(self.__book_srv.get_all_books()), 7)

        self.assertRaises(ValueError, self.__book_srv.add_book, "Carte", "bla bla", "Autor")

        self.assertRaises(ValueError, self.__book_srv.add_book, "Carte 4", "bla", "Autor 4")

    def test_get_all_books(self):

        booklist = self.__book_srv.get_all_books()
        self.assertEqual(len(booklist), 5)

        self.__book_srv.add_book("Carte 1", "asd asd", "Autor 1")
        self.__book_srv.add_book("Carte 2", "bla bla", "Autor 2")

        booklist = self.__book_srv.get_all_books()
        self.assertEqual(len(booklist), 7)

        self.__book_srv.add_book("Carte 3", "asd asd", "Autor 3")
        self.__book_srv.add_book("Carte 4", "bla bla", "Autor 4")

        booklist = self.__book_srv.get_all_books()
        self.assertEqual(len(booklist), 9)

    def test_update_book(self):

        book_list = self.__book_srv.get_all_books()
        self.__book_srv.add_book("Titlu 1", "descriere 1", "Autor 1")
        self.__book_srv.add_book("Titlu 2", "descriere 2", "Autor 2")

        self.__book_srv.update_book(0, "Titlu nou", "descriere noua", "Autor nou")
        self.assertTrue(book_list[0].get_title() == "Titlu nou")
        self.assertTrue(book_list[0].get_desc() == "descriere noua")
        self.assertTrue(book_list[0].get_auth() == "Autor nou")

        self.__book_srv.update_book(1, "Titlu nou 1", "descriere noua 1", "Autor nou 1")
        self.assertTrue(book_list[1].get_title() == "Titlu nou 1")
        self.assertTrue(book_list[1].get_desc() == "descriere noua 1")
        self.assertTrue(book_list[1].get_auth() == "Autor nou 1")

        self.assertRaises(ValueError, self.__book_srv.update_book, 1, "Titlu", "descriere noua 1", "Autor")

        self.assertRaises(ValueError, self.__book_srv.update_book, 1, "Titlu", "descriere", "Autor 1")

        self.assertRaises(ValueError, self.__book_srv.update_book, 1, "Titlu nou", "descriere noua", "Autor nou")

    def test_delete_book(self):

        self.__book_srv.add_book("Carte 1", "asd asd", "Autor 1")
        self.__book_srv.add_book("Carte 2", "asd asd", "Autor 2")
        self.__book_srv.add_book("Carte 3", "asd asd", "Autor 3")
        self.__book_srv.add_book("Carte 4", "asd asd", "Autor 4")
        self.__book_srv.add_book("Carte 5", "asd asd", "Autor 5")
        self.__book_srv.add_book("Carte 6", "asd asd", "Autor 6")

        self.__book_srv.delete_book("Carte 4", "Autor 4")
        self.assertEqual(len(self.__book_srv.get_all_books()), 10)

        self.__book_srv.delete_book("Carte 6", "Autor 6")
        self.assertEqual(len(self.__book_srv.get_all_books()), 9)

        self.assertRaises(ValueError, self.__book_srv.delete_book, "Carte 7", "Autor 7")

        self.assertRaises(ValueError, self.__book_srv.delete_book, "Carte 5", "Autor 4")

    def test_search_in_titles(self):

        new_list = self.__book_srv.search_in_titles("Cuvant")
        self.assertEqual(len(new_list), 0)

        new_list = self.__book_srv.search_in_titles("Despre Destin")
        self.assertEqual(len(new_list), 1)

        new_list = self.__book_srv.search_in_titles("Despre")
        self.assertEqual(len(new_list), 1)

        new_list = self.__book_srv.search_in_titles("Insti")
        self.assertEqual(len(new_list), 1)

        new_list = self.__book_srv.search_in_titles("DAMEI")
        self.assertEqual(len(new_list), 1)

        new_list = self.__book_srv.search_in_titles("de la miezul")
        self.assertEqual(len(new_list), 1)

        self.__book_srv.add_book("Exalarea-cartea", "desc 1", "Jeb K.")
        self.__book_srv.add_book("Exalare", "desc 2", "Tom F.")

        new_list = self.__book_srv.search_in_titles("Exalare")
        self.assertEqual(len(new_list), 3)

    def test_get_book_with_id(self):

        book1 = self.__book_srv.get_book_with_id(1)
        self.assertEqual(book1.get_id(), 1)
        self.assertEqual(book1.get_title(), "Despre Destin")
        self.assertEqual(book1.get_auth(), "Andrei Plesu")

        book2 = self.__book_srv.get_book_with_id(4)
        self.assertEqual(book2.get_id(), 4)
        self.assertEqual(book2.get_title(), "Exalare")
        self.assertEqual(book2.get_auth(), "Ted Chiang")

        book3 = self.__book_srv.get_book_with_id(0)
        self.assertEqual(book3.get_id(), 0)
        self.assertEqual(book3.get_title(), "Biblioteca de la miezul noptii")
        self.assertEqual(book3.get_auth(), "Matt Haig")

    def test_clear_repo(self):

        self.__book_srv.clear_repo()
        self.assertTrue(self.__book_srv.get_all_books() == [])
        self.assertEqual(self.__book_srv.get_list_size(), 0)
