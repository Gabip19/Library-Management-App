import unittest
from domain.entities import Book, Client


class TestCaseBookDomain(unittest.TestCase):

    def test_create_book(self):

        book = Book(0, "titlu", "descriere", "autor")

        self.assertTrue(book.get_id() == 0)
        self.assertTrue(book.get_title() == "titlu")
        self.assertTrue(book.get_desc() == "descriere")
        self.assertTrue(book.get_auth() == "autor")

        book.set_id(1)
        book.set_title("titlu nou")
        book.set_desc("descriere noua")
        book.set_auth("autor nou")

        self.assertTrue(book.get_id() == 1)
        self.assertTrue(book.get_title() == "titlu nou")
        self.assertTrue(book.get_desc() == "descriere noua")
        self.assertTrue(book.get_auth() == "autor nou")

    def test_equal_book(self):

        b1 = Book(0, "Titlu", "Descriere", "Autor")
        b2 = Book(1, "Titlu", "Alta Descriere", "Autor")
        self.assertEqual(b1, b2)

        b3 = Book(0, "Alt Titlu", "Descriere", "Alt Autor")
        self.assertNotEqual(b1, b3)

        b4 = Book(3, "Titlu", "Ceva descriere", "Alt Autor")
        self.assertNotEqual(b1, b4)



class TestCaseClientDomain(unittest.TestCase):

    def test_create_client(self):

        c = Client(23, "Mihai Popescu", "1020120221317")
        self.assertTrue(c.get_name() == "Mihai Popescu")
        self.assertTrue(c.get_id() == 23)
        self.assertTrue(c.get_CNP() == "1020120221317")

        c.set_name("Popescu Andrei")
        c.set_id(42)
        c.set_CNP("1234567890123")

        self.assertTrue(c.get_name() == "Popescu Andrei")
        self.assertTrue(c.get_id() == 42)
        self.assertTrue(c.get_CNP() == "1234567890123")

    def test_equal_client(self):
        c1 = Client(23, "Mihai Popescu", "1020120221317")
        c2 = Client(42, "Mihai Popescu", "1020120221317")
        self.assertEqual(c1, c2)

        c3 = Client(62, "Alex Toma", "1020120221317")
        self.assertNotEqual(c1, c3)

        c4 = Client(42, "Mihai Popescu", "1020120225215")
        self.assertNotEqual(c1, c4)
