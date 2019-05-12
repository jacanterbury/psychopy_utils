
# Copyright (C) 2019 John A. Allen
# Distributed under the terms of the GNU General Public License (GPL).

"""Designed for debugging use, this logs messages into memory and only writes them to 
disk when close() is called (ie at a 'safe' time that does not jeopordise the experiment operation)
"""

class Logger:
	"""Wrapper class for logging"""


	"""Initialization of class"""
	def __init__(self, fname='.\logger.txt', mode='w', timestamp=False):
		from cStringIO import StringIO
		self.file_str=StringIO()
		self.file = open( fname, mode)
		self.timestamp = timestamp

		if self.timestamp:
			import time
			self.time=time


	def write(self,msg='Hello World!',nl=True):
		if nl:
			msg = msg + '\n'
		if self.timestamp:
			msg = str('%.3f' % self.time.time()) + ':, ' + msg	# log to 3dp ie milliseconds
		self.file_str.write( msg)

	
	def close(self):
		if self.timestamp:
			self.write('Closing')

		self.file.write(self.file_str.getvalue() )
		self.file.close()


			
