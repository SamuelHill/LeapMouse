import Leap
import time
from AppKit import *

def main():
	controller = Leap.Controller()
	screens = NSScreen.screens()
	for s in screens:
		
		
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
		if not frame.hands.is_empty:
			hand = frame.hands[0]
			fingers = hand.fingers
			if not fingers.is_empty:
				num_fingers = 0
				avg_pos = Leap.Vector()
				for finger in fingers:
					num_fingers += 1
					avg_pos += finger.tip_position
				avg_pos /= len(fingers)
				posx = (SCREENWIDTH)/(FARRIGHT-FARLEFT)*(avg_pos[0]-FARLEFT)
				posy = (SCREENHEIGHT)/(BOTTOM-TOP)*(avg_pos[1]-TOP)
				# Limit to screen
				posx = 0 if posx < 0 else posx
				posx = SCREENWIDTH if posx > SCREENWIDTH else posx
				posy = 0 if posy < 0 else posy
				posy = SCREENHEIGHT if posy > SCREENHEIGHT else posy
				if num_fingers == 1:
					mousemove(posx,posy)
					if avg_pos[2] < BACKGROUND:
						if touched == False:
							mouseclick(posx,posy)
							touched = True
					else:
						touched = False
				# if num_fingers == 2:
if __name__ == "__main__":
    main()