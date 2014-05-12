import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap
from Quartz import CGDisplayBounds
#from Quartz import CGGetOnlineDisplayList
from Quartz import CGMainDisplayID
import time

def mouseEvent(type, posx, posy):
        theEvent = CGEventCreateMouseEvent(
                    None, 
                    type, 
                    (posx,posy), 
                    kCGMouseButtonLeft)
        CGEventPost(kCGHIDEventTap, theEvent)

def mousemove(posx,posy):
        mouseEvent(kCGEventMouseMoved, posx,posy);

def mouseclick(posx,posy):
        #mouseEvent(kCGEventMouseMoved, posx,posy);
        mouseEvent(kCGEventLeftMouseDown, posx,posy)
        mouseEvent(kCGEventLeftMouseUp, posx,posy)

def main():
	controller = Leap.Controller()
	controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
	mainMonitor = CGDisplayBounds(CGMainDisplayID())
#	err, ids, count = CGGetOnlineDisplayList(10,None,None)
#	WIDTH = 0
#	HEIGHT = 0
#	for id in ids:
#		monitor = CGDisplayBounds(id)
#		WIDTH += monitor.size.width
#		HEIGHT += monitor.size.height
		
	FPS = 50
	FARLEFT = -300
	FARRIGHT = 300
	TOP = 500
	BOTTOM = 100
	BACKGROUND = -25
	SCREENWIDTH = mainMonitor.size.width
	SCREENHEIGHT = mainMonitor.size.height
	
	last_time = time.time()
	touched = False
	
	while True:
		new_time = time.time()
		sleep_time = ((1000.0 / FPS) - (new_time - last_time)) / 1000.0
		if sleep_time > 0:
			time.sleep(sleep_time)
		last_time = new_time
		frame = controller.frame()
		finger = frame.fingers.frontmost
		stabilizedPosition = finger.stabilized_tip_position
		interactionBox = frame.interaction_box
		normalizedPosition = interactionBox.normalize_point(stabilizedPosition)
		x = normalizedPosition.x * SCREENWIDTH
		y = SCREENHEIGHT - normalizedPosition.y * SCREENHEIGHT
		mousemove(x,y)
#				if avg_pos[2] < BACKGROUND:
#					if touched == False:
#						mouseclick(posx,posy)
#						touched = True
#				else:
#					touched = False
					

if __name__ == "__main__":
    main()
