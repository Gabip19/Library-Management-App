import unittest

from domain.entities import Book, Client
from domain.validators import BookValidator, ClientValidator, IdValidator


class TestCaseValidatorsDomain(unittest.TestCase):

    def test_validate_book(self):

        validator = BookValidator()

        b1 = Book(23, "Cartea 1", "descriere 1", "autor 1")
        b2 = Book(42, "Cartea 2", "descriere 2", "autor 2")
        validator.validate(b1)
        validator.validate(b2)

        b3 = Book(54, "Carte", "descriere 3", "autor")
        self.assertRaises(ValueError, validator.validate, b3)

        b4 = Book(68, "Carte", "descriere", "autor 2")
        self.assertRaises(ValueError, validator.validate, b4)

        b5 = Book(15, "Carte", "descriere", "autor")
        self.assertRaises(ValueError, validator.validate, b5)

    def test_validate_client(self):

        validator = ClientValidator()

        c1 = Client(13, "Adrian Doroftei", "1234567890123")
        c2 = Client(24, "Flavian Ionescu", "9012324567821")
        validator.validate(c1)
        validator.validate(c2)

        c3 = Client(54, "Ioan", "1234567890123")
        self.assertRaises(ValueError, validator.validate, c3)

        c4 = Client(42, "Ioan Matei", "123456789")
        self.assertRaises(ValueError, validator.validate, c4)

        c5 = Client(1, "Ioan Matei", "123456789012345")
        self.assertRaises(ValueError, validator.validate, c5)

        c6 = Client(1, "Ioan Matei", "12345asdas123")
        self.assertRaises(ValueError, validator.validate, c6)

        c7 = Client(1, "Ioan", "123412341234")
        self.assertRaises(ValueError, validator.validate, c7)

    def test_validate_id(self):

        validator = IdValidator()

        id1 = 3
        list1 = [1, 2, 3, 4]
        validator.validate(id1, list1)

        id2 = 1
        list2 = [1, 2]
        validator.validate(id2, list2)

        self.assertRaises(ValueError, validator.validate, "asd", [1, 2, 3])

        self.assertRaises(ValueError, validator.validate, -1, [1, 2, 3])

        self.assertRaises(ValueError, validator.validate, 3, [1, 2, 3])
