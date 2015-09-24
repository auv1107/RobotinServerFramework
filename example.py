#!/usr/bin/python

from robotin.server import Server
from robotin.protocol import TransitTCPProtocol, TransitUDPProtocol

server = Server('udp', 8007)
f = server.factory

@f.handler('m')
def m(data):
	print 'got a event - ' + data

server.listen()
