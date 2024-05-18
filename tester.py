# tester
from rng_quote_gen_microservice import QuoteGenerator
def rng_affirmation_generator():
    """
    The method returns a randomly chosen affirmation from the library of affirmations.
    """
    # Create an instance of the QuoteGenerator
    quote_generator = QuoteGenerator()

    # Generate a quote based on category, quote will be written in a file called "quote.txt" in your directory
    result = quote_generator.generate_quote("affirmation")

    # Read the generated quote from the text file
    with open("quote.txt", "r") as file:
        quote = file.read()
    return quote

if __name__ == "__main__":
    print(rng_affirmation_generator())




