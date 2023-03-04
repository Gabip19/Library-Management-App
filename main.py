"""
Scrieți o aplicație pentru o bibliotecă.
Aplicația stochează:
    • cărți: <id>,<titlu>,<descriere>,<autor>,etc
    • clienți: <id>, <nume>, <CNP>,etc
Creați o aplicație care permite:
    • gestiunea listei de cărți și clienți.
    • adaugă, șterge, modifică, lista de cărți, lista de clienți
    • căutare carte, căutare clienți.
    • Închiriere/returnare carte
    • Rapoarte:
        • Cele mai inchiriate cărți.
        • Clienți cu cărți închiriate ordonat dupa: nume, după numărul de cărți închiriate
        • Primi 20% dintre cei mai activi clienți (nume client si numărul de cărți închiriate)

Analiza Complexitate:
    contains_rent
Recursivitate:
    get_client_with_id_rec
    get_client_current_rents_rec
"""

from domain.validators import BookValidator, ClientValidator, IdValidator
from repository.book_repo import BookInMemoryRepository, BookFileRepository
from repository.client_repo import ClientInMemoryRepository, ClientFileRepository
from repository.rent_repo import RentInMemoryRepository, RentFileRepository
from service.book_service import BookService
from service.client_service import ClientService
from service.rent_service import RentService
from ui.console import Console


# SETUP BOOK SERVICE
book_validator = BookValidator()
# book_repository = BookInMemoryRepository()
book_repository = BookFileRepository("C:\\Users\\Asus\\PycharmProjects\\Proiect Biblioteca\\data\\books.txt")
book_service = BookService(book_repository, book_validator)

# SETUP CLIENT SERVICE
client_validator = ClientValidator()
# client_repository = ClientInMemoryRepository()
client_repository = ClientFileRepository("C:\\Users\\Asus\\PycharmProjects\\Proiect Biblioteca\\data\\clients.txt")
client_service = ClientService(client_repository, client_validator)

# SETUP RENTABOOK SERVICE
# rent_repository = RentInMemoryRepository()
rent_repository = RentFileRepository("data/rents.txt")
rent_service = RentService(rent_repository, client_repository, book_repository)

# SETUP UI
id_validator = IdValidator()
ui = Console(book_service, client_service, rent_service, id_validator)
ui.show_ui()
