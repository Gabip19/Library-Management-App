from termcolor import colored


class Console:
    def __init__(self, book_srv, client_srv, rent_srv, id_val):
        self.__book_srv = book_srv
        self.__client_srv = client_srv
        self.__rent_srv = rent_srv
        self.__id_validator = id_val


    def show_ui(self):
        """
        Meniul principal al programului de unde se fac alegerile
        """
        while True:
            try:
                self.__print_main_menu()
                option = self.__get_option()
                if option == 1:
                    self.__book_submenu()
                elif option == 2:
                    self.__client_submenu()
                elif option == 3:
                    self.__search_book()
                elif option == 4:
                    self.__search_client()
                elif option == 5:
                    self.__search_client_by_id()
                elif option == 6:
                    self.__rent_book()
                elif option == 7:
                    self.__return_book()
                elif option == 8:
                    self.__generate_random()
                elif option == 9:
                    self.__generate_random1()
                elif option == 10:
                    self.__reports_submenu()
                elif option == 11:
                    print("\n")
                    list_rents = self.__rent_srv.get_all_rents()
                    for el in list_rents:
                        print(el)
                        print("-"*60)
                    print("\n")
                elif option == 12:
                    return
                else:
                    print(colored("Optiune invalida.\n", "red"))
            except ValueError as ve:
                print(colored(str(ve)+"\n", "red"))


    @staticmethod
    def __print_main_menu():
        """
        Printeaza meniul principal al programului
        """
        print("1. Gestioneaza lista de carti.")
        print("2. Gestioneaza lista de clienti.")
        print("3. Cauta carte.")
        print("4. Cauta client.")
        print("5. Cauta client dupa id.")
        print("6. Inchiriaza carte.")
        print("7. Returneaza carte.")
        print("8. Genereaza clienti aleatoriu.")
        print("9. Genereaza inchirieri aleatorii.")
        print("10. Rapoarte.")
        print("11. Printeaza lista inchirierilor.")
        print("12. Exit.\n")


    @staticmethod
    def __get_option():
        """
        Citeste de la tastatura optiunea utilizatorului
        :raise ValueError daca optiunea nu este un numar intreg
        """
        try:
            option = int(input("Optiunea dumneavoastra este: "))
            return option
        except ValueError:
            raise ValueError("Optiunea trebuie sa fie un numar.")


    """BOOK UI"""
    def __book_submenu(self):
        """
        Submeniul corespunzator operatiilor pe lista de carti
        """
        self.__print_book_menu()
        option = self.__get_option()
        if option == 1:
            self.__add_book()
        elif option == 2:
            self.__update_book()
        elif option == 3:
            self.__delete_book()
        elif option == 4:
            self.__show_all_books()
        else:
            print(colored("Optiune invalida.\n", "red"))


    @staticmethod
    def __print_book_menu():
        """
        Printeaza submeniul corespunzator listei de carti
        """
        print("1. Adauga o noua carte la lista.")
        print("2. Modifica o carte existenta in lista.")
        print("3. Sterge o carte din lista.")
        print("4. Printeaza lista de carti.\n")


    def __add_book(self):
        """
        Adauga o carte cu datele citite de la tastatura
        """
        title = input("Titlul cartii: ")
        desc = input("Descrierea cartii: ")
        auth = input("Autorul cartii: ")

        new_book = self.__book_srv.add_book(title, desc, auth)
        print(colored("Cartea cu numele", "green"), new_book.get_title(), colored("a autorului", "green"),
              new_book.get_auth(), colored("a fost adaugata cu succes.\n", "green"))


    def __update_book(self):
        """
        Modifica datele unei carti existente in lista
        """
        current_book_list = self.__book_srv.get_all_books()
        for book in current_book_list:
            print(book)

        input_id = input("\nIntroduceti ID-ul cartii pe care doriti sa o modificati: ")
        self.__id_validator.validate(input_id, self.__book_srv.get_all_books())
        input_id = int(input_id)

        input_title = input("Introduceti noul titlu: ")
        input_auth = input("Introduceti noul autor: ")
        input_desc = input("Introduceti noua descriere:\n")
        self.__book_srv.update_book(input_id, input_title, input_desc, input_auth)
        print(colored("Cartea cu ID-ul", "green"), input_id, colored("a fost actualizata cu succes.\n", "green"))


    def __delete_book(self):
        """
        Sterge din lista o carte cu datele citite de la tastatura
        """
        title = input("Titlul cartii pe care doriti sa o stergeti:\n")
        auth = input("Autorul cartii pe care doriti sa o stergeti:\n")

        self.__book_srv.delete_book(title, auth)
        print(colored("Cartea cu numele", "green"), title, colored("a autorului", "green"),
              auth, colored("a fost stearsa din lista.\n", "green"))


    def __show_all_books(self):
        """
        Afiseaza toate cartile din lista de carti a bibliotecii
        """
        book_list = self.__book_srv.get_all_books()
        if len(book_list):
            print('-'*60)
            for book in book_list:
                print(colored("Titlu: ", "cyan"), book.get_title())
                print(colored("Autor: ", "cyan"), book.get_auth())
                print(colored("Descriere:\n", "cyan"), book.get_desc())
                print('-'*60)
            print("\n")
        else:
            print(colored("Nu exista carti in lista.\n", "cyan"))


    def __search_book(self):
        """
        Afiseaza lista de carti ce au titlul specificat sau care
        contin in titlu o secventa data
        """
        seq_to_search = input("Introduceti o secventa din titlul cartii sau "
                              "titlul cartii pe care doriti sa o cautati:\n")
        book_list = self.__book_srv.search_in_titles(seq_to_search)
        if len(book_list):
            print(colored("\nCartile existente sunt:", "green"))
            for book in book_list:
                print(book)
        else:
            print(colored("Nu s-a gasit nicio carte cu datele introduse.", "cyan"))
        print("\n")


    """CLIENT UI"""
    def __client_submenu(self):
        """
        Submeniul corespunzator operatiilor pe lista de clienti
        """
        self.__print_client_menu()
        option = self.__get_option()
        if option == 1:
            self.__add_client()
        elif option == 2:
            self.__update_client()
        elif option == 3:
            self.__delete_client()
        elif option == 4:
            self.__show_all_clients()
        else:
            print(colored("Optiune invalida.\n", "red"))


    @staticmethod
    def __print_client_menu():
        """
        Printeaza submeniul corespunzator listei de clienti
        """
        print("1. Adauga un nou client la lista.")
        print("2. Modifica datele unui client existent in lista.")
        print("3. Sterge un client din lista.")
        print("4. Printeaza lista de clienti.\n")


    def __add_client(self):
        """
        Adauga un client cu datele citite de la tastatura
        """
        name = input("Numele: ")
        CNP = input("CNP: ")

        new_client = self.__client_srv.add_client(name, CNP)
        print(colored("Clientul cu numele", "green"), new_client.get_name(),
              colored("a fost adaugat cu succes.\n", "green"))


    def __update_client(self):
        """
        Modifica datele unui client existent in lista
        """
        self.__show_all_clients()

        input_id = input("Introduceti ID-ul clientului a caror date doriti sa le modificati: ")
        self.__id_validator.validate(input_id, self.__client_srv.get_all_clients())
        input_id = int(input_id)

        input_name = input("Introduceti noul nume: ")
        input_CNP = input("Introduceti noul CNP: ")
        client = self.__client_srv.get_client_with_id(input_id)
        updated_client = self.__client_srv.update_client(input_id, input_name, input_CNP)
        self.__rent_srv.update_rents_for_client(client, updated_client)

        print(colored("Datele clientul cu ID-ul", "green"), input_id,
              colored("au fost actualizate cu succes.\n", "green"))


    def __delete_client(self):
        """
        Sterge din lista un client cu datele citite de la tastatura
        """
        name = input("Numele clientului pe care doriti sa il stergeti:\n")
        CNP = input("CNP-ul clientului pe care doriti sa il stergeti:\n")

        self.__client_srv.delete_client(name, CNP)
        print(colored("Clientul cu numele", "green"), name, colored("a fost sters din lista.\n", "green"))


    def __show_all_clients(self):
        """
        Afiseaza toti clientii din lista de clienti a bibliotecii
        """
        client_list = self.__client_srv.get_all_clients()
        if len(client_list):
            for client in client_list:
                print("Id:", colored(client.get_id(), "cyan"), "Nume:", colored(client.get_name(), "cyan"),
                      "CNP:", colored(client.get_CNP(), "cyan"))
            print("\n")
        else:
            print(colored("Nu exista clienti in lista.\n", "cyan"))


    def __search_client(self):
        """
        Verifica daca un client se afla in lista de clienti
        """
        input_name = input("Introduceti numele clientului: ")
        input_CNP = input("Introduceti CNP-ul clientului: ")

        id = self.__client_srv.search_client(input_name, input_CNP)
        if id >= 0:
            print(colored("\nClientul cautat se afla in lista.", "green"))
            print("Id:", colored(id, "cyan"), "Nume:", colored(input_name, "cyan"), "CNP:", colored(input_CNP, "cyan"))
            self.__print_client_rented_books(id)
        else:
            print(colored("\nClientul cautat nu se afla in lista.\n", "cyan"))


    def __search_client_by_id(self):
        """
        Afiseaza clientul cu id-ul dat
        """
        client_id = input("Introduceti id-ul clientului: ")
        self.__id_validator.validate(client_id, self.__client_srv.get_all_clients())
        client_id = int(client_id)

        client = self.__client_srv.get_client_with_id(client_id)
        print("\nId:", colored(str(client_id), "cyan"), "Nume:", colored(client.get_name(), "cyan"), "CNP:",
              colored(client.get_CNP(), "cyan"))
        self.__print_client_rented_books(client_id)


    def __print_client_rented_books(self, client_id):
        """
        Afiseaza lista cartilor inchiriate de un client cu id-ul dat
        """
        client_rents = self.__rent_srv.get_client_current_rents(client_id)
        if len(client_rents):
            print(colored("Carti inchiriate:", "yellow"))
            for rent in client_rents:
                print(rent.get_rented_book())
        else:
            print(colored("Clientul nu are carti inchiriate.", "yellow"))
        print("\n")


    def __generate_random(self):
        """
        UI pt generarea de clienti aleatoriu
        """
        try:
            number_of_entities = int(input("Introduceti numarul de entitati: "))
        except ValueError:
            raise ValueError("Numarul de entitati trebuie sa fie un numar intreg strict pozitiv.")
        if number_of_entities <= 0:
            raise ValueError("Numarul de entitati trebuie sa fie un numar intreg strict pozitiv.")

        self.__client_srv.generate_random_clients(number_of_entities)
        print(colored(f"\nAu fost generati cu succes {number_of_entities} clienti.\n", "green"))


    """RENT SERVICE UI"""
    def __rent_book(self):
        """
        UI pentru inchiriere carte
        """
        print(colored("\n== Inchiriaza carte ==", "cyan"))

        client_id = input("Introduceti id-ul clientului: ")
        self.__id_validator.validate(client_id, self.__client_srv.get_all_clients())

        book_id = input("Introduceti id-ul cartii: ")
        self.__id_validator.validate(book_id, self.__book_srv.get_all_books())

        self.__rent_srv.rent_book(int(client_id), int(book_id))

        print(colored("Cartea a fost inchiriata cu succes.\n", "green"))


    def __return_book(self):
        """
        UI pentru returnare carte
        """
        print(colored("\n== Returneaza carte ==", "cyan"))

        client_id = input("Introduceti id-ul clientului: ")
        self.__id_validator.validate(client_id, self.__client_srv.get_all_clients())

        book_id = input("Introduceti id-ul cartii: ")
        self.__id_validator.validate(book_id, self.__book_srv.get_all_books())

        self.__rent_srv.return_book(int(client_id), int(book_id))

        print(colored("Cartea a fost returnata cu succes.\n", "green"))


    """REPORTS UI"""
    def __reports_submenu(self):
        """
        Submeniul corespunzator rapoartelor
        """
        self.__print_reports_menu()
        option = self.__get_option()
        if option == 1:
            self.__most_rented_books()
        elif option == 2:
            self.__clients_ord_by_name()
        elif option == 3:
            self.__clients_ord_by_rentsn()
        elif option == 4:
            self.__active_clients()
        elif option == 5:
            self.__most_rented_auths()
        else:
            print(colored("Optiune invalida.\n", "red"))

    @staticmethod
    def __print_reports_menu():
        """
        Printeaza submeniul corespunzator rapoartelor
        """
        print("\n1. Afiseaza cele mai inchiriate carti.")
        print("2. Afizeaza clientii cu carti inchiriate ordonati dupa nume.")
        print("3. Afiseaza clientii cu carti inchiriate ordonati dupa numarul de carti inchiriate.")
        print("4. Primi 20% dintre cei mai activi clienti.")
        print("5. Afiseaza cei mai inchiriati autori.\n")


    def __most_rented_books(self):
        """
        Afiseaza cele mai inchiriate carti in ordinea descrescatoare a numarului de inchirieri
        """
        result_list = self.__rent_srv.get_most_rented_books()
        if len(result_list):
            for i, book_dto in enumerate(result_list):
                print(str(i) + colored(") Titlu: ", "cyan") + book_dto.get_field1() + colored(" Autor: ", "cyan") +
                      book_dto.get_field2() + colored(" Numar inchirieri: ", "cyan") + str(book_dto.get_field3()))
            print("\n")
        else:
            raise ValueError("Nu exista carti inchiriate.\n")


    def __clients_ord_by_rentsn(self):
        """
        Afiseaza clientii cu carti inchiriare ordonati dupa numarul de carti inchiriate
        """
        result_list = self.__rent_srv.clients_ord_by_rentsn()
        self.__print_client_result_list(result_list)


    def __clients_ord_by_name(self):
        """
        Afiseaza clientii cu carti inchiriate ordonati dupa nume
        """
        result_list = self.__rent_srv.clients_ord_by_name()
        self.__print_client_result_list(result_list)


    def __active_clients(self):
        """
        Afiseaza primii 20% dintre cei mai activi clienti
        """
        result_list = self.__rent_srv.get_active_clients(20)
        self.__print_client_result_list(result_list)


    @staticmethod
    def __print_client_result_list(result_list):
        """
        Afiseaza clientii din lista rezultata de dupa calculul raportului
        """
        if len(result_list):
            for i, el in enumerate(result_list):
                print(str(i) + colored(") Nume: ", "cyan") + el.get_field1() +
                      colored(" nr. carti inchiriate: ", "cyan") + str(el.get_field2()))
            print("\n")
        else:
            raise ValueError("Nu exista clienti cu carti inchiriate.\n")


    def __most_rented_auths(self):
        """
        UI pt cei mai inchiriati autori
        """
        result_list = self.__rent_srv.get_most_rented_auths(5)
        for i, el in enumerate(result_list):
            print(str(i) + colored(") Autor: ", "cyan") + el.get_field1()
                  + colored(" nr. inchirieri: ", "cyan") + str(el.get_field2()))
        print("\n")


    def __generate_random1(self):
        """
        UI pt generarea de rent-uri aleatorii
        """
        try:
            number_of_entities = int(input("Introduceti numarul de entitati: "))
        except ValueError:
            raise ValueError("Numarul de entitati trebuie sa fie un numar intreg strict pozitiv.")
        if number_of_entities <= 0:
            raise ValueError("Numarul de entitati trebuie sa fie un numar intreg strict pozitiv.")

        self.__rent_srv.generate_random_rents(number_of_entities)
        print(colored(f"\nAu fost generate cu succes inchirieri aleatorii.\n", "green"))
