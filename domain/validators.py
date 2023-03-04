class BookValidator:
    """
    Clasa pentru validarea datelor unei carti
    """
    def validate(self, book):
        list_of_errors = []
        if len(book.get_auth().split()) < 2:
            list_of_errors.append("Numele autorului trebuie sa aiba cel putin 2 cuvinte.")
        if len(book.get_desc().split()) < 2:
            list_of_errors.append("Descrierea cartii nu poate fi doar un cuvant.")

        if len(list_of_errors):
            errors_as_string = "\n".join(list_of_errors)
            raise ValueError(errors_as_string)



class ClientValidator:
    """
    Clasa pentru validarea datelor unui client
    """
    def validate(self, client):
        list_of_errors = []
        if len(client.get_name().split()) < 2:
            list_of_errors.append("Numele trebuie sa aiba cel putin 2 cuvinte.")
        if len(client.get_CNP()) != 13 or not client.get_CNP().isdecimal():
            list_of_errors.append("CNP-ul trebuie sa fie format din exact 13 cifre.")

        if len(list_of_errors):
            errors_as_string = "\n".join(list_of_errors)
            raise ValueError(errors_as_string)



class IdValidator:
    """
    Clasa pentru validarea unui id
    """
    def validate(self, id, list_of_obj):
        try:
            id = int(id)
        except ValueError:
            raise ValueError(f"ID-ul trebuie sa fie un numar cuprins intre 0 si {len(list_of_obj)-1}.")
        if id < 0 or id > len(list_of_obj)-1:
            raise ValueError(f"ID-ul trebuie sa fie un numar cuprins intre 0 si {len(list_of_obj)-1}.")
