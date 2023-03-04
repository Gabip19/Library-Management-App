from domain.entities import Book
from domain.validators import BookValidator
from repository.book_repo import BookInMemoryRepository


class BookService:
    def __init__(self, repo, validator):
        """
        Initializeaza service pentru carti
        :param repo: obiectul de tip BookRepository care ne ajuta sa gestionam
        lista de carti a bibliotecii
        :type repo: BookInMemoryRepository
        :param validator: validator pentru verificarea cartilor
        :type validator: BookValidator
        """
        self.__repo = repo
        self.__book_val = validator

    def add_book(self, title, desc, auth):
        """
        Adaugare carte la lista
        :param title: titlul cartii
        :type title: str
        :param desc: descrierea cartii
        :type desc: str
        :param auth: autorul cartii
        :type auth: str
        :raise ValueError daca datele cartii nu sunt valide
               ValueError daca respectiva carte exista deja in lista
        """
        new_book = Book(self.__repo.size(), title, desc, auth)
        book_list = self.__repo.get_booklist()
        if new_book in book_list:
            raise ValueError("Cartea respectiva exista deja in lista de carti.")
        self.__book_val.validate(new_book)
        self.__repo.store(new_book)

        return new_book

    def update_book(self, id, title, desc, auth):
        """
        Actualizeaza datele unei carti
        :param id: ID-ul cartii ce va fi modificata
        :type id: int
        :param title: noul titlu al cartii
        :type title: str
        :param desc: noua descriere a cartii
        :type desc: str
        :param auth: noul autor al cartii
        :type auth: str
        :raise ValueError daca noile date ale cartii nu sunt valide
        """
        book_list = self.__repo.get_booklist()
        updated_book = Book(id, title, desc, auth)
        self.__book_val.validate(updated_book)
        if updated_book not in book_list:
            self.__repo.update_book(id, updated_book)
        else:
            raise ValueError("Datele introduse corespund unei carti deja existente in lista.")

    def delete_book(self, title, auth):
        """
        Sterge o carte din lista
        :param title: titlul cartii ce va fi stearsa
        :type title: str
        :param auth: autorul cartii ce va fi stearsa
        :type auth: str
        :raise ValueError daca respectiva carte nu exista in lista de carti
        """
        book_to_delete = Book(0, title, '', auth)
        if book_to_delete in self.__repo.get_booklist():
            self.__repo.delete_book(book_to_delete)
        else:
            raise ValueError("Cartea respectiva nu exista in lista de carti.")

    def get_all_books(self):
        """
        Returneaza lista cu toate cartile din biblioteca
        :return: lista de carti
        :rtype: list (of Book)
        """
        return self.__repo.get_booklist()

    def get_list_size(self):
        """
        Returneaza lungimea liste de carti
        :return: lungimea listei de carti a bibliotecii
        :rtype: int
        """
        return self.__repo.size()

    def get_book_with_id(self, id):
        """
        Returneaza cartea din lista de carti ce are id-ul egal cu cel dat
        :param id: id-ul cartii care se va returna
        :type id: int
        :return: cartea care are id-ul introdus
        :rtype: Book
        """
        return self.__repo.get_book_with_id(id)

    def search_in_titles(self, seq_to_search):
        """
        Cauta in titlurile cartilor o secventa introdusa de utilizator
        :param seq_to_search: secventa ce se va cauta in titluri
        :type seq_to_search: str
        :return: o lista formata din cartile a caror titluri contin secventa data
        :rtype: list (of Book)
        """
        filtered_list = []
        for book in self.__repo.get_booklist():
            if seq_to_search.lower() in book.get_title().lower():
                filtered_list.append(book)
        return filtered_list

    def clear_repo(self):
        """
        Sterge toate cartile din lista
        """
        self.__repo.delete_all()
