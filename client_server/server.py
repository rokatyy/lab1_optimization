"""
В файле содержится информация о беспилотных летательных аппаратах:
Наименование	|   Крейсерская скорость (км/ч)  |	Продолжительность полета (мин)
Разработать
программу, позволяющую получить характеристики по наименованию;
список БПЛА, способных достичь цели, находящейся на заданном расстоянии, не более чем за 10 минут.
Предусмотреть корректный ответ сервера при отсутствии требуемой информации.
"""

from pandas import read_csv
import socket
from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineOnlyReceiver


def get_data_from_file(file_path):
    """
    This method returns data from file
    Args:
        file_path (str) - full file path
    Returns:
        data (DataFrame object)
    """
    data = read_csv(file_path)
    return data


class ChatProtocol(LineOnlyReceiver):
    name = ""

    def getName(self):
        if self.name != "":
            return self.name
        return self.transport.getPeer().host

    def connectionMade(self):
        print("New connection from " + self.getName())
        self.sendLine(b"Welcome to my my chat server.")
        self.sendLine(b"Send '/NAME [new name]' to change your name.")
        self.sendLine(b"Send '/EXIT' to quit.")
        self.factory.clientProtocols.append(self)

    def connectionLost(self, reason):
        print(("Lost connection from " + self.getName()).encode('utf-8'))
        self.factory.clientProtocols.remove(self)

    def lineReceived(self, line):
        print(self.getName() + " said " + line)
        if line[:5] == "/NAME":
            oldName = self.getName()
            self.name = line[5:].strip()
            self.factory.sendMessageToAllClients((oldName + " changed name to" + self.getName()).encode('utf-8'))
        elif line == "/EXIT":
            self.transport.loseConnection()
        else:
            self.factory.sendMessageToAllClients((self.getName() + " says " + line).encode('utf-8'))

    def sendLine(self, line):
        self.transport.write((line + "\r\n").encode('utf-8'))


class ChatProtocolFactory(ServerFactory):
    protocol = ChatProtocol

    def __init__(self):
        self.clientProtocols = []

    def sendMessageToAllClients(self, mesg):
        for client in self.clientProtocols:
            client.sendLine(mesg)


print("Starting Server")
factory = ChatProtocolFactory()
reactor.listenTCP(12345, factory)
reactor.run()
