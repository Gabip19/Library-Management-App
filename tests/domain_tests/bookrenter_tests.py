import unittest
from domain.entities import Book, Client
from domain.bookrenter import BookRenter


class TestCaseBookRenterDomain(unittest.TestCase):

    def test_create_renter(self):

        client1 = Client(0, "Nume 1", "1234567890123")
        book1 = Book(0, "Titlu 1", "desc 1", "Autor 1")

        br1 = BookRenter(client1, book1)
        self.assertTrue(br1.get_client().get_id() == 0)
        self.assertTrue(br1.get_client().get_name() == "Nume 1")
        self.assertTrue(br1.get_client().get_CNP() == "1234567890123")
        self.assertTrue(br1.get_rented_book().get_id() == 0)
        self.assertTrue(br1.get_rented_book().get_title() == "Titlu 1")
        self.assertTrue(br1.get_rented_book().get_desc() == "desc 1")
        self.assertTrue(br1.get_rented_book().get_auth() == "Autor 1")

        client2 = Client(1, "Nume 2", "1234123412341")
        book2 = Book(1, "Titlu 2", "desc 2", "Autor 2")

        br2 = BookRenter(client2, book2)
        self.assertTrue(br2.get_client().get_id() == 1)
        self.assertTrue(br2.get_client().get_name() == "Nume 2")
        self.assertTrue(br2.get_client().get_CNP() == "1234123412341")
        self.assertTrue(br2.get_rented_book().get_id() == 1)
        self.assertTrue(br2.get_rented_book().get_title() == "Titlu 2")
        self.assertTrue(br2.get_rented_book().get_desc() == "desc 2")
        self.assertTrue(br2.get_rented_book().get_auth() == "Autor 2")

    def test_equal_renter(self):

        client1 = Client(0, "Nume 1", "1234567890123")
        book1 = Book(0, "Titlu 1", "desc 1", "Autor 1")
        br1 = BookRenter(client1, book1)

        client2 = Client(5, "Nume 1", "1234567890123")
        book2 = Book(3, "Titlu 1", "descriere carte", "Autor 1")
        br2 = BookRenter(client2, book2)
        self.assertEqual(br1, br2)

        book3 = Book(3, "Titlu 1", "descriere carte", "Autor 1")
        br3 = BookRenter(client2, book3)
        self.assertEqual(br3, br2)
        self.assertEqual(br3, br1)

        client3 = Client(5, "Nume 1", "1234567890123")
        book3 = Book(3, "Titlu", "descriere carte", "Autor 1")
        br4 = BookRenter(client3, book3)
        self.assertNotEqual(br4, br1)
        self.assertNotEqual(br4, br2)

        client4 = Client(5, "Alt nume", "1234567890123")
        br5 = BookRenter(client4, book3)
        self.assertNotEqual(br5, br1)
        self.assertNotEqual(br5, br2)
