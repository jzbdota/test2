#!/usr/bin/env python

# test2.py

i = int(raw_input('net interest:'))

arr = [100, 60, 40, 20, 10, 0]
rat = [.01, .015, .03, .05, .075, .1]
r = 0
for idx in range(0,6):
	if i >arr[idx]:
		r+=(i-arr[idx])*rat[idx]
		i=arr[idx]
		
print r