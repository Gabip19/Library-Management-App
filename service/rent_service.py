from domain.bookrenter import BookRenter
from domain.datatransferobj import DataTransfer
from repository.book_repo import BookInMemoryRepository
from repository.client_repo import ClientInMemoryRepository
from repository.rent_repo import RentInMemoryRepository
from random import randint

from utils.sort_functions import Sort


class RentService:
    def __init__(self, rent_repo, client_repo, book_repo):
        """
        Initializeaza service pentru inchirieri de carti
        :param rent_repo: obiectul de tip RentRepository care ne ajuta
        sa gestionam lista cu inchirierile fiecarui client
        :type rent_repo: RentInMemoryRepository
        :param client_repo: obiectul de tip ClientRepository care ne ajuta
        sa gestionam lista cu clienti
        :type client_repo: ClientInMemoryRepository
        :param book_repo: obiectul de tip BookRepository care ne ajuta
        sa gestionam lista cu carti
        :type book_repo: BookInMemoryRepository
        """
        self.__rent_repo = rent_repo
        self.__client_repo = client_repo
        self.__book_repo = book_repo

    def rent_book(self, client_id, book_id):
        """
        Inchiriaza o carte
        :param client_id: id-ul clientului care inchiriaza cartea
        :type client_id: int
        :param book_id: id-ul cartii care se va inchiria
        :type book_id: int
        """
        client = self.__client_repo.get_client_with_id(client_id)
        book = self.__book_repo.get_book_with_id(book_id)

        rent = self.__rent_repo.contains_rent(client, book)
        if rent is None or rent.is_book_returned():
            new_client_rent = BookRenter(client, book)
            self.__rent_repo.store(new_client_rent)
        else:
            raise ValueError("Cartea respectiva se afla deja in posesia clientului.")

    def return_book(self, client_id, book_id):
        """
        Returneaza o carte
        :param client_id: id-ul clientului care returneaza cartea
        :type client_id: int
        :param book_id: id-ul cartii care se va returna
        :type book_id: int
        """
        client = self.__client_repo.get_client_with_id(client_id)
        book = self.__book_repo.get_book_with_id(book_id)

        rent = self.__rent_repo.contains_rent(client, book)
        if rent is not None and not rent.is_book_returned():
            self.__rent_repo.return_book(rent)
        else:
            raise ValueError("Cartea respectiva nu se afla in posesia clientului.")

    def get_list_size(self):
        """
        Returneaza lungimea lista cu inchirieri de carti
        :return: lungimea listei cu inchirieri
        :rtype: int
        """
        return self.__rent_repo.size()

    def get_all_rents(self):
        """
        Returneaza lista cu inchirierile cartilor
        :return: lista cu inchirieri
        :rtype: list (of BookRenter)
        """
        return self.__rent_repo.get_all_rents()

    def update_rents_for_client(self, client, updated_client):
        """
        Actualizeaza datele unui client pentru fiecare inchiriere a acestuia
        :param client: clientul pentru care se actualizeaza datele
        :type client: Client
        :param updated_client:
        :type updated_client: Client
        """
        self.__rent_repo.update_rents_for_client(client, updated_client)

    def get_client_current_rents(self, client_id):
        """
        Returneaza o lista cu toate cartile inchiriate in momentul actual de un client
        :param client_id: id-ul clientului pentru care se va returna lista cartilor inchiriate
        :type client_id: int
        :return: lista inchirierilor clientului la momentul actual
        :rtype: list (of BookRenter)
        """
        all_rents = self.__rent_repo.get_all_rents()

        client = self.__client_repo.get_client_with_id(client_id)
        client_current_rents = []

        for rent in all_rents:
            if rent.get_client() == client and not rent.is_book_returned():
                client_current_rents.append(rent)
        return client_current_rents

    def get_client_current_rents_rec(self, client_id, index):
        """
        Implementare recursiva
        Returneaza o lista cu toate cartile inchiriate in momentul actual de un client
        :param client_id: id-ul clientului pentru care se va returna lista cartilor inchiriate
        :type client_id: int
        :param index: index-ul elementului de la care va incepe cautarea (se apeleaza cu 0)
        :type index: int
        :return: lista inchirierilor clientului la momentul actual
        :rtype: list (of BookRenter)
        """
        all_rents = self.__rent_repo.get_all_rents()
        client = self.__client_repo.get_client_with_id(client_id)

        if index >= len(all_rents):
            return []
        elif all_rents[index].get_client() == client and not all_rents[index].is_book_returned():
            return [all_rents[index]] + self.get_client_current_rents_rec(client_id, index+1)
        else:
            return self.get_client_current_rents_rec(client_id, index+1)

    def get_client_all_rents(self, client_id):
        """
        Returneaza o lista cu toate cartile ce au fost sau sunt inchiriate de un client
        :param client_id: id-ul clientului pentru care se va returna lista cartilor inchiriate
        :type client_id: int
        :return: lista tuturor inchirierilor clientului
        :rtype: list (of BookRenter)
        """
        all_rents = self.__rent_repo.get_all_rents()

        client = self.__client_repo.get_client_with_id(client_id)
        client_rents = []

        for rent in all_rents:
            if rent.get_client() == client:
                client_rents.append(rent)
        return client_rents

    def get_most_rented_books(self):
        """
        Gaseste cartile cu cele mai multe inchirieri
        :return: o lista cu cartile ordonate in functie de numarul de inchirieri
        :rtype: list (of DataTransfer)
        """
        book_frec = {}
        all_rents = self.__rent_repo.get_all_rents()
        for rent in all_rents:
            book_id = rent.get_rented_book().get_id()
            if book_id in book_frec.keys():
                book_frec[book_id] += 1
            else:
                book_frec[book_id] = 1

        # sorted_list = Sort(book_frec.items(), reverse=True, cmp=cmp_two_pairs)
        sorted_list = Sort(book_frec.items(), key=lambda key: key[1], reverse=True)

        result = []
        for pair in sorted_list:
            book = self.__book_repo.get_book_with_id(pair[0])
            book_dto = DataTransfer(book.get_title(), book.get_auth(), pair[1])
            result.append(book_dto)
        return result

    def get_active_clients(self, percent):
        """
        Gaseste primi percent% dintre clientii activi
        :param percent: procentul
        :type percent: int
        :return: o lista cu primi percent% clienit activi
        :rtype: list (of DataTransfer)
        :raise: ValueError daca nu exista suficienti clienti cu carti inchiriate
        """
        percent = abs(percent)
        client_rents_numbers = {}
        client_list = self.__client_repo.get_clientlist()

        for i in range(len(client_list)):
            number_of_rents = len(self.get_client_all_rents(i))
            if number_of_rents:
                client_rents_numbers[i] = number_of_rents

        sorted_list = Sort(client_rents_numbers.items(), key=lambda key: key[1], reverse=True)

        result = []
        for pair in sorted_list:
            client = self.__client_repo.get_client_with_id(pair[0])
            client_dto = DataTransfer(client.get_name(), pair[1], None)
            result.append(client_dto)

        number_of_clients = int((self.__client_repo.size()*percent)/100)

        if len(result) >= number_of_clients:
            result = result[:number_of_clients]
            return result
        else:
            raise ValueError("Nu exista suficienti clienti cu carti inchiriate.")

    def clients_ord_by_rentsn(self):
        """
        Gaseste clientii cu cele mai multe carti inchiriate
        :return: o lista cu clientii ordonati in functie de numarul de carti inchiriate
        :rtype: list (of DataTransfer)
        """
        client_rents_numbers = {}
        client_list = self.__client_repo.get_clientlist()

        for i in range(len(client_list)):
            number_of_rents = len(self.get_client_current_rents_rec(i, 0))
            if number_of_rents:
                client_rents_numbers[i] = number_of_rents

        sorted_list = Sort(client_rents_numbers.items(), key=lambda key: key[1], reverse=True)
        # sorted_list = Sort(client_rents_numbers.items(), reverse=True, cmp=self.cmp_two_pairs1)

        result = []
        for pair in sorted_list:
            client = self.__client_repo.get_client_with_id(pair[0])
            client_dto = DataTransfer(client.get_name(), pair[1], None)
            result.append(client_dto)
        return result

    def clients_ord_by_name(self):
        """
        Gaseste clientii cu cele mai multe carti inchiriate
        :return: o lista cu clientii cu carti inchiriate ordonati dupa nume
        :rtype: list (of DataTransfer)
        """
        list_of_els = []
        client_list = self.__client_repo.get_clientlist()
        for i in range(len(client_list)):
            number_of_rents = len(self.get_client_current_rents_rec(i, 0))
            if number_of_rents:
                el_to_add = (self.__client_repo.get_client_with_id(i).get_name(), number_of_rents)
                list_of_els.append(el_to_add)

        sorted_list = Sort(list_of_els, key=lambda key: key[0])

        result = []
        for el in sorted_list:
            client_dto = DataTransfer(el[0], el[1], None)
            result.append(client_dto)
        return result

    def generate_random_rents(self, number_of_entities):
        """
        Genereaza rent-uri aleatoriu
        :param number_of_entities: numarul de rent-uri ce vor fi generate
        :type number_of_entities: int
        """
        client_list_size = self.__client_repo.size()
        book_list_size = self.__book_repo.size()
        for i in range(number_of_entities):
            client_id = randint(0, client_list_size-1)
            client = self.__client_repo.get_client_with_id(client_id)

            book_id = randint(0, book_list_size-1)
            book = self.__book_repo.get_book_with_id(book_id)

            new_rent = BookRenter(client, book)
            if new_rent not in self.__rent_repo.get_all_rents():
                self.rent_book(client_id, book_id)

    def get_most_rented_auths(self, n):
        """
        Returneaza primii n cei mai inchiriati autori
        :param n: numarul autorilor cu cele mai inchiriate carti ce se va returna
        :type n: int
        :return: primii n autori a caror carti sunt cele mai inchiriate
        :rtype: list (of DataTransfer cu numele autorului si numarul total al cartilor inchiriate)
        :raise: ValueError daca nu exista suficient autori cu carti inchiriate
        """
        n = abs(n)
        auth_list = []
        for book in self.__book_repo.get_booklist():
            if book.get_auth() not in auth_list:
                auth_list.append(book.get_auth())

        list_of_els = []
        for auth in auth_list:
            count = 0
            for rent in self.__rent_repo.get_all_rents():
                if rent.get_rented_book().get_auth() == auth:
                    count += 1
            if count:
                list_of_els.append((auth, count))

        sorted_list = Sort(list_of_els, reverse=True, cmp=cmp_two_pairs)
        # sorted_list = Sort(list_of_els, key=lambda key: key[1], reverse=True)

        if len(sorted_list) >= n:
            sorted_list = sorted_list[:n]
            result = []
            for pair in sorted_list:
                auth_dto = DataTransfer(pair[0], pair[1], None)
                result.append(auth_dto)
            return result
        else:
            raise ValueError("Nu exista suficienti autori cu carti inchiriate.")

    def clear_repo(self):
        self.__rent_repo.delete_all()



def cmp_two_pairs(item1, item2):
    if item1[1] > item2[1]:
        return True
    elif item1[1] == item2[1]:
        if item1[0] <= item2[0]:
            return True
        else:
            return False
    else:
        return False
