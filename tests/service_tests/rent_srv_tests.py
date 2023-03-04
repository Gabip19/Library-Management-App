import unittest
from repository.book_repo import BookFileRepository
from repository.client_repo import ClientFileRepository
from repository.rent_repo import RentFileRepository
from service.rent_service import RentService


class TestCaseRentService(unittest.TestCase):

    def setUp(self) -> None:
        rent_repo = RentFileRepository("test_rent_srv.txt")
        client_repo = ClientFileRepository("test_client_srv.txt")
        book_repo = BookFileRepository("test_book_srv.txt")
        self.__srv = RentService(rent_repo, client_repo, book_repo)
        self.__srv.clear_repo()

    def tearDown(self) -> None:
        self.__srv.clear_repo()

    def test_get_all_rents(self):

        self.assertEqual(self.__srv.get_all_rents(), [])
        self.__srv.rent_book(3, 1)
        self.assertEqual(len(self.__srv.get_all_rents()), 1)

        self.__srv.rent_book(1, 2)
        self.__srv.rent_book(1, 1)
        self.__srv.rent_book(3, 2)
        self.assertEqual(len(self.__srv.get_all_rents()), 4)

    def test_rent_book(self):

        self.__srv.rent_book(3, 1)
        self.assertEqual(len(self.__srv.get_all_rents()), 1)

        self.assertRaises(ValueError, self.__srv.rent_book, 3, 1)

        self.__srv.rent_book(3, 2)
        self.__srv.rent_book(1, 3)
        self.assertEqual(len(self.__srv.get_all_rents()), 3)

        self.__srv.return_book(3, 1)
        self.__srv.rent_book(3, 1)
        self.assertEqual(len(self.__srv.get_all_rents()), 4)

        self.assertRaises(ValueError, self.__srv.rent_book, 3, 1)

    def test_return_book(self):

        self.__srv.rent_book(3, 1)
        self.__srv.rent_book(3, 2)

        self.__srv.return_book(3, 1)
        self.assertTrue(self.__srv.get_all_rents()[0].is_book_returned())
        self.__srv.return_book(3, 2)
        self.assertTrue(self.__srv.get_all_rents()[1].is_book_returned())

        self.assertRaises(ValueError, self.__srv.return_book, 3, 1)

        self.assertRaises(ValueError, self.__srv.return_book, 2, 1)

    def test_get_client_current_rents(self):

        self.__srv.rent_book(3, 1)
        self.__srv.rent_book(3, 4)
        self.__srv.rent_book(3, 2)

        self.assertEqual(len(self.__srv.get_client_current_rents(1)), 0)
        self.assertEqual(len(self.__srv.get_client_current_rents(3)), 3)
        self.__srv.return_book(3, 1)
        self.assertEqual(len(self.__srv.get_client_current_rents(3)), 2)

        self.__srv.rent_book(1, 2)
        self.assertEqual(len(self.__srv.get_client_current_rents(1)), 1)
        self.__srv.return_book(1, 2)
        self.__srv.rent_book(1, 2)
        self.assertEqual(len(self.__srv.get_client_current_rents(1)), 1)

    def test_get_client_current_rents_rec(self):

        self.__srv.rent_book(3, 1)
        self.__srv.rent_book(3, 4)
        self.__srv.rent_book(3, 2)

        self.assertEqual(len(self.__srv.get_client_current_rents_rec(1, 0)), 0)
        self.assertEqual(len(self.__srv.get_client_current_rents_rec(3, 0)), 3)
        self.__srv.return_book(3, 1)
        self.assertEqual(len(self.__srv.get_client_current_rents_rec(3, 0)), 2)

        self.__srv.rent_book(1, 2)
        self.assertEqual(len(self.__srv.get_client_current_rents_rec(1, 0)), 1)
        self.__srv.return_book(1, 2)
        self.__srv.rent_book(1, 2)
        self.assertEqual(len(self.__srv.get_client_current_rents_rec(1, 0)), 1)

    def test_get_client_all_rents(self):

        self.__srv.rent_book(3, 1)
        self.__srv.rent_book(3, 4)
        self.__srv.rent_book(3, 2)

        self.assertEqual(len(self.__srv.get_client_all_rents(1)), 0)
        self.assertEqual(len(self.__srv.get_client_all_rents(3)), 3)
        self.__srv.return_book(3, 1)
        self.assertEqual(len(self.__srv.get_client_all_rents(3)), 3)

        self.__srv.rent_book(1, 2)
        self.assertEqual(len(self.__srv.get_client_current_rents(1)), 1)
        self.__srv.return_book(1, 2)
        self.__srv.rent_book(1, 3)
        self.assertEqual(len(self.__srv.get_client_all_rents(1)), 2)

    def test_get_most_rented_books(self):

        result_list1 = self.__srv.get_most_rented_books()
        self.assertEqual(len(result_list1), 0)

        self.__srv.rent_book(3, 4)
        self.__srv.rent_book(2, 4)
        self.__srv.rent_book(2, 1)
        self.__srv.rent_book(4, 1)
        self.__srv.rent_book(2, 3)
        self.__srv.rent_book(3, 3)
        self.__srv.rent_book(1, 3)

        result_list = self.__srv.get_most_rented_books()
        self.assertEqual(len(result_list), 3)
        self.assertEqual(result_list[0].get_field1(), "Institutul")
        self.assertEqual(result_list[0].get_field2(), "Stephen King")
        self.assertEqual(result_list[0].get_field3(), 3)

        self.assertEqual(result_list[1].get_field1(), "Exalare")
        self.assertEqual(result_list[1].get_field2(), "Ted Chiang")
        self.assertEqual(result_list[1].get_field3(), 2)

        self.assertEqual(result_list[2].get_field1(), "Despre Destin")
        self.assertEqual(result_list[2].get_field2(), "Andrei Plesu")
        self.assertEqual(result_list[2].get_field3(), 2)

    def test_clients_ord_by_rentsn(self):

        result_list1 = self.__srv.clients_ord_by_rentsn()
        self.assertEqual(len(result_list1), 0)

        self.__srv.rent_book(3, 4)
        self.__srv.rent_book(3, 2)
        self.__srv.rent_book(3, 0)
        self.__srv.rent_book(4, 2)
        self.__srv.rent_book(0, 2)
        self.__srv.rent_book(0, 3)

        result_list2 = self.__srv.clients_ord_by_rentsn()
        self.assertEqual(result_list2[0].get_field1(), "Petru Andrei")
        self.assertEqual(result_list2[0].get_field2(), 3)

        self.assertEqual(result_list2[1].get_field1(), "Andrei Mihailescu")
        self.assertEqual(result_list2[1].get_field2(), 2)

        self.assertEqual(result_list2[2].get_field1(), "Alexandru Afloarei")
        self.assertEqual(result_list2[2].get_field2(), 1)

        self.__srv.rent_book(0, 0)
        self.__srv.rent_book(0, 1)

        result_list3 = self.__srv.clients_ord_by_rentsn()
        self.assertEqual(result_list3[0].get_field1(), "Andrei Mihailescu")
        self.assertEqual(result_list3[0].get_field2(), 4)

    def test_clients_ord_by_name(self):

        result_list1 = self.__srv.clients_ord_by_name()
        self.assertEqual(len(result_list1), 0)

        self.__srv.rent_book(3, 1)
        self.__srv.rent_book(0, 1)
        self.__srv.rent_book(0, 2)
        self.__srv.rent_book(1, 2)
        self.__srv.rent_book(2, 3)
        self.__srv.rent_book(4, 3)
        self.__srv.rent_book(3, 0)

        result_list2 = self.__srv.clients_ord_by_name()
        self.assertEqual(result_list2[0].get_field1(), "Adrian Doroftei")
        self.assertEqual(result_list2[1].get_field1(), "Alexandru Afloarei")
        self.assertEqual(result_list2[2].get_field1(), "Andrei Mihailescu")
        self.assertEqual(result_list2[3].get_field1(), "Matei Ionescu")
        self.assertEqual(result_list2[4].get_field1(), "Petru Andrei")

        self.__srv.return_book(0, 1)
        self.__srv.return_book(0, 2)
        result_list3 = self.__srv.clients_ord_by_name()
        self.assertEqual(result_list3[2].get_field1(), "Matei Ionescu")
        self.assertEqual(result_list3[3].get_field1(), "Petru Andrei")

    def test_get_active_clients(self):

        self.__srv.rent_book(3, 2)
        self.__srv.rent_book(2, 2)
        self.__srv.rent_book(0, 2)
        self.__srv.rent_book(4, 3)
        self.__srv.rent_book(1, 3)
        self.__srv.rent_book(1, 1)
        self.__srv.rent_book(0, 3)
        self.__srv.rent_book(3, 3)
        self.__srv.rent_book(2, 0)
        self.__srv.rent_book(1, 4)
        self.__srv.rent_book(3, 4)

        list0 = self.__srv.get_active_clients(0)
        self.assertEqual(len(list0), 0)

        list1 = self.__srv.get_active_clients(10)
        self.assertEqual(len(list1), 0)

        list2 = self.__srv.get_active_clients(20)
        self.assertEqual(len(list2), 1)
        self.assertEqual(list2[0].get_field1(), "Adrian Doroftei")

        list3 = self.__srv.get_active_clients(60)
        self.assertEqual(len(list3), 3)
        self.assertEqual(list3[0].get_field1(), "Adrian Doroftei")
        self.assertEqual(list3[1].get_field1(), "Petru Andrei")
        self.assertEqual(list3[2].get_field1(), "Andrei Mihailescu")

        list4 = self.__srv.get_active_clients(100)
        self.assertEqual(len(list4), 5)
        self.assertEqual(list4[3].get_field1(), "Matei Ionescu")
        self.assertEqual(list4[4].get_field1(), "Alexandru Afloarei")

        self.assertRaises(ValueError, self.__srv.get_active_clients, 120)

    # BLACKBOX TESTING
    def test_get_most_rented_auths(self):

        self.__srv.rent_book(3, 2)
        self.__srv.rent_book(2, 2)
        self.__srv.rent_book(0, 2)
        self.__srv.rent_book(4, 3)
        self.__srv.rent_book(1, 3)
        self.__srv.rent_book(1, 1)
        self.__srv.rent_book(0, 3)
        self.__srv.rent_book(3, 3)
        self.__srv.rent_book(2, 0)
        self.__srv.rent_book(1, 4)
        self.__srv.rent_book(3, 4)

        list = self.__srv.get_most_rented_auths(0)
        self.assertEqual(len(list), 0)

        list0 = self.__srv.get_most_rented_auths(1)
        self.assertEqual(len(list0), 1)
        self.assertEqual(list0[0].get_field1(), "Stephen King")

        list1 = self.__srv.get_most_rented_auths(3)
        self.assertEqual(len(list1), 3)
        self.assertEqual(list1[0].get_field1(), "Stephen King")
        self.assertEqual(list1[1].get_field1(), "Walter Tevis")
        self.assertEqual(list1[2].get_field1(), "Ted Chiang")

        list1 = self.__srv.get_most_rented_auths(-3)
        self.assertEqual(len(list1), 3)
        self.assertEqual(list1[0].get_field1(), "Stephen King")
        self.assertEqual(list1[1].get_field1(), "Walter Tevis")
        self.assertEqual(list1[2].get_field1(), "Ted Chiang")

        list3 = self.__srv.get_most_rented_auths(5)
        self.assertEqual(len(list3), 5)
        self.assertEqual(list3[0].get_field1(), "Stephen King")
        self.assertEqual(list3[1].get_field1(), "Walter Tevis")
        self.assertEqual(list3[2].get_field1(), "Ted Chiang")
        self.assertEqual(list3[3].get_field1(), "Matt Haig")
        self.assertEqual(list3[4].get_field1(), "Andrei Plesu")

        list4 = self.__srv.get_most_rented_auths(-5)
        self.assertEqual(len(list4), 5)
        self.assertEqual(list4[0].get_field1(), "Stephen King")
        self.assertEqual(list4[1].get_field1(), "Walter Tevis")
        self.assertEqual(list4[2].get_field1(), "Ted Chiang")
        self.assertEqual(list4[3].get_field1(), "Matt Haig")
        self.assertEqual(list4[4].get_field1(), "Andrei Plesu")

        self.assertRaises(ValueError, self.__srv.get_most_rented_auths, 10000)
        self.assertRaises(ValueError, self.__srv.get_most_rented_auths, -10000)

        self.assertRaises(ValueError, self.__srv.get_most_rented_auths, 20000)
        self.assertRaises(ValueError, self.__srv.get_most_rented_auths, -20000)

    def test_clear_repo(self):

        self.__srv.clear_repo()
        self.assertTrue(self.__srv.get_all_rents() == [])
        self.assertEqual(self.__srv.get_list_size(), 0)
