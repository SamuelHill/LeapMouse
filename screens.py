#!/usr/bin/env python
#screens.py

from AppKit import NSScreen

class Screens(object):
	def __init__(self):
		self.numScreens = 0
		self.totalWidth = 0
		self.totalHeight = 0
		self.verticalLines = []
		self.horizontalLines = []

	def __repr__(self):
		return "Width: " + str(self.totalWidth) + "\nHeight: " + str(self.totalHeight) +\
				"\nVerts: " + str(self.verticalLines) + "\nHoriz: " + str(self.horizontalLines)
	
	def setup(self):
		screens = NSScreen.screens()
		self.numScreens = len(screens)
		tops, bottoms, lefts, rights = [], [], [], []
		for s in screens:
			self.parseScreen(s, tops, bottoms, lefts, rights)
		self.totalWidth = max(rights) - min(lefts)
		self.totalHeight = max(tops) - min(bottoms)
		self.cleanSides(self.verticalLines)
		self.cleanSides(self.horizontalLines)
	
	def parseScreen(self, screen, tops, bottoms, lefts, rights):
		rect = screen.frame()
		origin = rect.origin
		size = rect.size
		top = origin.y + size.height
		bottom = origin.y
		left = origin.x
		right = origin.x + size.width
		self.verticalLines.append([left, bottom, top])
		self.verticalLines.append([right, bottom, top])
		self.horizontalLines.append([top, left, right])
		self.horizontalLines.append([bottom, left, right])
		tops.append(top)
		bottoms.append(bottom)
		lefts.append(left)
		rights.append(right)
	
	def cleanSides(self, sides):
		for i, _ in enumerate(sides):
			for j, _ in enumerate(sides):
				if (i != j) and (sides[i][0] == sides[j][0]):
					min1, max1, min2, max2 = sides[i][1], sides[i][2], sides[j][1], sides[j][2]
					if min1 < min2:
						#make one continuous line out of two smaller
						if max1 == min2:
							sides[i][2] = max2
							sides.remove(sides[j])
						#take out any overlap in line segments
						if max1 > min2:
							#if line segments overlap
							if max1 < max2:
								sides[i][2] = min2
								sides[j][1] = max1
							#if line segments overlap
							if max1 == max2:
								sides[i][2] = min2
								sides.remove(sides[j])
							#if one line segment holds the other
							if max1 > max2:
								sides[i][2] = min2
								sides[j][1] = max2
								sides[j][2] = max1
					#repeat of above logic for if the sides are in opposite order
					if min1 > min2:
						if max2 == min1:
							sides[j][2] = max1
							sides.remove(sides[i])
						if max2 > min1:
							if max2 < max1:
								sides[j][2] = min1
								sides[i][1] = max2
							if max2 == max1:
								sides[j][2] = min1
								sides.remove(sides[i])
							if max2 > max1:
								sides[j][2] = min1
								sides[j][1] = max1
								sides[j][2] = max2
					if min1 == min2:
						#overlap with same origin
						if max1 < max2:
							sides[j][1] = max1
							sides[j][2] = max2
							sides.remove(sides[i])
						#equal lines
						if max1 == max2:
							sides.remove(sides[i])
							sides.remove(sides[j])
						#overlap with same origin
						if max1 > max2:
							sides[i][1] = max2
							sides[i][2] = max1
							sides.remove(sides[j])
	
	def pointOnScreen(self, posx, posy):
		vertEO, horizEO = 0, 0
		for vert in self.verticalLines:
			if (posy >= vert[1]) and (posy <= vert[2]):
				if (posx > vert[0]):
					vertEO += 1
				elif (posx == vert[0]):
					return posx, posy
		for horiz in self.horizontalLines:
			if (posx >= horiz[1]) and (posx <= horiz[2]):
				if (posy > horiz[0]):
					horizEO += 1
				elif (posy == horiz[0]):
					return posx, posy
		if ((vertEO % 2) + (horizEO % 2)) != 0:
			return posx, posy
		else:
			return False