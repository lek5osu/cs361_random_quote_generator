# tester
from rng_quote_gen_microservice import rng_affirmation_generator
# call random quote generator
rng_affirmation_generator()
# Read the generated quote from the text file
with open("quote.txt", "r") as file:
    quote = file.read()

print(quote)





