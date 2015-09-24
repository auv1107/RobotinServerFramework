#!/usr/bin/python

from protocol import TransitTCPProtocol, TransitUDPProtocol
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

class TransitFactory(Factory):
	def __init__(self):
		self._handlers = dict()

	def buildProtocol(self, addr):
		return TransitTCPProtocol(self)

	def buildUdpProtocol(self):
		return TransitUDPProtocol(self)

	def handleEvent(self, type, data):
		if (self._handlers.has_key(type)):
			self._handlers[type](data)

	def handler(self, type):
		def wrapper(func):
			if not callable(func):
				raise ValueError("{} is not callable".format(func))
			if (type != "" and type != None):
				self._handlers[type] = func
			return func
		return wrapper

class Server:
	def __init__(self, t, port):
		if ('tcp' == t.lower()):
			self._type = 'tcp'
		elif ('udp' == t.lower()):
			self._type = 'udp'
		else:
			raise "Unknown socket type"

		if not (type(port) == int and port > 0):
			raise "port should be a Integer and greater than 0"
		self._port = port

		self.factory = TransitFactory()
		pass

	def listen(self):
		if (self._type == 'tcp'):
			endpoint = TCP4ServerEndpoint(reactor, self._port)
			endpoint.listen(self.factory)

		if (self._type == 'udp'):
			reactor.listenUDP(self._port, self.factory.buildUdpProtocol())
	
		reactor.run()
