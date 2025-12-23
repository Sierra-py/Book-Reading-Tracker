# Book Reading Tracker
A simple Command Line Application to track the books you have read; see your reading statistics and their visualization.

## Features
- **Add book**: Add the book you've read to your library
- **See Statistics**: View your reading metrics - books per month, genre breakdown, reading speed, and more
- **See Visualization**: Display graphs of your reading metrics for better insights
- **Saves JSON file**: All your books are saved automatically in a JSON file

## Installation
```bash
git clone https://github.com/Sierra-py/Book-Reading-Tracker.git
cd Book-Reading-Tracker
pip install -r requirements.txt
```

## Usage

Run the program:
```bash
python main.py
```

Menu options:
1. **Show All Books** - View your complete library
2. **Add A Book** - Add a new book with title, author, dates, rating, pages
3. **Show Analytics** - View reading statistics (books per month, genre breakdown, average pages, reading speed)
4. **Show Visualizations** - Display charts for your reading data
5. **Exit** - Save and quit

## Example

After adding books, analytics will show:
- Books completed per month
- Average pages per book
- Genre distribution
- Rating distribution (5, 4+, 3+, 2+, 1+)
- Reading speed (pages per day)

Visualizations include bar charts and pie charts for each metric.