import socket
import pickle
import random
import datetime

PORT = 9000

IP = socket.gethostname()


class File:
    def __init__(self):
        self.__liste = []

    def __str__(self):
        return str(self.__liste)

    def file_vide(self):
        return self.__liste == []

    def enfile(self, val):
        self.__liste.append(val)

    def defile(self):
        return self.__liste.pop(0)

    def premier(self):
        return self.__liste[0]

    def taille(self):
        return len(self.__liste)


def get_uuid():
    uuid = random.randint(1000, 9999)
    with open('../static/nums.txt', 'r+') as f:
        while True:
            if not str(uuid) in f.read():
                f.write(f"{uuid}\n")
                return str(uuid)


def send(content):
    now = datetime.datetime.now()

    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_socket.connect((IP, PORT))

    string = "P#"
    string += '%02d:%02d:%02d' % (now.hour, now.minute, now.second)
    string += f' - {content}'

    c_socket.send(string.encode())
    print(f"Sent {string} to server")

    c_socket.close()


def get_server_update():
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    c_socket.connect((IP, PORT))
    c_socket.send("G#".encode())

    ping = c_socket.recv(1024)

    c_socket.close()

    return pickle.loads(ping)
