import zmq

def request_quote(category):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    socket.send_string(category)
    message = socket.recv_string()
    print(f"Received reply: {message}")

if __name__ == "__main__":
    request_quote("inspirational")
    request_quote("affirmation")
    request_quote("movie")
