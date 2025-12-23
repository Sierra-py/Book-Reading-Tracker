import matplotlib.pyplot as plt
from library import *
from analytics import *

def plot_books_per_month(month_count: dict[str, int]) -> None:
    plt.bar(list(month_count.keys()), list(month_count.values()))
    plt.title('Books finished in a month.')
    plt.xlabel('Month')
    plt.ylabel('Books completed')
    plt.grid(True, axis='y', alpha=0.3)
    plt.xticks(rotation=45, ha='right')
    plt.show()

def plot_genre_distribution(genres: dict[str, int]) -> None:
    plt.bar(list(genres.keys()), list(genres.values()))
    plt.title('Books per genre.')
    plt.xlabel('Genre')
    plt.ylabel('Books')
    plt.xticks(rotation=45, ha='right')

    plt.show()

def plot_rating_distribution(ratings: dict[str, int]) -> None:
    plt.pie(list(ratings.values()), labels=list(ratings.keys()))
    plt.title('Books rating distribution.')
    plt.xlabel('Rating')
    plt.ylabel('Books')

    plt.show()

def plot_reading_speed(pages_per_day: dict[str, int]) -> None:
    plt.bar(list(pages_per_day.keys()), list(pages_per_day.values()))
    plt.title('Book reading speed.')
    plt.xlabel('Book')
    plt.ylabel('pages per day')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.show()

if __name__ == '__main__':
    # Testing Code.
    month_count = book_per_month(load_books())
    ratings = rating_distribution(load_books())
    genres = genre_distribution(load_books())
    pages_per_day = reading_speed(load_books())
    # plot_books_per_month(month_count)
    # plot_genre_distribution(genres)
    plot_rating_distribution(ratings)
    # plot_reading_speed(pages_per_day)
