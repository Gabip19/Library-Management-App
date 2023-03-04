from domain.bookrenter import BookRenter
from domain.entities import Book, Client


class RentInMemoryRepository:
    """
    Clasa creata cu responsabilitatea de a gestiona
    multimea inchirierilor de carti
    """
    def __init__(self):
        self.__rent_list = []

    def store(self, client_rent):
        """
        Adauga rentul unui client in lista de rents
        :param client_rent: rentul clientului de adaugat
        :type client_rent: BookRenter
        """
        self.__rent_list.append(client_rent)

    def get_all_rents(self):
        """
        Returneaza lista cu toate renturile
        :return: lista de renturi
        :rtype: list (of BookRenters)
        """
        return self.__rent_list

    def size(self):
        """
        Returneaza numarul renturi din lista renturilor
        :return: lungimea listei de renturi
        :rtype: int
        """
        return len(self.__rent_list)

    def contains_rent(self, client, book):
        """
        Verifica daca un client dat a inchiriat vreodata o carte data
        :param client: clientul pentru care se verifica
        :type client: Client
        :param book: cartea pentru care se verifica
        :type book: Book
        :return: Obiectul de tip BookRenter daca acesta exista in lista
                 None in caz contrar
        :rtype: BookRenter
        """
        rent_list = self.get_all_rents()
        for rent in reversed(rent_list):
            if rent.get_client() == client and rent.get_rented_book() == book:
                return rent
        return None

    def update_rents_for_client(self, client, updated_client):
        """
        Actualizeaza datele unui client pentru fiecare inchiriere a acestuia
        :param client: clientul pentru care se actualizeaza datele
        :type client: Client
        :param updated_client:
        :type updated_client: Client
        """
        for rent in self.get_all_rents():
            if rent.get_client() == client:
                rent.set_client(updated_client)

    def return_book(self, rent):
        """
        Returneaza o carte asociata unui rent
        :param rent: rent-ul pentru care se returneaza cartea
        :type rent: BookRenter
        """
        rent.return_book()

    def delete_all(self):
        """
        Sterge toate inchirierile din lista
        """
        self.__rent_list = []



class RentFileRepository(RentInMemoryRepository):
    """
    Clasa creata cu responsabilitatea de a gestiona
    multimea de inchirieri a bibliotecii
    """
    def __init__(self, filename):
        RentInMemoryRepository.__init__(self)
        self.__file_name = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Incarca cartile din fisier in lista
        """
        try:
            f = open(self.__file_name, "r")
        except IOError:
            raise IOError("Fisierul dat nu a putut fi deschis.")

        lines = f.readlines()
        for line in lines:
            client_id, client_name, client_cnp, book_id, book_title, book_auth, status = \
                [token.strip() for token in line.split(";")]
            client = Client(client_id, client_name, client_cnp)
            book = Book(book_id, book_title, "", book_auth)
            rent = BookRenter(client, book)
            if status == "True":
                rent.return_book()
            RentInMemoryRepository.store(self, rent)
        f.close()

    def __save_to_file(self):
        """
        Salveaza lista de carti in fisier
        """
        all_rents = RentInMemoryRepository.get_all_rents(self)
        with open(self.__file_name, 'w') as rent_file:
            for rent in all_rents:
                rent_string = str(rent.get_client().get_id()) + ';' + str(rent.get_client().get_name()) + ';' \
                              + str(rent.get_client().get_CNP()) + ';' + str(rent.get_rented_book().get_id()) + ';' \
                              + str(rent.get_rented_book().get_title()) + ";" + str(rent.get_rented_book().get_auth()) \
                              + ";" + str(rent.is_book_returned()) + '\n'
                rent_file.write(rent_string)

    def store(self, rent):
        """
        Adauga rentul unui client in lista de rents
        :param rent: rentul clientului de adaugat
        :type rent: BookRenter
        """
        RentInMemoryRepository.store(self, rent)
        self.__save_to_file()

    def get_all_rents(self):
        """
        Returneaza lista cu toate renturile
        :return: lista de renturi
        :rtype: list (of BookRenters)
        """
        return RentInMemoryRepository.get_all_rents(self)

    def size(self):
        """
        Returneaza numarul renturi din lista renturilor
        :return: lungimea listei de renturi
        :rtype: int
        """
        return RentInMemoryRepository.size(self)

    def contains_rent(self, client, book):
        """
        Verifica daca un client dat a inchiriat vreodata o carte data
        :param client: clientul pentru care se verifica
        :type client: Client
        :param book: cartea pentru care se verifica
        :type book: Book
        :return: Obiectul de tip BookRenter daca acesta exista in lista
                 None in caz contrar
        :rtype: BookRenter
        """
        return RentInMemoryRepository.contains_rent(self, client, book)

    def return_book(self, rent):
        """
        Returneaza o carte asociata unui rent
        :param rent: rent-ul pentru care se returneaza cartea
        :type rent: BookRenter
        """
        RentInMemoryRepository.return_book(self, rent)
        self.__save_to_file()

    def update_rents_for_client(self, client, updated_client):
        """
        Actualizeaza datele unui client pentru fiecare inchiriere a acestuia
        :param client: clientul pentru care se actualizeaza datele
        :type client: Client
        :param updated_client:
        :type updated_client: Client
        """
        RentInMemoryRepository.update_rents_for_client(self, client, updated_client)
        self.__save_to_file()

    def delete_all(self):
        """
        Sterge toate inchirierile din lista
        """
        RentInMemoryRepository.delete_all(self)
        self.__save_to_file()
