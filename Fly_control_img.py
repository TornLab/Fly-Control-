class IMG:
    def drone_IMG(self):

       from djitellopy import Tello
       import cv2, math, time
       import beepy

       def sound():
         beepy.beep(3)
                 
       tello = Tello()

       tello.connect()
       
       farme_read = tello.get_frame_read()

       sound()

       while True:

           img = farme_read.frame

           siziFrame = cv2.resize(img ,(1280,720))

           cv2.imshow("FLY CONTROL",img)

           keyboard = cv2.waitKey(1) & 0xff

           if keyboard == ord("t"):
               tello.takeoff()

           elif keyboard == ord("l"):
               tello.land()

           elif keyboard == ord("w"):
               tello.move_forward(40)

           elif keyboard == ord("s"):
               tello.move_back(40)

           elif keyboard == ord("d"):
               tello.move_right(40)

           elif keyboard == ord("a"):
               tello.move_left(40)

           elif keyboard == ord("o"):
               tello.move_up(40)

           elif keyboard == ord("k"):
               tello.move_down(40)

           elif keyboard == ord("v"):
               tello.streamon()

           elif keyboard == ord("b"):
               tello.streamoff()

           elif keyboard == ord("1"):
               tello.turn_motor_on()

           elif keyboard == ord("2"):
               tello.turn_motor_off()

           elif keyboard == ord("z"):
               break
