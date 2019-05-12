
# Copyright (C) 2019 John A. Allen
# Distributed under the terms of the GNU General Public License (GPL).

class PPTrigger:
	"""Wrapper class for calling parallel triggers in code for PsychoPy

	"""
	status = False 		# IFalse allows for testing on machines without parallel ports
	address = 0xE010 	# this is generally overridden at runtime

	
	def __init__(self, win, address, status=True):
		"""Initialization of class with address required
		"""
		#Populate defaults
		self.status = status
		self.address = address
		self.win = win

		#Initialize parallel port if required
		if self.status == True:
			#Pull in library if we're not in test mode
			from psychopy import parallel
			self.parallel = parallel
			#Set the address
			self.parallel.setPortAddress(self.address)
			#Clear it right away
			self.clear()

	
	def fire(self,trigger,flip=True):
		"""Function to fire the trigger
		"""
		#Are we calling this trigger on a flip? See PsychoPy docs for explanation of 'flip'
		if flip == True:
			self.win.callOnFlip(self.mainFire, trigger=trigger)
		else:
			#Nope - just fire.
			self.mainFire(trigger=trigger)
	
	
	def mainFire(self, trigger):
		"""Fires trigger, but defined to use as a callback on fire function
		"""
		if self.status == True:
			self.parallel.setData(trigger)
			
	def clear(self,trigger=0):
		"""Wrapper function to fire a clearing trigger ... 
		
		can override if needs to be different to 0
		"""
		self.mainFire(trigger)
		


