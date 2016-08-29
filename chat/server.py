# -*- coding: utf-8 -*-

"""
"""
from asyncore import dispatcher
from asynchat import async_chat
import asyncore
import socket

NAME = "cug541"


class ChatServer(dispatcher):

    def __init__(self, port):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.sessions = []
        print "listen on port {}...".format(port)

    def handle_accept(self):
        conn, addr = self.accept()
        self.sessions.append(ChatSession(conn, self))
        print "connection from {}".format(addr[0])

    def disconnect(self, session):
        self.sessions.remove(session)

    def broadcast(self, line):
        for session in self.sessions:
            session.push(line + '\r\n')


class ChatSession(async_chat):

    def __init__(self, sock, server):
        async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator("\r\n")
        self.data = []
        self.push("welcome to {}\r\n".format(NAME))

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        self.server.broadcast(line)
        print line

    def handle_close(self):
        async_chat.handle_close(self)
        self.server.disconnect(self)


class CommandHandler:

    def unknow(self, session, cmd):
        session.push('Unknow command: {}\r\n'.format(cmd))

    def handle(self, session, line):
        if not line.strip(): return
        parts = line.split(' ', 1)
        cmd = parts[0]
        try:
            line = parts[1].strip()
        except IndexError:
            line = ''
        meth = getattr(self, 'do_' + cmd, None)
        try:
            meth(session, line)
        except TypeError:
            self.unknow(session, cmd)


class Room(CommandHandler):

    def __init__(self, server):
        self.server = server
        self.sessions = []

    def add(self, session):
        self.sessions.append(session)

    def remove(self, session):
        self.sessions.remove(session)

    def broadcase(self, line):
        for session in self.sessions:
            session.push(line)

    def do_logout(self, session, line):
        raise EndSession


class EndSession(Exception):
    pass


if __name__ == '__main__':
    s = ChatServer(5005)
    asyncore.loop()
