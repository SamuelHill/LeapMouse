from AppKit import *
screens = NSScreen.screens()
for s in screens:
	rect = s.frame()
	origin = rect.origin
	size = rect.size
	print "x: {} y: {}".format(origin.x, origin.y)
	print "width: {} height: {}".format(size.width, size.height)
	print ""