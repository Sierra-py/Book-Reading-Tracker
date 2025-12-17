from book import Book
import datetime
import pytest


def test_valid_book():

    book = Book('Ibadat', "Ayush Shukla", "Poetry", datetime.date(2024,11,10), datetime.date(2024,12,22), 5, 150)
    assert book.name == 'Ibadat'
    assert book.author == 'Ayush Shukla'
    assert book.date_started == datetime.date(2024,11,10)

def test_invalid_name_or_author():
    with pytest.raises(ValueError):
        Book(None, "Ayush Shukla", "Poetry", datetime.date(2024,11,10), datetime.date(2024,12,22), 6, 150)

    with pytest.raises(ValueError):
        Book("Ibadat", 123, "Poetry", datetime.date(2024,11,10), datetime.date(2024,12,22), 6, 150)

def test_invalid_rating():            
    with pytest.raises(ValueError):
        Book('Ibadat', "Ayush Shukla", "Poetry", datetime.date(2024,11,10), datetime.date(2024,12,22), 6, 150)

    with pytest.raises(ValueError):
        Book("Ibadat", "Ayush Shukla", "Poetry", datetime.date(2024,11,10), datetime.date(2024,12,22), -2, 150)

def test_finish_date_before_start_date():
    with pytest.raises(ValueError):
        Book('Ibadat', "Ayush Shukla", "Poetry", datetime.date(2024,11,10), datetime.date(2024,10,22), 5, 150)

def test_invalid_dates():
    with pytest.raises(ValueError):
        Book('Ibadat', "Ayush Shukla", "Poetry", None, datetime.date(2024,12,22), 5, 150)

    with pytest.raises(ValueError):
        Book(None, "Ayush Shukla", "Poetry", datetime.date(2024,11,10), '2024-12-22', 6, 150)

def test_invalid_pages():
    with pytest.raises(ValueError):
        Book("Ibadat", "Ayush Shukla", "Poetry", datetime.date(2024,11,10), datetime.date(2024,12,22), 6, '50 pages')
    with pytest.raises(ValueError):
        Book(None, "Ayush Shukla", "Poetry", datetime.date(2024,11,10), datetime.date(2024,12,22), 6, 0)

def test_to_dict():
    book1 = Book('Ibadat', "Ayush Shukla", "Poetry", datetime.date(2024,11,10), datetime.date(2024,12,22), 5, 150)
    book_dict = book1.to_dict()
 
    assert book_dict['name'] == 'Ibadat'
    assert book_dict['rating'] == 5
    assert book_dict['date_started'] == "2024-11-10"

def test_from_dict():

    book_dict = {
    'name': 'Ibadat', 
    'author': 'Ayush Shukla', 
    'genre': 'Poetry', 
    'date_started': '2024-11-10', 
    'date_finished': '2024-12-22', 
    'rating': 5, 
    'pages': 150
    }

    book1 = Book.from_dict(book_dict)

    assert book1.name == 'Ibadat'
    assert book1.author == 'Ayush Shukla'
    assert book1.date_finished == datetime.date(2024, 12, 22)