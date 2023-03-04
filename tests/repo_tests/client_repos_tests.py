import unittest
from domain.entities import Client
from repository.client_repo import ClientInMemoryRepository, ClientFileRepository


class TestCaseClientMemoryRepo(unittest.TestCase):

    def setUp(self) -> None:
        self.__repo = ClientInMemoryRepository()

        self.__repo.store(Client(0, "Andrei Mihailescu", "5001215570016"))
        self.__repo.store(Client(1, "Adrian Doroftei", "1275728387234"))
        self.__repo.store(Client(2, "Matei Ionescu", "4742818172447"))
        self.__repo.store(Client(3, "Petru Andrei", "3827582189822"))
        self.__repo.store(Client(4, "Alexandru Afloarei", "2498589238356"))

    def tearDown(self) -> None:
        self.__repo.delete_all()

    def test_store_client(self):

        c1 = Client(23, "Client 1", "1234567890123")
        self.__repo.store(c1)
        self.assertEqual(len(self.__repo.get_clientlist()), 6)

        c2 = Client(14, "Client 2", "1234432123211")
        self.__repo.store(c2)
        self.assertEqual(len(self.__repo.get_clientlist()), 7)

    def test_get_all_clients(self):

        clientlist = self.__repo.get_clientlist()
        self.assertEqual(len(clientlist), 5)

        self.__repo.store(Client(6, "Nume 1", "1234123412341"))
        self.__repo.store(Client(7, "Nume 2", "4234112344341"))

        clientlist = self.__repo.get_clientlist()
        self.assertEqual(len(clientlist), 7)

        self.__repo.store(Client(8, "Nume 3", "6437281687112"))
        self.__repo.store(Client(9, "Nume 4", "6437812574651"))

        clientlist = self.__repo.get_clientlist()
        self.assertEqual(len(clientlist), 9)

    def test_delete_client(self):

        c1 = Client(5, "Client 1", "1234567890123")
        self.__repo.store(c1)
        c2 = Client(6, "Client 2", "1234783212323")
        self.__repo.store(c2)
        c3 = Client(7, "Client 3", "7321781782311")
        self.__repo.store(c3)
        c4 = Client(8, "Client 4", "5123212382815")
        self.__repo.store(c4)
        c5 = Client(9, "Client 5", "7421852895829")
        self.__repo.store(c5)

        self.__repo.delete_client(c3)
        self.assertEqual(c5.get_id(), 8)
        self.assertEqual(len(self.__repo.get_clientlist()), 9)

        self.__repo.delete_client(c1)
        self.assertEqual(c5.get_id(), 7)
        self.assertEqual(len(self.__repo.get_clientlist()), 8)

    def test_is_client_in_list(self):

        c1 = Client(0, "Andrei Mihailescu", "5001215570016")
        self.assertTrue(self.__repo.is_client_in_list(c1) >= 0)

        c2 = Client(0, "Adrian Doroftei", "1275728387234")
        self.assertTrue(self.__repo.is_client_in_list(c2) >= 0)

        c3 = Client(0, "Adrian D.", "1275728387234")
        self.assertTrue(self.__repo.is_client_in_list(c3) == -1)

        c4 = Client(0, "Adrian Doroftei", "1275728387521")
        self.assertTrue(self.__repo.is_client_in_list(c4) == -1)

        c5 = Client(0, "Client", "1234567890123")
        self.assertTrue(self.__repo.is_client_in_list(c5) == -1)

    def test_get_client_with_id(self):

        client1 = self.__repo.get_client_with_id(3)
        self.assertTrue(client1.get_id() == 3)
        self.assertTrue(client1.get_name() == "Petru Andrei")
        self.assertTrue(client1.get_CNP() == "3827582189822")

        client2 = self.__repo.get_client_with_id(0)
        self.assertTrue(client2.get_id() == 0)
        self.assertTrue(client2.get_name() == "Andrei Mihailescu")
        self.assertTrue(client2.get_CNP() == "5001215570016")

        client3 = self.__repo.get_client_with_id(4)
        self.assertTrue(client3.get_id() == 4)
        self.assertTrue(client3.get_name() == "Alexandru Afloarei")
        self.assertTrue(client3.get_CNP() == "2498589238356")

    def test_get_client_with_id_rec(self):

        client1 = self.__repo.get_client_with_id_rec(3, 0)
        self.assertTrue(client1.get_id() == 3)
        self.assertTrue(client1.get_name() == "Petru Andrei")
        self.assertTrue(client1.get_CNP() == "3827582189822")

        client2 = self.__repo.get_client_with_id_rec(0, 0)
        self.assertTrue(client2.get_id() == 0)
        self.assertTrue(client2.get_name() == "Andrei Mihailescu")
        self.assertTrue(client2.get_CNP() == "5001215570016")

        client3 = self.__repo.get_client_with_id_rec(4, 0)
        self.assertTrue(client3.get_id() == 4)
        self.assertTrue(client3.get_name() == "Alexandru Afloarei")
        self.assertTrue(client3.get_CNP() == "2498589238356")

    def test_delete_all(self):

        self.__repo.delete_all()
        self.assertTrue(self.__repo.get_clientlist() == [])
        self.assertEqual(self.__repo.size(), 0)



