from rng_quote_gen_microservice import rng_affirmation_generator
import os

try:
    # Call random quote generator
    success = "t"
    success = rng_affirmation_generator()
except Exception as e:
    print(f"An error occurred in rng_affirmation_generator(): {e}")
    # Remove the quote file if it exists and an error occurred
    if os.path.exists("quote.txt"):
        os.remove("quote.txt")
if success != "f":
    # Read the generated quote from the text file
    try:
        with open("quote.txt", "r") as file:
            quote = file.read()
        print(quote)
    except Exception as e:
        print(f"An error occurred while reading the quote file: {e}")
else:
    # Remove the quote file if it exists and an error occurred
    if os.path.exists("quote.txt"):
        os.remove("quote.txt")




