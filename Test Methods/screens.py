#!/usr/bin/env python
#screens.py

from AppKit import *

class Screens(object):
	def __init__(self):
		self.numScreens = 0
		self.coordinates = []
		self.totalWidth = 0
		self.totalHeight = 0
		self.verticalLines = []
		self.horizontalLines = []

	def __repr__(self):
		return "Screen coordinates: " + str(self.coordinates) + "\nWidth: " +\
				str(self.totalWidth) + "\nHeight: " + str(self.totalHeight)
	
	def setup(self):
		screens = NSScreen.screens()
		self.numScreens = len(screens)
		tops, bottoms, lefts, rights = [], [], [], []
		for s in screens:
			top, bottom, left, right = self.parseScreen(s, tops, bottoms, lefts, rights)
		self.totalWidth = max(rights) - min(lefts)
		self.totalHeight = max(tops) - min(bottoms)
		self.cleanCoordinates()
		self.makeLines()
	
	def parseScreen(self, screen, tops, bottoms, lefts, rights):
		rect = screen.frame()
		origin = rect.origin
		size = rect.size
		top = origin.y + size.height
		bottom = origin.y
		left = origin.x
		right = origin.x + size.width
		self.coordinates.append((top, left))
		self.coordinates.append((top, right))
		self.coordinates.append((bottom, right))
		self.coordinates.append((bottom, left))
		tops.append(top)
		bottoms.append(bottom)
		lefts.append(left)
		rights.append(right)
		return (top, bottom, left, right)
	
	def cleanCoordinates(self):
		clean = []
		for c in self.coordinates:
			matches = 0
			for co in self.coordinates:
				if c == co:
					matches += 1
			if matches == 1:
				clean.append(c)
		self.coordinates = clean
	
	def makeLines(self):
		for c in self.coordinates:
			print str(c[0]) + " " + str(c[1])
	
	def posInScreen(self, posx, posy):
		posx = 0 if posx < 0 else posx
		posx = SCREENWIDTH if posx > SCREENWIDTH else posx
		posy = 0 if posy < 0 else posy
		posy = SCREENHEIGHT if posy > SCREENHEIGHT else posy