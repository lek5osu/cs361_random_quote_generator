# Random Quote Generator

# Description
This program is a microservice I implemented for my CS 361 Software Engineering I class. This microservice returns a 
randomly selected string containing a quote that is catagorized as "inspirational", "affirmation", "movie". This microservice uses the ZeroMQ to make requests and receive responses.
## Communication Contract

### How to request data from this microservice
To request data from this microservice, the client must set up a request socket to the server set up by the microservice. It is recommended to include the following method in the client for this purpose
```
import zmq
def request_quote(category):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    socket.send_string(category)
```
The 3 categories of quotes can be retrieved using the follwoing calls.

* `request_quote("inspirational")` - This requests an inspirational quote.
* `request_quote("affirmation")` - This requests an affirmational quote.
* `request_quote("movie")` - This requests a movie quote.

### How to receive data from the microservice
To receive data, the follwoing line of code should be implemented following the request:
```
message = socket.recv_string()
    
```
The requested quote will be assigned to the 'message variable'

if any error has occured in the module itself, a specific error messsage will be written in the quote.txt file instead.
### UML Sequence Diagram
![image]([https://raw.githubusercontent.com/lek5osu/cs361_random_quote_generator/main/updatedUML.png])

