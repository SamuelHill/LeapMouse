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
        # uncomment this line if you want to force the mouse 
        # to MOVE to the click location first (I found it was not necessary).
        #mouseEvent(kCGEventMouseMoved, posx,posy);
        mouseEvent(kCGEventLeftMouseDown, posx,posy);
        mouseEvent(kCGEventLeftMouseUp, posx,posy)

def main():
	controller = Leap.Controller()
	mainMonitor = CGDisplayBounds(CGMainDisplayID())
	FPS = 30
	FARLEFT = -300
	FARRIGHT = 300
	TOP = 600
	BOTTOM = 200
	SCREENWIDTH = mainMonitor.size.width
	SCREENHEIGHT = mainMonitor.size.height
	
	last_time = time.time()
	
	while True:
		new_time = time.time()
		sleep_time = ((1000.0 / FPS) - (new_time - last_time)) / 1000.0
		if sleep_time > 0:
			time.sleep(sleep_time)
		last_time = new_time
		frame = controller.frame()
		if not frame.hands.is_empty:
			hand = frame.hands[0]
			fingers = hand.fingers
			if not fingers.is_empty:
				avg_pos = Leap.Vector()
				for finger in fingers:
					avg_pos += finger.tip_position
				avg_pos /= len(fingers)
				posx = (SCREENWIDTH)/(FARRIGHT-FARLEFT)*(avg_pos[0]-FARLEFT)
				posy = (SCREENHEIGHT)/(BOTTOM-TOP)*(avg_pos[1]-TOP)
				mousemove(posx,posy)

if __name__ == "__main__":
    main()