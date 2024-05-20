import random
import sqlite3
import time
import os
def init_used_quote_db():
    """
    Initializes/create db to store used quotes. Allows microservice cycle through the list of quotes once
    before repeating quotes.
    """
    try:
        connection = sqlite3.connect('quotes.db')
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS used_quotes (
                id INTEGER PRIMARY KEY,
                category TEXT NOT NULL,
                quote TEXT NOT NULL
            )
        ''')
        connection.commit()
    except Exception as e:
        print(f"An error occurred while initializing the used quotes database: {e}")
        return "f"

def add_used_quote(category, quote):
    """
    Method adds the randomly selected quote to db
    """
    try:
        connection = sqlite3.connect('quotes.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO used_quotes (category, quote) VALUES (?, ?)', (category, quote))
        connection.commit()
    except Exception as e:
        print(f"An error occurred while adding a used quote: {e}")
        return "f"


def get_used_quotes(category):
    """
    Method retrieves db of used quotes
    """
    try:
        connection = sqlite3.connect('quotes.db')
        cursor = connection.cursor()
        cursor.execute('SELECT quote FROM used_quotes WHERE category = ?', (category,))
        quotes = [row[0] for row in cursor.fetchall()]
        return quotes
    except Exception as e:
        print(f"An error occurred while retrieving used quotes: {e}")
        return []

def clear_used_quotes(category):
    """
    method clears db of quotes under category
    """
    try:
        connection = sqlite3.connect('quotes.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM used_quotes WHERE category = ?', (category,))
        connection.commit()
    except Exception as e:
        print(f"An error occurred while clearing used quotes: {e} Error prevents a new quote from generating.")


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
                "Good Job!",
                "You are amazing!",
                "You are awesome!"
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
        try:
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

            # File write operation with validation and delay
            while True:
                try:
                    with open("quote.txt", "w") as file:
                        file.write(selected_quote)
                    break
                except IOError as e:
                    print(f"An error occurred while writing to the file: {e}. Retrying in 3 seconds...")
                    time.sleep(3)

            return selected_quote
        except Exception as e:
            print(f"An error occurred while generating the quote: {e}")
            return "f'"

def rng_inspirational_quote_generator():
    """
    The method returns a randomly chosen affirmation from the library of affirmations.
    """
    try:
        # Create an instance of the QuoteGenerator
        quote_generator = QuoteGenerator()

        # Generate a quote based on category, quote will be written in a file called "quote.txt" in your directory
        result = quote_generator.generate_quote("inspirational")
    except Exception as e:
        print(f"An error occurred while generating an inspirational quote: {e}")
        return "f"

def rng_affirmation_generator():
    """
    The method returns a randomly chosen affirmation from the library of affirmations.
    """
    try:
        # Create an instance of the QuoteGenerator
        quote_generator = QuoteGenerator()

        # Generate a quote based on category, quote will be written in a file called "quote.txt" in your directory
        result = quote_generator.generate_quote("affirmation")
    except Exception as e:
        print(f"An error occurred while generating an affirmation: {e}")
        return "f"

def rng_movie_quote_generator():
    """
    The method returns a randomly chosen affirmation from the library of affirmations.
    """
    try:
        # Create an instance of the QuoteGenerator
        quote_generator = QuoteGenerator()

        # Generate a quote based on category, quote will be written in a file called "quote.txt" in your directory
        result = quote_generator.generate_quote("movie")
    except Exception as e:
        print(f"An error occurred while generating a movie quote: {e}")
        return "f"

if __name__ == "__main__":
    try:
        quote_generator = QuoteGenerator()
        if quote_generator != "f":
            result = quote_generator.generate_quote("affirmation")
            # File read operation with validation and delay
            while True:
                try:
                    with open("quote.txt", "r") as file:
                        quote = file.read()
                        print(quote)
                    break
                except IOError as e:
                    print(f"An error occurred while reading the file: {e}. Retrying in 3 seconds...")
                    time.sleep(3)
        else:
            # Remove the quote file if it exists and an error occurred
            if os.path.exists("quote.txt"):
                os.remove("quote.txt")
    except Exception as e:
        print(f"An error occurred creating Random Quote Generator object: {e}")