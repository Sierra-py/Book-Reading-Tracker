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

    
    book4 = Book('The Silent Patient', 'Alex Michaelides', 'Thriller', datetime.date(2024, 1, 5), datetime.date(2024, 2, 10), 4.5, 368)
    book5 = Book('Where the Crawdads Sing', 'Delia Owens', 'Mystery', datetime.date(2023, 11, 1), datetime.date(2023, 12, 15), 4.8, 375)
    book6 = Book('The Midnight Library', 'Matt Haig', 'Fantasy', datetime.date(2023, 7, 20), datetime.date(2023, 9, 1), 4.2, 304)
    book7 = Book('Becoming', 'Michelle Obama', 'Biography', datetime.date(2024, 5, 15), datetime.date(2024, 6, 25), 4.9, 448)
    book8 = Book('Educated', 'Tara Westover', 'Memoir', datetime.date(2024, 4, 10), datetime.date(2024, 5, 5), 4.7, 334)
    book9 = Book('The Book Thief', 'Markus Zusak', 'Historical Fiction', datetime.date(2024, 8, 12), datetime.date(2024, 9, 18), 4.6, 552)
    book10 = Book('Dune', 'Frank Herbert', 'Science Fiction', datetime.date(2024, 2, 1), datetime.date(2024, 3, 30), 4.8, 896)
    book11 = Book('The Vanishing Half', 'Brit Bennett', 'Literary Fiction', datetime.date(2024, 3, 15), datetime.date(2024, 4, 25), 4.5, 343)
    book12 = Book('The Alchemist', 'Paulo Coelho', 'Adventure', datetime.date(2024, 6, 5), datetime.date(2024, 7, 10), 4.4, 208)
    book13 = Book('The Four Winds', 'Kristin Hannah', 'Historical Fiction', datetime.date(2024, 9, 1), datetime.date(2024, 10, 20), 4.7, 464)
    book14 = Book('The Giver of Stars', 'Jojo Moyes', 'Historical Fiction', datetime.date(2024, 7, 10), datetime.date(2024, 8, 20), 4.3, 400)
    book15 = Book('Circe', 'Madeline Miller', 'Fantasy', datetime.date(2024, 10, 1), datetime.date(2024, 11, 10), 4.5, 400)
    book16 = Book('The Invisible Life of Addie LaRue', 'V.E. Schwab', 'Fantasy', datetime.date(2024, 1, 10), datetime.date(2024, 2, 15), 4.7, 444)
    book17 = Book('Normal People', 'Sally Rooney', 'Romance', datetime.date(2023, 12, 1), datetime.date(2024, 1, 10), 4.3, 273)
    book18 = Book('The Night Circus', 'Erin Morgenstern', 'Fantasy', datetime.date(2024, 3, 10), datetime.date(2024, 4, 30), 4.6, 387)
    book19 = Book('The Secret History', 'Donna Tartt', 'Thriller', datetime.date(2024, 11, 15), datetime.date(2024, 12, 20), 4.7, 559)
    book20 = Book('Little Fires Everywhere', 'Celeste Ng', 'Literary Fiction', datetime.date(2024, 2, 5), datetime.date(2024, 3, 5), 4.4, 338)
    book21 = Book('The Seven Husbands of Evelyn Hugo', 'Taylor Jenkins Reid', 'Romance', datetime.date(2024, 6, 1), datetime.date(2024, 7, 15), 4.6, 400)
    book22 = Book('The Goldfinch', 'Donna Tartt', 'Literary Fiction', datetime.date(2024, 5, 1), datetime.date(2024, 6, 10), 4.8, 771)
    book23 = Book('The Shadow of the Wind', 'Carlos Ruiz Zafón', 'Historical Fiction', datetime.date(2024, 4, 1), datetime.date(2024, 5, 20), 4.7, 487)
    book24 = Book('A Little Life', 'Hanya Yanagihara', 'Literary Fiction', datetime.date(2024, 8, 1), datetime.date(2024, 9, 15), 4.6, 720)
    book25 = Book('Anxious People', 'Fredrik Backman', 'Comedy', datetime.date(2024, 7, 15), datetime.date(2024, 8, 5), 4.4, 368)
    book26 = Book('All the Light We Cannot See', 'Anthony Doerr', 'Historical Fiction', datetime.date(2024, 9, 1), datetime.date(2024, 10, 5), 4.7, 531)
    book27 = Book('The Ocean at the End of the Lane', 'Neil Gaiman', 'Fantasy', datetime.date(2024, 2, 20), datetime.date(2024, 3, 10), 4.5, 181)
    book28 = Book('The Henna Artist', 'Alka Joshi', 'Historical Fiction', datetime.date(2024, 6, 25), datetime.date(2024, 8, 10), 4.6, 358)
    book29 = Book('The Song of Achilles', 'Madeline Miller', 'Fantasy', datetime.date(2024, 5, 5), datetime.date(2024, 6, 15), 4.8, 374)
    book30 = Book('Homegoing', 'Yaa Gyasi', 'Historical Fiction', datetime.date(2024, 3, 10), datetime.date(2024, 4, 15), 4.6, 305)
    book31 = Book('Red, White & Royal Blue', 'Casey McQuiston', 'Romance', datetime.date(2024, 2, 1), datetime.date(2024, 3, 1), 4.6, 421)
    book32 = Book('The House in the Cerulean Sea', 'TJ Klune', 'Fantasy', datetime.date(2024, 7, 10), datetime.date(2024, 8, 1), 4.7, 400)
    book33 = Book('The Light We Lost', 'Jill Santopolo', 'Romance', datetime.date(2024, 6, 15), datetime.date(2024, 7, 10), 4.4, 368)
    book34 = Book('The Chain', 'Adrian McKinty', 'Thriller', datetime.date(2024, 8, 15), datetime.date(2024, 9, 5), 4.5, 416)
    book35 = Book('The Whisper Man', 'Alex North', 'Thriller', datetime.date(2024, 1, 25), datetime.date(2024, 2, 15), 4.3, 368)
    book36 = Book('The Couple Next Door', 'Shari Lapena', 'Thriller', datetime.date(2024, 4, 15), datetime.date(2024, 5, 10), 4.4, 320)
    book37 = Book('Before We Were Strangers', 'Renée Carlino', 'Romance', datetime.date(2024, 10, 15), datetime.date(2024, 11, 10), 4.4, 368)
    book38 = Book('The Girl on the Train', 'Paula Hawkins', 'Psychological Thriller', datetime.date(2024, 1, 5), datetime.date(2024, 2, 5), 4.2, 395)
    book39 = Book('Sharp Objects', 'Gillian Flynn', 'Thriller', datetime.date(2024, 3, 1), datetime.date(2024, 4, 5), 4.4, 254)
    book40 = Book('The Wife Between Us', 'Greer Hendricks & Sarah Pekkanen', 'Thriller', datetime.date(2024, 7, 5), datetime.date(2024, 8, 5), 4.1, 350)
    book41 = Book('Verity', 'Colleen Hoover', 'Thriller', datetime.date(2024, 6, 1), datetime.date(2024, 7, 10), 4.7, 320)



    add_book(book1, book_list)
    add_book(book2, book_list)
    add_book(book3, book_list)
    add_book(book4, book_list)
    add_book(book5, book_list)
    add_book(book6, book_list)
    add_book(book7, book_list)
    add_book(book8, book_list)
    add_book(book9, book_list)
    add_book(book10, book_list)
    add_book(book11, book_list)
    add_book(book12, book_list)
    add_book(book13, book_list)
    add_book(book14, book_list)
    add_book(book15, book_list)
    add_book(book16, book_list)
    add_book(book17, book_list)
    add_book(book18, book_list)
    add_book(book19, book_list)
    add_book(book20, book_list)
    add_book(book21, book_list)
    add_book(book22, book_list)
    add_book(book23, book_list)
    add_book(book24, book_list)
    add_book(book25, book_list)
    add_book(book26, book_list)
    add_book(book27, book_list)
    add_book(book28, book_list)
    add_book(book29, book_list)
    add_book(book30, book_list)
    add_book(book31, book_list)
    add_book(book32, book_list)
    add_book(book33, book_list)
    add_book(book34, book_list)
    add_book(book35, book_list)


    
    save_books(book_list)
    print(book_list[2])


