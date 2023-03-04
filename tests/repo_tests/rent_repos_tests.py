import unittest
from domain.bookrenter import BookRenter
from domain.entities import Client, Book
from repository.rent_repo import RentInMemoryRepository, RentFileRepository


class TestCaseRentMemoryRepo(unittest.TestCase):

    def setUp(self) -> None:
        self.__repo = RentInMemoryRepository()

    def tearDown(self) -> None:
        self.__repo.delete_all()

    def test_store(self):

        self.assertEqual(len(self.__repo.get_all_rents()), 0)
        client1 = Client(0, "Nume 1", "1234123412341")
        book1 = Book(0, "Titlu 1", "desc 1", "Autor 1")
        self.__repo.store(BookRenter(client1, book1))
        self.assertEqual(len(self.__repo.get_all_rents()), 1)

        client2 = Client(1, "Nume 2", "1234421412341")
        book2 = Book(1, "Titlu 2", "desc 2", "Autor 2")
        self.__repo.store(BookRenter(client2, book2))

        client3 = Client(2, "Nume 3", "3421274421341")
        book3 = Book(2, "Titlu 3", "desc 3", "Autor 3")
        self.__repo.store(BookRenter(client3, book3))

        self.assertEqual(len(self.__repo.get_all_rents()), 3)

    def test_get_all_rents(self):

        rentlist = self.__repo.get_all_rents()
        self.assertEqual(len(rentlist), 0)


        client1 = Client(0, "Nume 1", "1234123412341")
        book1 = Book(0, "Titlu 1", "desc 1", "Autor 1")
        self.__repo.store(BookRenter(client1, book1))

        client2 = Client(1, "Nume 2", "1234421412341")
        book2 = Book(1, "Titlu 2", "desc 2", "Autor 2")
        self.__repo.store(BookRenter(client2, book2))

        rentlist = self.__repo.get_all_rents()
        self.assertEqual(len(rentlist), 2)


        client3 = Client(2, "Nume 3", "3421274421341")
        book3 = Book(2, "Titlu 3", "desc 3", "Autor 3")
        self.__repo.store(BookRenter(client3, book3))

        client3 = Client(2, "Nume 4", "5367125715263")
        book3 = Book(2, "Titlu 3", "desc 3", "Autor 3")
        self.__repo.store(BookRenter(client3, book3))

        rentlist = self.__repo.get_all_rents()
        self.assertEqual(len(rentlist), 4)

    def test_contains_rent(self):

        client1 = Client(0, "Nume 1", "1234123412341")
        book1 = Book(0, "Titlu 1", "desc 1", "Autor 1")
        br1 = BookRenter(client1, book1)
        self.__repo.store(br1)

        client2 = Client(1, "Nume 2", "1234421412341")
        book2 = Book(1, "Titlu 2", "desc 2", "Autor 2")
        br2 = BookRenter(client2, book2)
        self.__repo.store(br2)

        client3 = Client(2, "Nume 3", "3421274421341")
        book3 = Book(2, "Titlu 3", "desc 3", "Autor 3")
        br3 = BookRenter(client3, book3)
        self.__repo.store(br3)

        self.assertTrue(self.__repo.contains_rent(client1, book1) == br1)
        self.assertTrue(self.__repo.contains_rent(client1, book2) is None)

        br4 = BookRenter(client1, book1)
        self.assertTrue(self.__repo.contains_rent(client1, book1) == br4)

        br5 = BookRenter(client1, book3)
        self.assertTrue(self.__repo.contains_rent(client1, book3) is None)

        self.__repo.store(br5)
        self.assertTrue(self.__repo.contains_rent(client1, book3) == br5)

    def test_update_rents_for_client(self):

        client1 = Client(0, "Nume 1", "1234123412341")
        book1 = Book(0, "Titlu 1", "desc 1", "Autor 1")
        br1 = BookRenter(client1, book1)
        self.__repo.store(br1)

        client2 = Client(1, "Nume 2", "1234421412341")
        book2 = Book(1, "Titlu 2", "desc 2", "Autor 2")
        br2 = BookRenter(client2, book2)
        self.__repo.store(br2)

        client3 = Client(2, "Nume 3", "3421274421341")
        book3 = Book(2, "Titlu 3", "desc 3", "Autor 3")
        br3 = BookRenter(client3, book3)
        self.__repo.store(br3)

        self.__repo.store(BookRenter(client3, book2))

        self.__repo.update_rents_for_client(client3, client2)
        self.assertEqual(self.__repo.get_all_rents()[2].get_client(), client2)
        self.assertEqual(self.__repo.get_all_rents()[3].get_client(), client2)

        self.__repo.update_rents_for_client(client2, client1)
        self.assertEqual(self.__repo.get_all_rents()[1].get_client(), client1)

    def test_delete_all(self):

        self.__repo.delete_all()
        self.assertTrue(self.__repo.get_all_rents() == [])
        self.assertEqual(self.__repo.size(), 0)



