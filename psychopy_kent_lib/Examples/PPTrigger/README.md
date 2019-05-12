Helper library file to offer parallel port functions


##Parallel fire library

Ensure that your experiment has the kent_psylib.py file included in the same directory as your PsychoPy program file.
Then add a code block and in the "Begin Experiment" part, and insert the following lines of:

	from kent_psylib import *
	pp = PPTrigger(win,address=0xE010,status=True)

win:
win is a PsychoPy variable, DO NOT change this

address:
Change address to your parallel address to that of the lab machine that you will be using.
On a Windows PC this can be found as follows:
- Control Panel
- Device Manager
- Expand the 'Ports (COM & LPT)' section
- Select the entry for your parallel port and then click on the 'Resources' tab.
- Use the first part of the 'Setting' for the first entry in the list. This will be four hexadecimal digits. e.g. E010 but prefix it with '0x' as per above.

statusL
If you wish to just test your script on a computer without a parallel port, then set status to "False"	

	
Then in your subsequent code blocks, you can fire a trigger e.g. by:

	pp.fire(trigger=255, flip=True)

trigger:
The trigger value can be in the range 0-255. It represents the total of an 8 bit binary number so
1 sets pin 1 (e.g. digital channel 1 on Biopac)
2 sets pin 2
4 sets pin 3
8 sets pin 4
16 sets pin 5
32 sets pin 6
64 sets pin 7
128 sets pin 8

For systems such as BIOPAC a combined value such as 129 would send a trigger pulse on channels 1 and 8 (129=128+1)

For other systems such as BrainVision EEG systems the trigger code is read as a single number in the range 1-255
Note that a value of 0 (zero) turns off all digital digital channels and this is what pp.clear() does (see below).

flip:
setting flip to True (the default value) will DELAY sending the trigger pulse until the next time the monitor frame is updated. This is normally what is needed for typical stimulus presentation experiments.


Make sure that you clear your trigger at some point before you want to send the next pulse. 
The 'End routine' tab on the code block is usually a suitable place to do this.

	pp.clear()
	
Any problems - please contact psychsupport@kent.ac.uk