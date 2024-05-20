from rng_quote_gen_microservice import rng_affirmation_generator

# Call random quote generator
rng_affirmation_generator()
try:
    with open("quote.txt", "r") as file:
        quote = file.read()
        print(quote)

except IOError as e:
    print(f"An error occurred while reading the file: {e}. Retrying in 3 seconds...")








