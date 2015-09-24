#!/usr/bin/python

from twisted.internet.protocol import Protocol,DatagramProtocol

class TransitTCPProtocol(Protocol):
	def __init__(self, factory):
		print 'init'
		self.factory = factory
		pass
	
	def dataReceived(self, data):
		data = data.strip()
		print data
		if (data == "" or data == None):
			print 'log here, data is not in logic'
			return
		type = data.split()[0]
		self.factory.handleEvent(type, data)
		pass
	
	def connectionMade(self):
		print 'connectionMade'
		pass

	def connectionLost(self, reason):
		print 'connectionLost'
		pass

class TransitUDPProtocol(DatagramProtocol):
	def __init__(self, factory):
		self.factory = factory

	def datagramReceived(self, data, (host, port)):
		data = data.strip()
		print "received %r from %s:%d" % (data, host, port)
		if (data == "" or data == None):
			print 'log here, data is not in logic'
			return
		type = data.split()[0]
		self.factory.handleEvent(type, data)
		pass
