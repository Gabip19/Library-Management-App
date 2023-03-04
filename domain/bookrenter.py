from domain.entities import Book
from domain.entities import Client


class BookRenter:
    def __init__(self, client, book_to_rent):
        """
        Creeaza un obiect care memoreaza o inchiriere a unei carti de catre un client
        :param client: clientul care inchiriaza cartea
        :type client: Client
        :param book_to_rent: cartea care se inchiriaza
        :type book_to_rent: Book
        """
        self.__client = client
        self.__rented_book = book_to_rent
        self.__is_book_returned = False

    def get_client(self):
        return self.__client

    def get_rented_book(self):
        return self.__rented_book

    def is_book_returned(self):
        """
        Returneaza statusul unei inchirieri
        :return: statusul inchirierii
        :rtype: bool
                True - daca respectiva cartea a fost returnata
                False - daca respectiva carte se afla inca in posesia clientului
        """
        return self.__is_book_returned

    def return_book(self):
        """
        Seteaza valoarea lui __is_book_returned cu True daca
        a fost returnata cartea corespunzatoare inchirierii
        """
        self.__is_book_returned = True

    def set_client(self, value):
        self.__client = value

    def __eq__(self, other):
        """
        Defineste conceptul de egalitate a doua carti
        :param other: BookRenter-ul cu care se compara
        :type other: BookRenter
        :return: True daca cele doua rentere sunt identice (au acelasi client si aceeasi carte inchiriata)
                 False altfel
        :rtype: bool
        """
        if self.__client == other.get_client() and self.__rented_book == other.get_rented_book():
            return True
        else:
            return False

    def __str__(self):
        return "Client: " + str(self.__client) + "\n" + "Carte: " + str(self.__rented_book) + "\nReturnata: " \
               + str(self.__is_book_returned)