class TestCaseRentFileRepo(unittest.TestCase):

    def setUp(self) -> None:
        self.__repo = RentFileRepository("test_rent_repo.txt")
        self.__repo.delete_all()

    def tearDown(self) -> None:
        self.__repo.delete_all()

    def test_store(self):

        self.assertEqual(len(self.__repo.get_all_rents()), 0)
        client1 = Client(0, "Nume 1", "1234123412341")
        book1 = Book(0, "Titlu 1", "desc 1", "Autor 1")
        self.__repo.store(BookRenter(client1, book1))
        self.assertEqual(len(self.__repo.get_all_rents()), 1)

        client2 = Client(1, "Nume 2", "1234421412341")
        book2 = Book(1, "Titlu 2", "desc 2", "Autor 2")
        self.__repo.store(BookRenter(client2, book2))

        client3 = Client(2, "Nume 3", "3421274421341")
        book3 = Book(2, "Titlu 3", "desc 3", "Autor 3")
        self.__repo.store(BookRenter(client3, book3))

        self.assertEqual(len(self.__repo.get_all_rents()), 3)

    def test_get_all_rents(self):

        rentlist = self.__repo.get_all_rents()
        self.assertEqual(len(rentlist), 0)


        client1 = Client(0, "Nume 1", "1234123412341")
        book1 = Book(0, "Titlu 1", "desc 1", "Autor 1")
        self.__repo.store(BookRenter(client1, book1))

        client2 = Client(1, "Nume 2", "1234421412341")
        book2 = Book(1, "Titlu 2", "desc 2", "Autor 2")
        self.__repo.store(BookRenter(client2, book2))

        rentlist = self.__repo.get_all_rents()
        self.assertEqual(len(rentlist), 2)


        client3 = Client(2, "Nume 3", "3421274421341")
        book3 = Book(2, "Titlu 3", "desc 3", "Autor 3")
        self.__repo.store(BookRenter(client3, book3))

        client3 = Client(2, "Nume 4", "5367125715263")
        book3 = Book(2, "Titlu 3", "desc 3", "Autor 3")
        self.__repo.store(BookRenter(client3, book3))

        rentlist = self.__repo.get_all_rents()
        self.assertEqual(len(rentlist), 4)

    def test_contains_rent(self):

        client1 = Client(0, "Nume 1", "1234123412341")
        book1 = Book(0, "Titlu 1", "desc 1", "Autor 1")
        br1 = BookRenter(client1, book1)
        self.__repo.store(br1)

        client2 = Client(1, "Nume 2", "1234421412341")
        book2 = Book(1, "Titlu 2", "desc 2", "Autor 2")
        br2 = BookRenter(client2, book2)
        self.__repo.store(br2)

        client3 = Client(2, "Nume 3", "3421274421341")
        book3 = Book(2, "Titlu 3", "desc 3", "Autor 3")
        br3 = BookRenter(client3, book3)
        self.__repo.store(br3)

        self.assertTrue(self.__repo.contains_rent(client1, book1) == br1)
        self.assertTrue(self.__repo.contains_rent(client1, book2) is None)

        br4 = BookRenter(client1, book1)
        self.assertTrue(self.__repo.contains_rent(client1, book1) == br4)

        br5 = BookRenter(client1, book3)
        self.assertTrue(self.__repo.contains_rent(client1, book3) is None)

        self.__repo.store(br5)
        self.assertTrue(self.__repo.contains_rent(client1, book3) == br5)

    def test_update_rents_for_client(self):

        client1 = Client(0, "Nume 1", "1234123412341")
        book1 = Book(0, "Titlu 1", "desc 1", "Autor 1")
        br1 = BookRenter(client1, book1)
        self.__repo.store(br1)

        client2 = Client(1, "Nume 2", "1234421412341")
        book2 = Book(1, "Titlu 2", "desc 2", "Autor 2")
        br2 = BookRenter(client2, book2)
        self.__repo.store(br2)

        client3 = Client(2, "Nume 3", "3421274421341")
        book3 = Book(2, "Titlu 3", "desc 3", "Autor 3")
        br3 = BookRenter(client3, book3)
        self.__repo.store(br3)

        self.__repo.store(BookRenter(client3, book2))

        self.__repo.update_rents_for_client(client3, client2)
        self.assertEqual(self.__repo.get_all_rents()[2].get_client(), client2)
        self.assertEqual(self.__repo.get_all_rents()[3].get_client(), client2)

        self.__repo.update_rents_for_client(client2, client1)
        self.assertEqual(self.__repo.get_all_rents()[1].get_client(), client1)

    def test_delete_all(self):

        self.__repo.delete_all()
        self.assertTrue(self.__repo.get_all_rents() == [])
        self.assertEqual(self.__repo.size(), 0)
