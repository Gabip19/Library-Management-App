from domain.entities import Client


class ClientInMemoryRepository:
    """
    Clasa creata cu responsabilitatea de a gestiona
    multimea clientilor bibliotecii
    """
    def __init__(self):
        # Multimea clientilor: clientlist
        self.__clientlist = []
        self.__populate_list(False)

    def store(self, client):
        """
        Adauga un client in lista de clienti
        :param client: clientul de adaugat
        :type client: Client
        """
        self.__clientlist.append(client)

    def get_clientlist(self):
        """
        Returneaza lista cu toti clientii bibiliotecii
        :return: lista de clienti
        :rtype: list (of Client)
        """
        return self.__clientlist

    def size(self):
        """
        Returneaza numarul de clienti din lista clientilor bibliotecii
        :return: lungimea listei de clienti
        :rtype: int
        """
        return len(self.__clientlist)

    def delete_client(self, client):
        """
        Sterge din lista de clienti a bibliotecii un client dat
        :param client: clientul care se va sterge
        :type client: Client
        """
        self.__clientlist.remove(client)
        for i, el_client in enumerate(self.__clientlist):
            el_client.set_id(i)

    def is_client_in_list(self, client):
        """
        Verifica daca un client se afla in lista de clienti
        :param client: clientul care se cauta in lista
        :type client: Client
        :return: id-ul clientului daca clientul dat se afla in lista
                 -1 altfel
        :rtype: int
        """
        for client_ in self.__clientlist:
            if client_ == client:
                return client_.get_id()
        return -1

    def get_client_with_id(self, id):
        """
        Returneaza clientul din lista de clienti care are id-ul egal cu cel dat
        :param id: id-ul clientului care se va returna
        :type id: int
        :return: clientul care are id-ul introdus
        :rtype: Client
        """
        for client in self.__clientlist:
            if id == client.get_id():
                return client

    def get_client_with_id_rec(self, id, index):
        """
        Implementare recursiva
        Returneaza clientul din lista de clienti care are id-ul egal cu cel dat
        :param id: id-ul clientului care se va returna
        :type id: int
        :param index: index-ul elementului de la care va incepe cautarea (se apeleaza cu 0)
        :type index: int
        :return: clientul care are id-ul introdus
        :rtype: Client
        """
        if index >= self.size():
            return None
        elif id == self.__clientlist[index].get_id():
            return self.__clientlist[index]
        else:
            return self.get_client_with_id_rec(id, index+1)

    def delete_all(self):
        """
        Sterge toti clientii din lista
        """
        self.__clientlist = []

    def __populate_list(self, var):
        """
        Populeaza lista de clienti a bibliotecii cu cativa clienti predefiniti
        :param var: deicede daca lista de clienti va fi populata sau nu
        :type var: bool
        """
        if var:
            new_client = Client(0, "Andrei Mihailescu", "5001215570016")
            self.store(new_client)
            new_client = Client(1, "Adrian Doroftei", "1275728387234")
            self.store(new_client)
            new_client = Client(2, "Matei Ionescu", "4742818172447")
            self.store(new_client)
            new_client = Client(3, "Petru Andrei", "3827582189822")
            self.store(new_client)
            new_client = Client(4, "Alexandru Afloarei", "2498589238356")
            self.store(new_client)



class ClientFileRepository(ClientInMemoryRepository):
    """
    Clasa creata cu responsabilitatea de a gestiona
    multimea de clienti ai bibliotecii
    """
    def __init__(self, filename):
        ClientInMemoryRepository.__init__(self)
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
            id, name, CNP = [token.strip() for token in line.split(";")]
            new_client = Client(id, name, CNP)
            ClientInMemoryRepository.store(self, new_client)
        f.close()

    def __save_to_file(self):
        """
        Salveaza lista de carti in fisier
        """
        client_list = ClientInMemoryRepository.get_clientlist(self)
        with open(self.__file_name, "w") as f:
            for client in client_list:
                client_string = str(client.get_id()) + ";" + str(client.get_name()) + ";" + str(client.get_CNP()) + "\n"
                f.write(client_string)

    def store(self, client):
        """
        Adauga un client in lista de clienti
        :param client: clientul de adaugat
        :type client: Client
        """
        ClientInMemoryRepository.store(self, client)
        self.__save_to_file()

    def get_clientlist(self):
        """
        Returneaza lista cu toti clientii bibiliotecii
        :return: lista de clienti
        :rtype: list (of Client)
        """
        return ClientInMemoryRepository.get_clientlist(self)

    def size(self):
        """
        Returneaza numarul de clienti din lista clientilor bibliotecii
        :return: lungimea listei de clienti
        :rtype: int
        """
        return ClientInMemoryRepository.size(self)

    def delete_client(self, client):
        """
        Sterge din lista de clienti a bibliotecii un client dat
        :param client: clientul care se va sterge
        :type client: Client
        """
        ClientInMemoryRepository.delete_client(self, client)
        self.__save_to_file()

    def is_client_in_list(self, client):
        """
        Verifica daca un client se afla in lista de clienti
        :param client: clientul care se cauta in lista
        :type client: Client
        :return: id-ul clientului daca clientul dat se afla in lista
                 -1 altfel
        :rtype: int
        """
        return ClientInMemoryRepository.is_client_in_list(self, client)

    def get_client_with_id(self, id):
        """
        Returneaza clientul din lista de clienti care are id-ul egal cu cel dat
        :param id: id-ul clientului care se va returna
        :type id: int
        :return: clientul care are id-ul introdus
        :rtype: Client
        """
        return ClientInMemoryRepository.get_client_with_id(self, id)

    def get_client_with_id_rec(self, id, index):
        return ClientInMemoryRepository.get_client_with_id_rec(self, id, index)

    def delete_all(self):
        """
        Sterge toti clientii din lista
        """
        ClientInMemoryRepository.delete_all(self)
        self.__save_to_file()
