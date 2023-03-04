class Book:
    def __init__(self, id, title, desc, auth):
        """
        Creeaza o noua carte cu id-ul id, titlul title,
        descrierea desc si autorul auth
        :param id: id-ul cartii
        :type id: int
        :param title: titlul cartii
        :type title: str
        :param desc: descrierea cartii
        :type desc: str
        :param auth: autorul cartii
        :type auth: str
        """
        self.__id = int(id)
        self.__title = title
        self.__desc = desc
        self.__auth = auth


    """GETTERS"""
    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_desc(self):
        return self.__desc

    def get_auth(self):
        return self.__auth


    """SETTERS"""
    def set_id(self, new_value):
        self.__id = new_value

    def set_title(self, new_value):
        self.__title = new_value

    def set_desc(self, new_value):
        self.__desc = new_value

    def set_auth(self, new_value):
        self.__auth = new_value


    def __eq__(self, other):
        """
        Defineste conceptul de egalitate a doua carti
        :param other: cartea cu care se compara
        :type other: Book
        :return: True daca cele doua carti sunt identice
        (au acelasi titlu si acelasi autor)
                 False altfel
        :rtype: bool
        """
        if self.__title == other.get_title() and self.__auth == other.get_auth():
            return True
        return False


    def __str__(self):
        return "ID: " + str(self.get_id()) + " TITLU: " + self.get_title() + " AUTOR: " + self.get_auth()



class Client:
    def __init__(self, id, name, CNP):
        """
        Creeaza o nou client cu id-ul id, numele name si CNP-ul CNP
        :param id: id-ul clientului
        :type id: int
        :param name: numele clientului
        :type name: str (2 cuvinte cel putin)
        :param CNP: CNP-ul clientului
        :type CNP:
        """
        self.__id = int(id)
        self.__name = name
        self.__CNP = CNP


    """GETTERS"""
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_CNP(self):
        return self.__CNP


    """SETTERS"""
    def set_id(self, new_value):
        self.__id = new_value

    def set_name(self, new_value):
        self.__name = new_value

    def set_CNP(self, new_value):
        self.__CNP = new_value


    def __eq__(self, other):
        """
        Defineste conceptul de egalitate dintre doi clienti
        :param other: clientul cu care se compara
        :type other: Client
        :return: True daca cei doi clienti sunt identici (au acelasi nume si CNP)
                 False altfel
        :rtype: bool
        """
        if self.__CNP == other.get_CNP() and self.__name == other.get_name():
            return True
        return False

    def __str__(self):
        return "ID: " + str(self.__id) + " NUME: " + self.__name + " CNP: " + self.__CNP
