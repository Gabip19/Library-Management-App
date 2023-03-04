from domain.entities import Client
from domain.validators import ClientValidator
from repository.client_repo import ClientInMemoryRepository
from random import randint

from utils.rand_functions import randomword, randomcnp


class ClientService:
    def __init__(self, repo, validator):
        """
        Initializeaza service pentru clienti
        :param repo: obiectul de tip ClientRepository care ne ajuta sa gestionam
        lista de clienti a bibliotecii
        :type repo: ClientInMemoryRepository
        :param validator: validator pentru verificarea clientilor
        :type validator: ClientValidator
        """
        self.__repo = repo
        self.__client_val = validator

    def add_client(self, name, CNP):
        """
        Adaugare client la lista
        :param name: numele clientului
        :type name: str
        :param CNP: CNP-ul clientului
        :type CNP: str
        :raise ValueError daca datele clientului nu sunt valide
               ValueError daca respectivul client exista deja in lista
        """
        new_client = Client(self.__repo.size(), name, CNP)
        client_list = self.__repo.get_clientlist()
        if new_client in client_list:
            raise ValueError("Clientul respectiv exista deja in lista de clienti.")
        self.__client_val.validate(new_client)
        self.__repo.store(new_client)

        return new_client

    def update_client(self, id, name, CNP):
        """
        Actualizeaza datele unui client
        :param id: ID-ul clientului ce va fi modificata
        :type id: int
        :param name: noul nume al clientului
        :type name: str
        :param CNP: noul CNP al clientului
        :type CNP: str
        :raise ValueError daca datele clientului nu sunt valide
        """
        client_list = self.__repo.get_clientlist()
        updated_client = Client(id, name, CNP)
        self.__client_val.validate(updated_client)
        if updated_client not in client_list:
            client_list[id] = updated_client
        else:
            raise ValueError("Datele introduse corespund unui client deja existent in lista.")
        return updated_client

    def delete_client(self, name, CNP):
        """
        Sterge un client din lista
        :param name: numele clientului ce va fi sters
        :type name: str
        :param CNP: CNP-ul clientului ce va fi sters
        :type CNP: str
        :raise ValueError daca respectivul client nu exista in lista de clienti
        """
        client_to_delete = Client(0, name, CNP)
        for client in self.__repo.get_clientlist():
            if client_to_delete == client:
                self.__repo.delete_client(client)
                return client.get_id()
        else:
            raise ValueError("Clientul respectiv nu exista in lista de clienti.")

    def get_all_clients(self):
        """
        Returneaza lista cu toti clientii bibliotecii
        :return: lista de clienti
        :rtype: list (of Client)
        """
        return self.__repo.get_clientlist()

    def get_list_size(self):
        """
        Returneaza lungimea liste de clienti
        :return: lungimea listei de clienti a bibliotecii
        :rtype: int
        """
        return self.__repo.size()

    def search_client(self, name, CNP):
        """
        Verifica daca un client se afla in lista de clienti
        :param name: Numele clientului ce se va cauta in lista
        :type name: str
        :param CNP: CNP-ul clientului ce se va cauta in lista
        :type CNP: str
        :return: id-ul clientului daca clientul dat se afla in lista
                 -1 altfel
        :rtype: int
        """
        client_to_search = Client(0, name, CNP)
        self.__client_val.validate(client_to_search)
        return self.__repo.is_client_in_list(client_to_search)

    def get_client_with_id(self, id):
        """
        Returneaza clientul din lista de clienti care are id-ul egal cu cel dat
        :param id: id-ul clientului care se va returna
        :type id: int
        :return: clientul care are id-ul introdus
        :rtype: Client
        """
        # client = self.__repo.get_client_with_id(id)
        client = self.__repo.get_client_with_id_rec(id, 0)
        return client

    def generate_random_clients(self, number_of_entities):
        """
        Genereaza clienti aleatoriu
        :param number_of_entities: numarul de clienti ce vor fi generati
        :type number_of_entities: int
        """
        for i in range(number_of_entities):
            # Genereaza prenumele
            first_name_len = randint(3, 10)
            first_name = randomword(first_name_len)
            first_name = first_name.capitalize()

            # Genereaza numele
            last_name_len = randint(3, 12)
            last_name = randomword(last_name_len)
            last_name = last_name.capitalize()

            # Creeaza numele complet
            name_as_list = [first_name, last_name]
            name = ' '.join(name_as_list)

            # Genereaza CNP
            CNP = randomcnp()

            # Adauga clientul generat in lista de clienti
            self.add_client(name, CNP)

    def clear_repo(self):
        """
        Sterge toate cartile din lista
        """
        self.__repo.delete_all()
