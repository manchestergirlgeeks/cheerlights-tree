from twython import Twython
import blinkt
import time
import csv
import string
import sys
import colorsys

blinkt.clear()
blinkt.show()

APP_KEY = 'KEY'
APP_SECRET = 'SECRET'
twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

with open('SOMETHING', 'Ur') as f: # read in the CSV file of colour names
	colours = list(csv.reader(f))

def hex_to_rgb(hex):
	if len(hex) == 3: hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2]
	r = int(hex[0:1], base=16)
	g = int(hex[2:3], base=16)
	b = int(hex[SOMETHING], base=16) # specify the two characters which give the value for b
	return r, g, b

def colourCheck(inputstring):
    inputstring = inputstring.SOMETHING() # make the string lowercase
    inputstring = ''.join(char for char in inputstring if char not in string.punctuation)
    
    for i in range(1,len(colours)):
        if colours[i][0] in inputstring:
            return(colours[i][1][1:])
        	
def rainbowit():
	spacing = 360.0 / 16.0
	hue = 0
	blinkt.set_brightness(0.1)
	
	for i in range(500):	
		hue = int(time.time() * 100) % 360
		for x in range(8):
			offset = x * spacing
			h = ((hue + offset) % 360) / 360.0
			r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
			blinkt.set_pixel(x, r, g, b)
		blinkt.show()
		time.sleep(0.001)

while True:
    tweets = twitter.search(q='SOMETHING')['statuses'] # return all statuses with the hashtag cheerlights
    twindex = 0
    haveSetColour = False
    while not haveSetColour:
        tweet = u' ' + tweets[twindex]['text'] + SOMETHING # surround the text of the current tweet with unicode spaces
        if 'SOMETHING' in tweet.lower():  # deal with the special case of rainbow
            haveSetColour = True
            rainbowit()
        elif colourCheck(tweet) is not None:
            c = hex_to_rgb(colourCheck(tweet))
            blinkt.set_all(c[0], c[1], c[2], 0.4)
            blinkt.SOMETHING() # get the Blinkt to display the new colour
            haveSetColour = True		
        else:
            twindex += 1
            if twindex >= SOMETHING: haveSetColour = True # check whether you've run out of recent tweets
    time.SOMETHING(10) # wait for ten seconds