class TestCaseClientFileRepo(unittest.TestCase):

    def setUp(self) -> None:
        self.__repo = ClientFileRepository("test_client_repo.txt")
        self.__repo.delete_all()

        self.__repo.store(Client(0, "Andrei Mihailescu", "5001215570016"))
        self.__repo.store(Client(1, "Adrian Doroftei", "1275728387234"))
        self.__repo.store(Client(2, "Matei Ionescu", "4742818172447"))
        self.__repo.store(Client(3, "Petru Andrei", "3827582189822"))
        self.__repo.store(Client(4, "Alexandru Afloarei", "2498589238356"))

    def tearDown(self) -> None:
        self.__repo.delete_all()

    def test_store_client(self):

        c1 = Client(23, "Client 1", "1234567890123")
        self.__repo.store(c1)
        self.assertEqual(len(self.__repo.get_clientlist()), 6)

        c2 = Client(14, "Client 2", "1234432123211")
        self.__repo.store(c2)
        self.assertEqual(len(self.__repo.get_clientlist()), 7)

    def test_get_all_clients(self):

        clientlist = self.__repo.get_clientlist()
        self.assertEqual(len(clientlist), 5)

        self.__repo.store(Client(6, "Nume 1", "1234123412341"))
        self.__repo.store(Client(7, "Nume 2", "4234112344341"))

        clientlist = self.__repo.get_clientlist()
        self.assertEqual(len(clientlist), 7)

        self.__repo.store(Client(8, "Nume 3", "6437281687112"))
        self.__repo.store(Client(9, "Nume 4", "6437812574651"))

        clientlist = self.__repo.get_clientlist()
        self.assertEqual(len(clientlist), 9)

    def test_delete_client(self):

        c1 = Client(5, "Client 1", "1234567890123")
        self.__repo.store(c1)
        c2 = Client(6, "Client 2", "1234783212323")
        self.__repo.store(c2)
        c3 = Client(7, "Client 3", "7321781782311")
        self.__repo.store(c3)
        c4 = Client(8, "Client 4", "5123212382815")
        self.__repo.store(c4)
        c5 = Client(9, "Client 5", "7421852895829")
        self.__repo.store(c5)

        self.__repo.delete_client(c3)
        self.assertEqual(c5.get_id(), 8)
        self.assertEqual(len(self.__repo.get_clientlist()), 9)

        self.__repo.delete_client(c1)
        self.assertEqual(c5.get_id(), 7)
        self.assertEqual(len(self.__repo.get_clientlist()), 8)

    def test_is_client_in_list(self):

        c1 = Client(0, "Andrei Mihailescu", "5001215570016")
        self.assertTrue(self.__repo.is_client_in_list(c1) >= 0)

        c2 = Client(0, "Adrian Doroftei", "1275728387234")
        self.assertTrue(self.__repo.is_client_in_list(c2) >= 0)

        c3 = Client(0, "Adrian D.", "1275728387234")
        self.assertTrue(self.__repo.is_client_in_list(c3) == -1)

        c4 = Client(0, "Adrian Doroftei", "1275728387521")
        self.assertTrue(self.__repo.is_client_in_list(c4) == -1)

        c5 = Client(0, "Client", "1234567890123")
        self.assertTrue(self.__repo.is_client_in_list(c5) == -1)

    def test_get_client_with_id(self):

        client1 = self.__repo.get_client_with_id(3)
        self.assertTrue(client1.get_id() == 3)
        self.assertTrue(client1.get_name() == "Petru Andrei")
        self.assertTrue(client1.get_CNP() == "3827582189822")

        client2 = self.__repo.get_client_with_id(0)
        self.assertTrue(client2.get_id() == 0)
        self.assertTrue(client2.get_name() == "Andrei Mihailescu")
        self.assertTrue(client2.get_CNP() == "5001215570016")

        client3 = self.__repo.get_client_with_id(4)
        self.assertTrue(client3.get_id() == 4)
        self.assertTrue(client3.get_name() == "Alexandru Afloarei")
        self.assertTrue(client3.get_CNP() == "2498589238356")

    def test_delete_all(self):

        self.__repo.delete_all()
        self.assertTrue(self.__repo.get_clientlist() == [])
        self.assertEqual(self.__repo.size(), 0)
