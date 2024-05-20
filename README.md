# Random Quote Generator

# Description
This program is a microservice I implemented for my CS 361 Software Engineering I class. This microservice returns a 
randomly selected string containing a quote that is catagorized as "inspirational", "affirmation", "movie". This microservice uses the client's local file system to make requests and receive responses.
## Communication Contract

### How to request data from this microservice
To request data from this microservice, the rng_quote_gen_microservice.py file containing the microservice must be placed in the same directory as the main
program. To place a request, the rng_quote_gen_microservice module must be imported into the main program. Depending on the type of quote requested, the function and be imported and called
as such.
```
# In this example, a request for an affirmation is made


from rng_quote_gen_microservice import rng_affirmation_generator
rng_affirmation_generator()
```
The methods in the module can be called by the following:

* `rng_inspirational_quote_generator()` - This requests an inspirational quote.
* `rng_affirmation_generator()` - This requests an affirmational quote.
* `rng_movie_quote_generator()` - This requests a movie quote.

### How to receive data from the microservice
To receive data, a file read operation should be made on the file 'quote.txt' after the request function has been called.
```
with open("quote.txt", "r") as file:
    quote = file.read()

print(quote)
```
If multiple quotes are to be requested. The data must be received between each request and stored in unique variables as such:
```
rng_affirmation_generator()
with open("quote.txt", "r") as file:
    quote1 = file.read()

rng_affirmation_generator()
with open("quote.txt", "r") as file:
    quote2 = file.read()

print(quote1)
print(quote2)
```
if any error has occured in the module itself, a specific error messsage will be written in the quote.txt file instead.
### UML Sequence Diagram
![image](https://raw.githubusercontent.com/lek5osu/cs361_random_quote_generator/main/UML%20milestone%202.png)

