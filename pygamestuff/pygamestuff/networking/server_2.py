import socket
import threading
import time

# --- functions ---


def handle_client(conn, addr):
    print("[thread] starting")

    # recv message
    i = 0
    while i < 1000:
        i += 1
        message = conn.recv(1024)
        message = message.decode()
        print("[thread] client:", addr, "idx:", i, "recv:", message)

        # simulate longer work
        # time.sleep(5)

        # send answer
        message = "Bye!"
        message = message.encode()
        conn.send(message)
        print("[thread] client:", addr, "send:", message)

        # conn.close()

        # print("[thread] ending")


# --- main ---

host = "0.0.0.0"
port = 8081

s = socket.socket()
s.setsockopt(
    socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
)  # solution for "[Error 89] Address already in use". Use before bind()
s.bind((host, port))
s.listen(1)

all_threads = []

try:
    while True:
        print("Waiting for client")
        conn, addr = s.accept()

        print("Client:", addr)

        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.start()

        all_threads.append(t)
except KeyboardInterrupt:
    print("Stopped by Ctrl+C")
finally:
    if s:
        s.close()
    for t in all_threads:
        t.join()
