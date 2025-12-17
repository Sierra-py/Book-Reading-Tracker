from book import Book
from library import add_book, load_books, save_books


def book_per_month(book_list: list[Book]) -> dict[str, int]:
    '''This functions returns the number of books finished in each month.'''
    month_count = {}

    for book in book_list:
        finished_date = f'{book.date_finished.year}-{book.date_finished.month:02d}'
        month_count[finished_date] = month_count.get(finished_date, 0) + 1

    return month_count

def average_pages(book_list: list[Book]) -> int:
    '''This function returns the average number of pages per book.'''
    
    pages = 0
    books_no = len(book_list)
    for book in book_list:
        pages += book.pages

    return (pages//books_no) if books_no > 0 else 0

def genre_distribution(book_list: list[Book]) -> dict[str, int]:
    '''number of books per each genre in form of a dict with genre as keys and no. of books as value.
    '''
    genres = {}
    for book in book_list:
        genres[book.genre] = genres.get(book.genre, 0) + 1

    return genres

def rating_distribution(book_list: list[Book]) -> dict[str, int]:
    '''return: number of books by rating in form of a dict with rating as keys and no. of books as value.    '''

    ratings = {'5':0, '4+':0, '3+':0, '2+':0, '1+':0}

    for book in book_list:
        if book.rating == 5:
            ratings['5'] += 1
        elif book.rating >= 4:
            ratings['4+'] += 1
        elif book.rating >= 3:
            ratings['3+'] += 1
        elif book.rating >= 2:
            ratings['2+'] += 1
        elif book.rating >= 1:
            ratings['1+'] += 1

    return ratings

def reading_speed(book_list: list[Book]) -> dict:
    '''return: reading speed of each book in form of a dict with book number as keys and speed in pages_per_day as value.'''
    
    pages_per_day = {}
    for i, book in enumerate(book_list):
        days_to_complete = (book.date_finished - book.date_started).days
        if days_to_complete == 0:
            days_to_complete = 1
        pages_per_day[book.name] = book.pages // days_to_complete
    return pages_per_day

if __name__ == '__main__':

    # code for testing purpose

    book_list = load_books()
    reads_per_month = book_per_month(book_list)
    print(reads_per_month)
    print(average_pages(book_list))
    print(genre_distribution(book_list))
    print(rating_distribution(book_list))
    print(reading_speed(book_list))

