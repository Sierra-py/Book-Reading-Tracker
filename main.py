from book import Book
from library import save_books, load_books
from analytics import book_per_month, average_pages, genre_distribution, rating_distribution, reading_speed
from visualize import plot_books_per_month, plot_genre_distribution, plot_rating_distribution, plot_reading_speed
import json
import datetime

def main():

    # Welcome Message
    print("\033[94m\033[1m","\nBook Reading Tracker\n", "\033[0m")

    # Main Menu Loop
    while True:
        print("\033[36m" + "="*8, "MENU", "="*8 + '\n' + "\033[0m")
        print('1. Show All Books.\n'
        '2. Add A Book.\n'
        '3. Show Analytics.\n'
        '4. Show Visualizations.\n'
        '5. Exit\n')

        choice = input("Choose Option: ").strip()
        
        if choice == "1":
            view_books(books)
        elif choice == "2":
            add_book_interface(books)
        elif choice == "3":
            view_analytics(books)
        elif choice == "4":
            view_visualizations(books)
        elif choice == "5":
            save_books(books)
            print("Saved. Goodbye!\n")
            break
        else:
            print("Invalid choice. Try again.\n")

def add_book_interface(books):
    
    while True:
        name = input("Enter the name of the book: ")
        if not name:
            print('\nName cannot be empty.\n')
        else:
            break
    
    while True:
        author = input("Enter author's name: ").title()
        if not author:
            print('\nAuthor name cannot be empty.\n')
        else:
            break
   
    while True:
        genre = input("Enter book's genre: ").title()
        if not genre:
            print("\nGenre cannot be empty. If genre is not specified enter 'others'.\n")
        else:
            break

    while True:
        try:
            start_input = input("Start date (yyyy-mm-dd): ")
            date_started = datetime.date.fromisoformat(start_input)
            
            finish_input = input("Finish date (yyyy-mm-dd): ")
            date_finished = datetime.date.fromisoformat(finish_input)
            
            if date_finished >= date_started:
                break
            else:
                print("\nFinish date must be after start date.\n")
        except ValueError:
            print("\nInvalid date format. Use yyyy-mm-dd.\n")    

    while True:
        try:
            rating = float(input("How would you rate this book on a scale of 1-5: "))
            if 1<=rating<=5:
                break
            else:
                print("Rating should be between 1-5\n")
        except ValueError:
            print('\nRating should be a number between 1-5.\n')

    while True:
        try:
            pages = int(input("Enter page count of this book: "))
            break
        except ValueError:
            print('Invalid number of pages. Enter a valid integer.\n')
  
    try:
        book = Book(name, author, genre, date_started, date_finished, rating, pages)
        if book not in books:
            books.append(book)
            print("\nBook added successfully.\n")
        else:
            print("\nThis book already exists in library.\n")
    except ValueError:
        print("\nInvalid Book\n")
    

def view_books(books):

    if not books:
        print(f"There are no books in current library.\n")
    else:
        for book in books:
            print(book)

def view_analytics(books):
    if not books:
        print(f"There are no books in current library.\n")
    else:
        s1 = book_per_month(books)
        s2 = average_pages(books)
        s3 = genre_distribution(books)
        s4 = rating_distribution(books)
        s5 = reading_speed(books)
        
        print(f"-----Number of books per month-----\n")
        print(json.dumps(s1, indent=1), '\n')
        print(f'-----Average number of pages in books-----\n{s2} pages\n')
        print(f"-----Number of books per genre-----\n")
        print(json.dumps(s3, indent=1), '\n')
        print(f"-----Books distribution by their ratings-----")
        print(json.dumps(s4, indent=1), '\n')
        print(f'-----Reading speed of each book-----\n')
        print(json.dumps(s5, indent=1), '\n')
        print(f'\n-----Total number of books in library-----\n{len(books)} books\n')

def view_visualizations(books):
    if not books:
        print(f"There are no books in current library.\n")
    else:
        while True:
            print("Welcome to visualizations\n" \
            "1. Show plot of books read per month\n" \
            "2. Show plot of genre distribution of books.\n" \
            "3. Show plot of rating distribution of books.\n" \
            "4. Show plot of reading speeds per book\n" \
            "5. Back to main menu.\n")

            choice = input("Which plot do you want to see? ")
            if choice == "1":
                plot_books_per_month(book_per_month(books))
            elif choice == "2":
                plot_genre_distribution(genre_distribution(books))
            elif choice == "3":
                plot_rating_distribution(rating_distribution(books))
            elif choice == "4":
                plot_reading_speed(reading_speed(books))
            elif choice == "5":
                break
            else:
                print("Invalid choice. Try again.\n")


if __name__ == '__main__':
    books = load_books()
    main()