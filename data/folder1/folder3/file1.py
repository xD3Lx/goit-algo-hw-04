import queue
import random

queue = queue.Queue()

def generate_request():
    # Create new request with random id
    request_id = random.randint(1, 1000)
    print(f"Request created: {request_id}")
    # Add request to the queue
    queue.put(request_id)


def process_request():
    if not queue.empty():
        # Handle and delete request from queue
        request_id = queue.get()
        print(f"Request has been processed: {request_id}")
    else:
        print("Queue is empty")


if __name__ == '__main__':
    try:
        while True:
            generate_request()
            process_request()

    except KeyboardInterrupt:
        # Handle user exiting the program
        print("\nExiting...")

