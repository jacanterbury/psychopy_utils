Helper library file to allow for (virtually) non-invasive logging of messages during runtime


##Logger  library

Ensure that your experiment has the kent_psylog.py file included in the same directory as your PsychoPy program file.
Then add a code block and in the "Begin Experiment" part, and insert the following lines of:

	from kent_psylog import *
	logger = Logger(name='.\logger.txt', timestamp=True)

name:
filename to save results into

timestamp:
If True then a timestamp is prepended to each message.

To log a message insert something similar to the following:

	logger.write(msg="my message here", nl=True)
	
nl:
If False then the current message is appended to the end of the previous one on the same text line.


To write all the previous messages to disk, call close() at a non time-sensitive point in the experiment.

	logger.close()
	
Any problems - please contact psychsupport@kent.ac.uk