from book import Book
import json
import datetime
from pathlib import Path

def save_books(book_list: list[Book], filename: str = 'Library.json') -> None:
    
    new_book_list = [book.to_dict() for book in book_list]
    with open(filename, 'w') as f:
        json.dump(new_book_list, f, indent = 4)

        


def load_books(filename:str = 'Library.json') -> list[Book]:

    if Path(filename).exists():
        with open(filename, 'r') as f:
            book_list = json.load(f)
        try:
            return [Book.from_dict(book) for book in book_list]
        except json.JSONDecodeError:
            raise ValueError(f'Corrupted Json file {filename}')
        except (ValueError, KeyError, TypeError) as e:
            raise ValueError(f'Invalid Book Data. {e}')
    else:
        return []
    
def add_book(book: Book, book_list: list[Book]) -> None:

    if book not in book_list:
        book_list.append(book)
    

if __name__ == '__main__':

    book_list = load_books()
    print(book_list)
    book1 = Book('Ibadat', "Ayush Shukla", "Poetry", datetime.date(2024,11,10), datetime.date(2024,12,22), 5, 150)
    book2 = Book('RashmiRathi', "Ramdhari Singh Dinkar", "Poetry", datetime.date(2024,8,13), datetime.date(2024,9,12), 4.5, 300)
    book3 = Book('A Court of Mist and Fury', "Sarah J.", "Fantasy Novel", datetime.date(2024,11,10), datetime.date(2024,12,22), 3.5, 450)

    add_book(book1, book_list)
    add_book(book2, book_list)
    add_book(book3, book_list)

    
    save_books(book_list)
    print(book_list[2])


