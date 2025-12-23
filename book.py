'''
This module has book class.
'''
import datetime

class Book:
    def __init__(self, 
                 name: str, 
                 author: str, 
                 genre: str, 
                 date_started: datetime.date, 
                 date_finished: datetime.date, 
                 rating: float, 
                 pages: int) -> None:
        
        if not isinstance(name, str) or not name:
            raise ValueError("Invalid Name.")

        if not isinstance(author, str) or not author:
            raise ValueError("Invalid Author Name.")
        
        if not isinstance(genre, str) or not genre:
            raise ValueError("Enter a valid genre.")
        
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Invalid page numbers.")
                
        if not isinstance(rating, (int, float)) or not (1 <= rating <= 5):
            raise ValueError("Invalid Rating. Enter a number between 1 to 5.")
        
        if not isinstance(date_started, datetime.date):
            raise ValueError("Start Date is invalid.")
        
        if not isinstance(date_finished, datetime.date):
            raise ValueError("Finish Date is invalid")

        if date_finished < date_started:
            raise ValueError("Finish date can not be before starting date")
      
        self.name = name
        self.author = author
        self.genre = genre
        self.date_started = date_started
        self.date_finished = date_finished
        self.rating = rating
        self.pages = pages

    def __str__(self) -> str:
        return f"""
Book Summary
Name : {self.name}
Author : {self.author}        
Genre : {self.genre}
Rating : {self.rating}
Pages : {self.pages}
"""
   
    def __eq__(self, other) -> bool:
        if isinstance(other, Book):
            return (self.name.lower() == other.name.lower() and
                    self.author.lower() == other.author.lower() and
                    self.pages == other.pages)
        return False    

    def to_dict(self) -> dict:
        # This function converts the Book class object into a dict.
        return {
            'name': self.name,
            'author': self.author,
            'genre': self.genre,
            'date_started': self.date_started.isoformat(),
            'date_finished': self.date_finished.isoformat(),
            'rating': self.rating,
            'pages': self.pages 
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Book':
        # This function converts the dict object into an object of Book class.
        return cls(name = data['name'], 
                   author = data['author'], 
                   genre = data['genre'], 
                   date_started = datetime.date.fromisoformat(data['date_started']), 
                   date_finished = datetime.date.fromisoformat(data['date_finished']), 
                   rating = data['rating'],
                   pages = data['pages'])


if __name__ == "__main__": 
    # Testing code
    book1 = Book('Ibadat', "Ayush Shukla", "Poetry", datetime.date(2024,11,10), datetime.date(2024,12,22), 5, 150) 

    book2 = Book('Ibadat', "Ayush Shukla", "Poetry", datetime.date(2024,11,10), datetime.date(2024,12,22), 5, 150) 
    book1_dict = book1.to_dict()
    print(book1_dict)
    book1_book = Book.from_dict(book1_dict)
    print(book1_book)

    book = Book(
        name="Test",
        author="Author",
        genre="Genre",
        date_started=datetime.date(2024, 1, 1),
        date_finished=datetime.date(2024, 1, 15),
        rating=4,  # None
        pages=100
    )
    print(book1 == book2)