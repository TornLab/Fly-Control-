class IMG_Face:
    def drone_IMG_Face(self):

        import cv2
        import numpy as np
        from djitellopy import Tello
        import art
        import colorama
        colorama.init()
        
        print(colorama.Back.BLACK)
        print(colorama.Fore.LIGHTWHITE_EX)
        print(art.text2art("FLY CONTROL"))

        tello = Tello()

        tello.connect()

        tello.streamon()

        tello.set_speed(20)

        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        while True:
            frame = tello.get_frame_read().frame
    
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
            if len(faces) > 0:
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
                face_x, face_y, face_w, face_h = faces[0]
                center_x, center_y = face_x + face_w/2, face_y + face_h/2
                frame_center_x, frame_center_y = frame.shape[1] / 2, frame.shape[0] / 2
        
                if center_x < frame_center_x - 50:
                    tello.rotate_counter_clockwise(20)
                elif center_x > frame_center_x + 50:
                    tello.rotate_clockwise(20)
        
                if center_y < frame_center_y - 30:
                    tello.move_up(20)
                elif center_y > frame_center_y + 30:
                    tello.move_down(20)
    
            cv2.imshow('frame', frame)
    
            keyboard = cv2.waitKey(1) & 0xFF
    
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

            elif keyboard == ord("1"):
                tello.turn_motor_on()

            elif keyboard == ord("2"):
                tello.turn_motor_off()

            elif keyboard == ord("z"):
                break
