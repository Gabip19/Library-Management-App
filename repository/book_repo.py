from domain.entities import Book


class BookInMemoryRepository:
    """
    Clasa creata cu responsabilitatea de a gestiona
    multimea de carti de la biblioteca
    """
    def __init__(self):
        # Multimea de carti: bookslist
        self.__booklist = []
        self.__populate_list(False)

    def store(self, book):
        """
        Adauga o carte in lista de carti
        :param book: cartea de adaugat
        :type book: Book
        """
        self.__booklist.append(book)

    def get_booklist(self):
        """
        Returneaza lista cu toate cartile disponibile in biblioteca
        :return: lista de carti
        :rtype: list (of Book)
        """
        return self.__booklist

    def size(self):
        """
        Returneaza numarul de carti din lista corespunzatoare bibliotecii
        :return: lungimea listei de carti
        :rtype: int
        """
        return len(self.__booklist)

    def update_book(self, id, updated_book):
        """
        Actualizeaza datele unei carti
        :param id: ID-ul cartii ce va fi modificata
        :type id: int
        :param updated_book: noua carte
        :type updated_book: Book
        """
        self.__booklist[id] = updated_book

    def delete_book(self, book):
        """
        Sterge din lista de carti a bibliotecii o carte data
        :param book: cartea care se va sterge
        :type book: Book
        """
        self.__booklist.remove(book)
        for i, el_book in enumerate(self.__booklist):
            el_book.set_id(i)

    def get_book_with_id(self, id):
        """
        Returneaza cartea din lista de carti ce are id-ul egal cu cel dat
        :param id: id-ul cartii care se va returna
        :type id: int
        :return: cartea care are id-ul introdus
        :rtype: Book
        """
        for book in self.__booklist:
            if id == book.get_id():
                return book

    def delete_all(self):
        """
        Sterge toate cartile din lista
        """
        self.__booklist = []

    def __populate_list(self, var):
        """
        Populeaza lista de carti a bibliotecii cu cateva carti predefinite
        :param var: deicede daca lista de carti va fi populata sau nu
        :type var: bool
        """
        if var:
            new_book = Book(
                0, "Biblioteca de la miezul noptii",
                "C????tig??toare a Goodreads Choice Awards ??n 2020 "
                "pentru cea mai bun?? carte de fic??iune, Biblioteca "
                "de la Miezul Nop??ii  te poart?? ??ntr-o c??l??torie "
                "magic?? printre regrete, c??r??i, universuri paralele, "
                "speran??e ??i o nou?? ??ans??.",
                "Matt Haig"
            )
            self.store(new_book)
            new_book = Book(
                1, "Despre Destin",
                "Despre destin este un roman epistolar alc??tuit din zece scrisori ??ntre Gabriel "
                "Liiceanu ??i Andrei Ple??u pe tema destinului ??i urzeala sor??ii.",
                "Andrei Plesu"
            )
            self.store(new_book)
            new_book = Book(
                2, "Gambitul Damei",
                "Gambitul Damei este povestea lui Beth Harmon care, r??mas?? orfan?? la "
                "v??rsta de opt ani trece prin numeroase ??nt??mpl??ri ??i momente "
                "dificile ??ncerc??nd s??-??i construiasc?? propriul drum ??i s?? devin?? "
                "campioan?? ??ntr-un joc dominat de b??rba??i ??? ??ahul.",
                "Walter Tevis"
            )
            self.store(new_book)
            new_book = Book(
                3, "Institutul",
                "Institutul ??mbin?? supranaturalul cu lumea proiectelor guvernamentale "
                "secrete ??i a teoriilor conspira??iei ??ntr-un thriller care te ??ine cu "
                "sufletul la gur??.",
                "Stephen King"
            )
            self.store(new_book)
            new_book = Book(
                4, "Exalare",
                "Printre cele mai citite c??r??i SF din 2020, Exalare vorbe??te despre cum ar "
                "ar??ta o lume cu acces la universurile ei paralele ??i te ??ndeamn?? s??-??i pui "
                "??ntreb??ri despre cum func??ioneaz?? de fapt lumea din jurul t??u ??i ce este "
                "Universul.",
                "Ted Chiang"
            )
            self.store(new_book)



class BookFileRepository(BookInMemoryRepository):
    """
    Clasa creata cu responsabilitatea de a gestiona
    multimea de carti de la biblioteca in fisier
    """
    def __init__(self, filename):
        BookInMemoryRepository.__init__(self)
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
            id, title, desc, auth = [token.strip() for token in line.split(";")]
            new_book = Book(id, title, desc, auth)
            BookInMemoryRepository.store(self, new_book)
        f.close()

    def __save_to_file(self):
        """
        Salveaza lista de carti in fisier
        """
        book_list = BookInMemoryRepository.get_booklist(self)
        with open(self.__file_name, "w") as f:
            for book in book_list:
                book_string = str(book.get_id()) + ";" + str(book.get_title()) + ";" + str(book.get_desc()) + \
                              ";" + str(book.get_auth()) + "\n"
                f.write(book_string)

    def store(self, book):
        """
        Adauga o carte in lista de carti
        :param book: cartea de adaugat
        :type book: Book
        """
        BookInMemoryRepository.store(self, book)
        self.__save_to_file()

    def get_booklist(self):
        """
        Returneaza lista cu toate cartile disponibile in biblioteca
        :return: lista de carti
        :rtype: list (of Book)
        """
        return BookInMemoryRepository.get_booklist(self)

    def size(self):
        """
        Returneaza numarul de carti din lista corespunzatoare bibliotecii
        :return: lungimea listei de carti
        :rtype: int
        """
        return BookInMemoryRepository.size(self)

    def update_book(self, id, updated_book):
        """
        Actualizeaza datele unei carti
        :param id: ID-ul cartii ce va fi modificata
        :type id: int
        :param updated_book: noua carte
        :type updated_book: Book
        """
        BookInMemoryRepository.update_book(self, id, updated_book)
        self.__save_to_file()

    def delete_book(self, book):
        """
        Sterge din lista de carti a bibliotecii o carte data
        :param book: cartea care se va sterge
        :type book: Book
        """
        BookInMemoryRepository.delete_book(self, book)
        self.__save_to_file()

    def get_book_with_id(self, id):
        """
        Returneaza cartea din lista de carti ce are id-ul egal cu cel dat
        :param id: id-ul cartii care se va returna
        :type id: int
        :return: cartea care are id-ul introdus
        :rtype: Book
        """
        return BookInMemoryRepository.get_book_with_id(self, id)

    def delete_all(self):
        """
        Sterge toate cartile din lista
        """
        BookInMemoryRepository.delete_all(self)
        self.__save_to_file()
