from rng_quote_gen_microservice import rng_affirmation_generator

# Call random quote generator/ requesting data from the microservice
rng_affirmation_generator()

# receiving data from the microservice
try:
    with open("quote.txt", "r") as file:
        quote = file.read()
        print(quote)

except IOError as e:
    print(f"An error occurred while reading the file: {e}. Retrying in 3 seconds...")








    try:
        rng_affirmation_generator()
        #  File read operation with validation and delay
        while True:
            try:
                with open("quote.txt", "r") as file:
                    quote = file.read()
                    print(quote)
                    break
            except IOError as e:
                print(f"An error occurred while reading the file: {e}. Retrying in 3 seconds...")
                time.sleep(3)

    except Exception as e:
        print(f"An error occurred creating Random Quote Generator object: {e}")
        while True:
            try:
                with open("quote.txt", "w") as file:
                    file.write(e)
                break
            except IOError as e:
                print(f"An error occurred while writing to the file: {e}. Retrying in 3 seconds...")
                time.sleep(3)
            try:
                with open("quote.txt", "r") as file:
                    quote = file.read()
                    print(quote)
                    break
            except IOError as e:
                print(f"An error occurred while reading the file: {e}. Retrying in 3 seconds...")
                time.sleep(3)