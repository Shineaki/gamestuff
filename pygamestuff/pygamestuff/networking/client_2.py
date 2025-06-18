import socket
import threading

# --- main ---

all_threads = []


def client(idx: int, s: socket.socket):
    print("Connected to the server")
    i = 0
    while i < 1000:
        i += 1
        message = "Hello"
        print("idx:", idx, "send:", message)
        message = message.encode()
        s.send(message)

        message = s.recv(1024)
        message = message.decode()
        print("idx:", idx, "recv:", message)


try:
    for i in range(5):
        host = "0.0.0.0"
        port = 8081

        s = socket.socket()
        s.connect((host, port))

        t = threading.Thread(target=client, args=[i, s])
        t.start()

        all_threads.append(t)
except KeyboardInterrupt:
    print("Stopped by Ctrl+C")
finally:
    if s:
        s.close()
    for t in all_threads:
        t.join()
