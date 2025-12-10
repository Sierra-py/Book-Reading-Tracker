'''
This module has book class.
'''
import datetime

class Book:
    def __init__(self, name: str, author: str, genre: str, date_started: datetime.date, date_finished: datetime.date, rating: float) -> None:
        
        if not name:
            raise ValueError("Name can not be empty.")

        elif not isinstance(author, str) or not author:
            raise ValueError("Enter a Valid Author Name.")
        
        elif not (1 <= rating <= 5):
            raise ValueError("Invalid Rating. Enter a number between 1 to 5.")
        
        elif not isinstance(date_started, datetime.date):
            raise ValueError("Start Date is invalid.")
        
        elif not isinstance(date_finished, datetime.date):
            raise ValueError("Finish Date is invalid")

        elif date_finished < date_started:
            raise ValueError("Finish date can not be before starting date")
        
        elif not isinstance(genre, str) or not genre:
            raise ValueError("Enter a valid genre.")
        
        self.name = name
        self.author = author
        self.genre = genre
        self.date_started = date_started
        self.date_finished = date_finished
        self.rating = rating


    def __str__(self) -> str:
        return f"""
Book Summary
Name : {self.name}
Author : {self.author}        
Genre : {self.genre}
Rating : {self.rating}
"""


if __name__ == "__main__": 
    # Testing code
    book1 = Book('Ibadat', "Ayush Shukla", "Poetry", datetime.date(2024,11,10), datetime.date(2025,1,12), 5) 
    print(book1)
    print(isinstance(book1.date_started, datetime.date))