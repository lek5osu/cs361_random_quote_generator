import random
import sqlite3


def init_used_quote_db():
    """
    Initializes/create db to store used quotes. Allows microservice cycle through the list of quotes once
    before repeating quotes.
    """
    connection = sqlite3.connect('quotes.db')
    cursor = connection.cursor()
    cursor.execute \
        ('''
            CREATE TABLE IF NOT EXISTS used_quotes (
                id INTEGER PRIMARY KEY,
                category TEXT NOT NULL,
                quote TEXT NOT NULL
            )
        ''')
    connection.commit()
    connection.close()


def add_used_quote(category, quote):
    """
    Method adds the randomly selected quote to db
    """
    connection = sqlite3.connect('quotes.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO used_quotes (category, quote) VALUES (?, ?)', (category, quote))
    connection.commit()
    connection.close()


def get_used_quotes(category):
    """
    Method retrieves db of used quotes
    """
    connection = sqlite3.connect('quotes.db')
    cursor = connection.cursor()
    cursor.execute('SELECT quote FROM used_quotes WHERE category = ?', (category,))
    quotes = [row[0] for row in cursor.fetchall()]
    connection.close()
    return quotes


def clear_used_quotes(category):
    """
    method clears db of quotes under category
    """
    connection = sqlite3.connect('quotes.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM used_quotes WHERE category = ?', (category,))
    connection.commit()
    connection.close()


class QuoteGenerator:
    def __init__(self):
        """
        initializes used_quotes_db and creates QuoteGenerator Object
        """
        self.quote_lists = {
            "inspirational": [
                "Be the person your dog thinks you are. - J.W. Stephens",
                "Make your bed to jumpstart your day and if your day sucks, at least you'll come home to a made bed.",
                "brother ugh..."
            ],
            "affirmation": [
                "Nice Work!",
                "Keep it Up!",
                "Good Job!"
            ],
            "movie": [
                "Magic Mirror on the wall, who is the fairest one of all? - Snow White",
                "I see dead people. - The Sixth Sense",
                "Just keep swimming. - Finding Nemo"
            ]
        }
        init_used_quote_db() # initiate db using sqlite 3. This is used to prevent duplicate quotes

    def generate_quote(self, category):
        """
        generates a random quote from quote_lists based on the category and writes it onto quote.txt file
        """
        if category not in self.quote_lists:
            return "Invalid category. Please enter 'inspirational', 'affirmation', or 'movie'."

        # Specify used vs available quotes using db.
        used_quotes = get_used_quotes(category)
        available_quotes = [quote for quote in self.quote_lists[category] if quote not in used_quotes]
        if not available_quotes:  # all quotes have been used, reset list
            clear_used_quotes(category)
            available_quotes = self.quote_lists[category]
            used_quotes = get_used_quotes(category)

        selected_quote = random.choice(self.quote_lists[category])
        while selected_quote in used_quotes:  # retrieve another quote if it's been used already
            selected_quote = random.choice(available_quotes)
        add_used_quote(category, selected_quote)

        with open("quote.txt", "w") as file:
            file.write(selected_quote)

        return selected_quote

if __name__ == "__main__":
    quote_generator = QuoteGenerator()
    result = quote_generator.generate_quote("affirmation")
    with open("quote.txt", "r") as file:
        quote = file.read()
    print(quote)