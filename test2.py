#!/usr/bin/env python

# test2.py

i = int(raw_input('net interest:'))

overhead = 0

if i > 10:
	overhead = 1
	if i > 20:
		overhead = overhead + 10 * .075
		if i > 40:
			overhead = overhead + 20 * .05
			if i > 60:
				overhead = overhead + 20 *.03
				if i > 100:
					overhead = overhead + 40 * .015
					overhead = overhead + (i-100) * .01
				else :
					overhead = overhead + (i-60) * .015
			else :
				overhead = overhead + (i-40)* .03
		else :
			overhead = overhead + (i-20)* .05
	else :
		overhead = overhead + (i-10)* .075
else : 
	overhead = i*.1
	
print overhead