class Full():
    def Stack(self):
       import numpy as np
       from djitellopy import Tello
       import cv2, math, time
       import colorama
       import art
       
       colorama.init()
        
       print(colorama.Fore.GREEN)
       print(art.text2art("FLY CONTROL"))
       
       tello = Tello()

       tello.connect()
       
       def help():
          print(
          """
              --takeoff : makes the drone fly
              --Forward : The drone moves forward by 40 cm
              --Backward : The drone moves back 40 cm
              --Right : The drone moves 40 cm to the right
              --Left : The drone moves 40 cm to the left
              --up: The height of the drone increases by 40 cm
              --Down : The height of the drone decreases by 40 cm
              --Flip_Right : drone turns 90 degrees to the right
              --Flip_Left : drone turns 90 degrees to the left
              --Flip_Back : The drone turns back 180 degrees
              --Flip_Custom: 
              --Land : to land the drone
              --Move_Custom : You can move the drone to wherever you like.
              --show_IP_UDP 
              --Camera  
              --Emergency 
              --Show_IP_Drone : It will show the IP of the drone
              --Show_the_drone_battery_voltage : It shows the battery voltage of the drone
              --Show_address  
              --Show_Height : It shows the height of the drone
              --Fly_Time : It shows the flight time
              --Check_the_yaw
              --Check_the_pitch
              --Check_the_roll
      """)
       
       print(colorama.Fore.RED,"Use(-Help)for command prompts")
       
       while True : 
           
          print(colorama.Fore.WHITE) 
          
          command = input("Enter command :")
           
          if command == "--takeoff" : 
            tello.takeoff()
           
          elif command == "--Land":
            tello.land()
            
          elif command == "--up":
            tello.move_up(x=40)
            
          elif command == "--Down":
            tello.move_down(x=40) 
            
          elif command == "--Forward":
            tello.move_forward(x=40)
            
          elif command == "--Backward":
            tello.move_back(x=40)
            
          elif command == "--Right":
            tello.move_right(x=40)
            
          elif command == "--Left":
            tello.move_left(x=40)
            
          elif command == "--Move_Customer":
            A = str(input("moving point ?"))
            B = int(input("How many degrees to move?"))
            tello.move(direction=A,x=B)
            
          elif command == "--Flip_Back":
            tello.flip_back()
            
          elif command == "--Flip_Right":
            tello.flip_right()
            
          elif command == "--Flip_Left":
            tello.flip_left()
            
          elif command == "--Flip_Forward":
            tello.flip_forward()
            
          elif command == "--Flip_Customer":
            C = str(input("Which way should I flip?"))
            tello.flip(direction=C)
            
          elif command == "--show_IP_UDP":
            print(tello.VS_UDP_IP)
            
          elif command == "--Show_IP_Drone":
            print(tello.TELLO_IP)
            
          elif command == "--Engines_on":
            tello.turn_motor_on()
            
          elif command == "--Engines_off":
            tello.turn_motor_off()
          
          elif command == "--Emergency":
            tello.emergency()
            
          elif command == "--Show_the_drone_battery_voltage":
            print(tello.get_battery())
            
          elif command == "--Show_address":
            print(tello.address)
            
          elif command == "--Fly_Time":
            print(tello.get_flight_time())
            
          elif command == "--Show_Height":
            print(tello.get_height())
            
          elif command == "--Check_the_roll":
            print(tello.get_roll())
            
          elif command == "--Check_the_pitch":
            print(tello.get_pitch())
                      
          elif command == "--Check_the_yaw":
            print(tello.get_yaw())
            
          elif command == "--Sspeed":
            x = int(input("How ? "))
            print(tello.set_speed(x))
          
          elif command == "--Camera":
            farme_read = tello.get_frame_read()

            while True:
    
              img = farme_read.frame

              siziFrame = cv2.resize(img,(1280,720))

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
