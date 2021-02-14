#!C:\Users\vieir\Anaconda3\envs\tf\python.exe

# Musical/graphical representation of a selection sort algorithm.
# The musical patterns generated can be manipulated by altering the time.sleep
# values and seeding the algorithm with different lists to be sorted.
# This list was generated using nested for loops, but can be substituted
# with a randomly generated list to create a drastically different sound.
# This is a work of slow-cooked eggplant brought to you by Benjamin Flores straight from 2015.

from pyo import  *
import random

import time

sortlist = [12, 8, 16, 24, 23, 22, 21, 17, 24, 23, 22, 21, 18, 24, 23, 
            22, 21, 19, 24, 23, 22, 21, 7, 16, 24, 23, 22, 21, 17, 24, 
            23, 22, 21, 18, 24, 23, 22, 21, 19, 24, 23, 22, 21, 6, 16, 
            24, 23, 22, 21, 17, 24, 23, 22, 21, 18, 24, 23, 22, 21, 19, 
            24, 23, 22, 21, 5, 16, 24, 23, 22, 21, 17, 24, 23, 22, 21, 
            18, 24, 23, 22, 21, 19, 24, 23, 22, 21, 13, 8, 16, 24, 23, 
            22, 21, 17, 24, 23, 22, 21, 18, 24, 23, 22, 21, 19, 24, 23, 
            22, 21, 7, 16, 24, 23, 22, 21, 17, 24, 23, 22, 21, 18, 24, 
            23, 22, 21, 19, 24, 23, 22, 21, 6, 16, 24, 23, 22, 21, 17, 
            24, 23, 22, 21, 18, 24, 23, 22, 21, 19, 24, 23, 22, 21, 5, 
            16, 24, 23, 22, 21, 17, 24, 23, 22, 21, 18, 24, 23, 22, 21, 
            19, 24, 23, 22, 21, 14, 8, 16, 24, 23, 22, 21, 17, 24, 23, 
            22, 21, 18, 24, 23, 22, 21, 19, 24, 23, 22, 21, 7, 16, 24, 
            23, 22, 21, 17, 24, 23, 22, 21, 18, 24, 23, 22, 21, 19, 24, 
            23, 22, 21, 6, 16, 24, 23, 22, 21, 17, 24, 23, 22, 21, 18, 
            24, 23, 22, 21, 19, 24, 23, 22, 21, 5, 16, 24, 23, 22, 21, 
            17, 24, 23, 22, 21, 18, 24, 23, 22, 21, 19, 24, 23, 22, 21, 
            15, 8, 16, 24, 23, 22, 21, 17, 24, 23, 22, 21, 18, 24, 23, 
            22, 21, 19, 24, 23, 22, 21, 7, 16, 24, 23, 22, 21, 17, 24, 
            23, 22, 21, 18, 24, 23, 22, 21, 19, 24, 23, 22, 21, 6, 16, 
            24, 23, 22, 21, 17, 24, 23, 22, 21, 18, 24, 23, 22, 21, 19, 
            24, 23, 22, 21, 5, 16, 24, 23, 22, 21, 17, 24, 23, 22, 21, 
            18, 24, 23, 22, 21, 19, 24, 23, 22, 21]

def selection(a):

	white_keys = [130.81, 146.84, 164.81, 174.62, 195.99, 220.0, 246.94, 
               261.62, 293.66, 329.63, 349.23, 392.0, 440.0, 493.9, 
               523.25, 587.31, 659.25, 698.46, 783.99, 880.0, 987.8, 
               1046.5, 1174.7, 1318.5, 1397.0, 1567.9, 1760.0, 1975.6, 
               2093.0]

	s = Server(sr=44000,buffersize=256).boot()
	iSaw = Sine(freq=0, mul=.1)
	jSaw = Sine(freq=0, mul=.15)
	revI = Freeverb(iSaw, size=1, bal=1).out()
	revJ = Freeverb(jSaw, size=.75, bal=1).out()

	s.start()

	i = 0
	while i < len(a):

		lowest = a[i]
		lowest_position = i

		j = i
		while j < len(a):

			if a[j] < lowest:

				lowest = a[j]

				print('>>'*a[j])
				jSaw.freq = white_keys[a[j]]
				time.sleep(.5)

				lowest_position = j
				j += 1

			else:

				print('##'*a[j])
				iSaw.freq = white_keys[a[i]]
				time.sleep(.00005)

				j += 1
				
		a[lowest_position] = a[i]
		a[i] = lowest
		i += 1

	s.stop()

	return a

print(selection(sortlist))
