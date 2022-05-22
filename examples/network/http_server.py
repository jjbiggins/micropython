try:
    import usocket as socket
except:
    import socket


CONTENT = b"""\
HTTP/1.0 200 OK

Hello #%d from MicroPython!
"""


def main(micropython_optimize=False):
    s = socket.socket()

    # Binding to all interfaces - server will be accessible to other hosts!
    ai = socket.getaddrinfo("0.0.0.0", 8080)
    print("Bind address info:", ai)
    addr = ai[0][-1]

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    print("Listening, connect your browser to http://<this_host>:8080/")

    counter = 0
    while True:
        res = s.accept()
        client_sock = res[0]
        client_addr = res[1]
        print("Client address:", client_addr)
        print("Client socket:", client_sock)

        client_stream = (
            client_sock
            if micropython_optimize
            else client_sock.makefile("rwb")
        )

        print("Request:")
        req = client_stream.readline()
        print(req)
        while True:
            h = client_stream.readline()
            if h in [b"", b"\r\n"]:
                break
            print(h)
        client_stream.write(CONTENT % counter)

        client_stream.close()
        if not micropython_optimize:
            client_sock.close()
        counter += 1
        print()


main()
