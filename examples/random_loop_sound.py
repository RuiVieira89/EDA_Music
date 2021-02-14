
#!C:\Users\vieir\Anaconda3\envs\tf\python.exe

# looping music with randomly generated notes (within a whole step range)

from pyo import  *
import random

import time

notes = [130.81, 146.84, 164.81, 185.0, 207.66, 233.08, 261.62, 293.66, 
         329.63, 370.0, 415.3, 466.18, 523.25, 587.31, 659.25, 739.99, 
         830.63, 932.32, 1046.5, 1174.7, 1318.5, 1480.0, 1661.3, 1864.6, 
         2093.0]
white_keys = [130.81, 146.84, 164.81, 174.62, 195.99, 220.0, 246.94, 
              261.62, 293.66, 329.63, 349.23, 392.0, 440.0, 493.9, 
              523.25, 587.31, 659.25, 698.46, 783.99, 880.0, 987.8, 
              1046.5, 1174.7, 1318.5, 1397.0, 1567.9, 1760.0, 1975.6, 
              2093.0]

s = Server(sr=44000,buffersize=256).boot()

a = SuperSaw(freq=0, mul=.4)
b = SuperSaw(freq=0, mul=.1)

chor = Chorus(a)
dist = Disto(b)

compA = Compress(a).mix(2)
compB = Compress(b).mix(2)

revA = Freeverb(a, size=1, bal=1).out()
revB = Freeverb(b, size=.75, bal=1).out()

s.start()

h = 0
while h < 4:
	
	i = 0
	while i < 8:
		x = random.randrange(8,17)
		a.freq = white_keys[x]

		j = x
		k = 0
		while k < 2:
			print(j)
			b.freq = white_keys[j]
			time.sleep(.15)

			j -= 2
			b.freq = white_keys[j]
			time.sleep(.225)

			j += 1
			b.freq = white_keys[j]
			time.sleep(.15)

			k += 1

		m = j
		a.freq = white_keys[m]
		while m < (j+4):
			b.freq = white_keys[m]
			time.sleep(.15)
			m += 1
		i += 1

		i = 0
	while i < 8:
		x = random.randrange(8,17)
		a.freq = white_keys[x]

		j = x
		k = 0
		while k < 2:
			print(j)
			b.freq = white_keys[j]
			time.sleep(.15)

			j -= 2
			b.freq = white_keys[j]
			time.sleep(.225)

			j += 1
			b.freq = white_keys[j]
			time.sleep(.15)

			k += 1

		m = j
		a.freq = white_keys[m]
		while m < (j+4):
			b.freq = white_keys[m]
			time.sleep(.15)
			m += 1
		i += 1


time.sleep(1.2)

s.stop()
