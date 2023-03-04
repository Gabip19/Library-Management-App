import unittest
from domain.validators import ClientValidator
from repository.client_repo import ClientInMemoryRepository
from service.client_service import ClientService


class TestCaseClientService(unittest.TestCase):

    def setUp(self) -> None:
        repo = ClientInMemoryRepository()
        validator = ClientValidator()
        self.__srv = ClientService(repo, validator)

        self.__srv.add_client("Andrei Mihailescu", "5001215570016")
        self.__srv.add_client("Adrian Doroftei", "1275728387234")
        self.__srv.add_client("Matei Ionescu", "4742818172447")
        self.__srv.add_client("Petru Andrei", "3827582189822")
        self.__srv.add_client("Alexandru Afloarei", "2498589238356")

    def tearDown(self) -> None:
        self.__srv.clear_repo()

    def test_add_client(self):

        new_client1 = self.__srv.add_client("Client 1", "1234567890123")
        self.assertTrue(new_client1.get_name() == "Client 1")
        self.assertTrue(new_client1.get_CNP() == "1234567890123")
        self.assertTrue(new_client1.get_id() == 5)
        self.assertEqual(len(self.__srv.get_all_clients()), 6)

        new_client2 = self.__srv.add_client("Client 2", "4521521232134")
        self.assertTrue(new_client2.get_name() == "Client 2")
        self.assertTrue(new_client2.get_CNP() == "4521521232134")
        self.assertTrue(new_client2.get_id() == 6)
        self.assertEqual(len(self.__srv.get_all_clients()), 7)

        self.assertRaises(ValueError, self.__srv.add_client, "Nume", "1234567890123")

        self.assertRaises(ValueError, self.__srv.add_client, "Nume 4", "12345678901")

        self.assertRaises(ValueError, self.__srv.add_client, "Nume", "123456fdsa324")

        self.assertRaises(ValueError, self.__srv.add_client, "Client 1", "1234567890123")

    def test_get_all_clients(self):

        self.assertEqual(len(self.__srv.get_all_clients()), 5)

        self.__srv.add_client("Nume 1", "1234567890123")
        self.__srv.add_client("Nume 2", "1525712736562")

        self.assertEqual(len(self.__srv.get_all_clients()), 7)

        self.__srv.add_client("Nume 3", "1234567890125")
        self.__srv.add_client("Nume 4", "1525712736566")

        self.assertEqual(len(self.__srv.get_all_clients()), 9)

    def test_update_client(self):

        client_list = self.__srv.get_all_clients()

        self.__srv.update_client(3, "Nume nou", "1234567890123")
        self.assertEqual(client_list[3].get_name(), "Nume nou")
        self.assertEqual(client_list[3].get_CNP(), "1234567890123")

        self.__srv.update_client(4, "Nume nou 1", "7532659212843")
        self.assertEqual(client_list[4].get_name(), "Nume nou 1")
        self.assertEqual(client_list[4].get_CNP(), "7532659212843")

        self.assertRaises(ValueError, self.__srv.update_client, 3, "Nume nou", "1234567890")

        self.assertRaises(ValueError, self.__srv.update_client, 3, "Nume nou", "1sffa567890as")

        self.assertRaises(ValueError, self.__srv.update_client, 3, "Nume", "1234567890123")

        self.assertRaises(ValueError, self.__srv.update_client, 4, "Nume nou 1", "7532659212843")

    def test_delete_client(self):

        self.__srv.add_client("Nume 1", "1234567890123")
        self.__srv.add_client("Nume 2", "5321235123123")
        self.__srv.add_client("Nume 3", "5637261873622")
        self.__srv.add_client("Nume 4", "5647328672837")
        self.__srv.add_client("Nume 5", "8591720566765")
        self.__srv.add_client("Nume 6", "1273737218496")

        self.__srv.delete_client("Nume 3", "5637261873622")
        self.assertEqual(len(self.__srv.get_all_clients()), 10)

        self.__srv.delete_client("Nume 5", "8591720566765")
        self.assertEqual(len(self.__srv.get_all_clients()), 9)

        self.assertRaises(ValueError, self.__srv.delete_client, "Nume 7", "6427161721231")

        self.assertRaises(ValueError, self.__srv.delete_client, "Nume 2", "5321235123126")

    def test_search_client(self):

        self.assertTrue(self.__srv.search_client("Andrei Mihailescu", "5001215570016") >= 0)
        self.assertTrue(self.__srv.search_client("Adrian Doroftei", "1275728387234") >= 0)
        self.assertTrue(self.__srv.search_client("Adrian D.", "1275728387234") == -1)
        self.assertTrue(self.__srv.search_client("Adrian Doroftei", "1275728387521") == -1)
        self.assertTrue(self.__srv.search_client("Client 2", "1234567890123") == -1)

    def test_get_client_with_id(self):

        client1 = self.__srv.get_client_with_id(1)
        self.assertEqual(client1.get_id(), 1)
        self.assertEqual(client1.get_name(), "Adrian Doroftei")
        self.assertEqual(client1.get_CNP(), "1275728387234")

        client2 = self.__srv.get_client_with_id(4)
        self.assertEqual(client2.get_id(), 4)
        self.assertEqual(client2.get_name(), "Alexandru Afloarei")
        self.assertEqual(client2.get_CNP(), "2498589238356")

        client3 = self.__srv.get_client_with_id(0)
        self.assertEqual(client3.get_id(), 0)
        self.assertEqual(client3.get_name(), "Andrei Mihailescu")
        self.assertEqual(client3.get_CNP(), "5001215570016")

    def test_clear_repo(self):

        self.__srv.clear_repo()
        self.assertTrue(self.__srv.get_all_clients() == [])
        self.assertEqual(self.__srv.get_list_size(), 0)
