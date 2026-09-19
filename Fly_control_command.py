class COMMAND():
    def fly_command(self):

      import colorama
      colorama.init()
      from easytello import tello
      import beepy
      import socket
      print(colorama.Fore.GREEN)

      host = socket.gethostname()
      ip = socket.gethostbyname(host)
      show_ip = ("[*] IP My System "+ip)

      def sound():
         beepy.beep(3)
      
      A = 0
      while A < 5:
          print (colorama.Fore.LIGHTGREEN_EX,show_ip)
          A += 1
    

      drone = tello.Tello()
      Sizi = 40

      def help():
          print(colorama.Fore.LIGHTMAGENTA_EX,
      """
          -Takeoff : makes the drone fly
          -Forward : The drone moves forward by 40 cm
          -Backward : The drone moves back 40 cm
          -Right : The drone moves 40 cm to the right
          -Left : The drone moves 40 cm to the left
          -Go_up : The height of the drone increases by 40 cm
          -Go_down : The height of the drone decreases by 40 cm
          -Turn_right : drone turns 90 degrees to the right
          -Turn_left : drone turns 90 degrees to the left
          -Turn_back : The drone turns back 180 degrees
          -Full_turn : The drone rotates 360 degrees
          -Land : to land the drone
          -Start_stream : The drone comes and starts taking video
          -End_stream : The drone comes and finishes filming
          -Speed : The speed of the drone can be as much as you want
          -Show_speed : It shows the speed of the drone
          -IP_drone : It will show the IP of the drone
          -Show_the_drone_battery_voltage : It shows the battery voltage of the drone
          -Show_flight_data : It shows the flight data of the drone
          -Port_drone : It will show the drone port
          -Show_WiFi_specifications_drone : It will show the Wi-Fi specifications of the drone
          -Changing_the_WiFi_of_the_drone : You can change the WiFi ID and password of the drone
          -Debug : It shows whether the drone is healthy or not
          -Show_IP_address_and_port : It will show the IP address and port of the drone
          -Show_height : It shows the height of the drone
          -Show_temperature : It shows the temperature of the drone
          -Show_time : It shows the time of the drone
          -Attitude : It shows the state of the UAV, it is determined according to the tilt of its axis relative to a reference such as the ground
          -flip : Through this option, you can give your drone a flip, for example, throw it backwards, whatever you want
          -wait : You can keep your drone waiting as long as you like
          -tof : It shows the flight time
          -baro : It shows the air pressure
          -stream_state : Drone filming status
          -repr : 
      """
      )
      print(colorama.Fore.RED,"Use(-Help)for command prompts")

      while True:
    
          print(colorama.Fore.LIGHTGREEN_EX)

          command = input("Enter command :")
    
          if command == "-Help":
              help()
        
          elif command == "-Takeoff":
              drone.takeoff()
              print("drone is flying")
              sound()
        
          elif command == "-Forward":
              drone.forward(Sizi)
              print("drone is going forward")
              sound()
        
          elif command == "-Backward":
              drone.back(Sizi)
              print("drone is going backward")
              sound()
        
          elif command == "-Right":
              drone.right(Sizi)
              print("drone is going right")
              sound()
        
          elif command == "-Left":
              drone.left(Sizi)
              print("drone is going left")
              sound()
        
          elif command == "-Go_up":
              drone.up(Sizi)
              print("drone is going up")
              sound()
        
          elif command == "-Go_down":
              drone.down(Sizi)
              print("drone is going right")
              sound()
        
          elif command == "-Turn_right":
              drone.cw(90)
              print("drone is going turnning right")
              sound()
        
          elif command == "-Turn_left":
              drone.ccw(90)
              print("drone is going turnning left")
              sound()
        
          elif command == "-Turn_back":
              drone.cw(180)
              print("drone is going turnning back")
              sound()
        
          elif command == "-Full_turn":
              drone.cw(360)
              print("drone is going turning full")
              sound()
        
          elif command == "-Land":
              drone.land()
              print("The drone is landing")
        
          elif command == "-Start_stream":
              drone.streamon()
              sound()
        
          elif command == "-End_stream":
              drone.streamoff()

          elif command == "-Speed":
              speed = int(input("Speed ? : "))
              print(speed)
              drone.set_speed(speed=speed)
              sound()

          elif command == "-Show_speed":
              print(drone.get_speed)
              sound()

          elif command == "-IP_drone":
              print(drone.tello_ip,drone.local_ip)
              sound()

          elif command == "-Show_the_drone_battery_voltage":
              print(drone.get_battery)
              sound()

          elif command == "-Show_flight_data":
              print(drone.get_log)
              sound()

          elif command == "-Port_drone":
              print(drone.tello_port,drone.local_port)
              sound()

          elif command == "-Show_WiFi_specifications_drone":
              print(drone.get_wifi)
              sound()

          elif command == "-Changing_the_WiFi_of_the_drone":
              drone.set_wifi(input("ssid : "),input("password : "))
              sound()

          elif command == "-Debug":
              print(drone.debug)
              sound()

          elif command == "-Show_IP_address_and_port":
              print(drone.tello_address)
              sound()

          elif command == "-Show_height":
              print(drone.get_height)
              sound()

          elif command == "-Show_temperature":
              print(drone.get_temp)
              sound()

          elif command == "-Show_time":
              print(drone.get_time)
              sound()
              
          elif command == "-Attitude":
              drone.get_attitude()
              sound()
              
          elif command == "-flip":
              drone.flip(input("?"))
              sound()
              
          elif command == "-wait":
              inp = float(input("Enter a decimal number : "))
              drone.wait(inp)
              
          elif command == "-tof":
              print(drone.get_tof())
              sound()
              
          elif command == "-acceleration":
              print(drone.get_acceleration())
              sound()
              
          elif command == "-baro":
              print(drone.get_baro())
              sound()
              
          elif command == "-stream_state":
              print(drone.stream_state)
              sound()
              
          elif command == "-repr":
              print(drone.__repr__())
              sound()
              
          elif command == "image":
              print(drone.stream_state.imag)
              sound()
              
          elif command == "000FFFuvi168%$^%^000":
              print(colorama.Fore.LIGHTYELLOW_EX,"Your malicious code was activated on the UAV")
              print(colorama.Fore.LIGHTGREEN_EX)
              sound()
              drone.set_speed(speed=100)
              drone.up(60)
              drone.forward(80)
              drone.cw(360)
              drone.left(78)
              drone.land()
              
          elif command == "111FFFuvi168@#$%$%^111":
              print(colorama.Fore.LIGHTYELLOW_EX,"Your malicious code was activated on the UAV")
              print(colorama.Fore.LIGHTGREEN_EX)
              sound()
              drone.flip("hello")
              drone.set_speed(speed=100)
              drone.forward(90)
              drone.emergency()
              drone.set_wifi(ssid="exploit",passwrd="payload")
              drone.land()
              
          elif command == "222FFFuvi168)&(&*^&$%#24@5)222":
              print(colorama.Fore.LIGHTYELLOW_EX,"Your malicious code was activated on the UAV")
              print(colorama.Fore.LIGHTGREEN_EX)
              sound()
              drone.set_speed(speed=100)
              drone.up(50)
              drone.cw(100)
              drone.ccw(100)
              drone.rc_control(a=50,b=50,c=50,d=50)
              drone.down(50)
              
          elif command == "333FFFuvi168!@#@#$#$%$%^%^&^&&*&)*333":
              print(colorama.Fore.LIGHTYELLOW_EX,"Your malicious code was activated on the UAV")
              print(colorama.Fore.LIGHTGREEN_EX)
              sound()
              drone.set_speed(speed=100)
              drone.takeoff()
              drone.up(100)
              drone.forward(100)
              drone.left(100)
              drone.right(100)
              drone.land()
              
          elif command == "333FFuvi168!hJFGDFTYT5&^%##333":
            print(colorama.Fore.LIGHTYELLOW_EX,"Your malicious code was activated on the UAV")
            print(colorama.Fore.LIGHTGREEN_EX)
            sound()
            drone.flip(direc="back")
            drone.flip(direc="forward")
            drone.flip(direc="left")
            drone.flip(direc="right")
              
          else:
              print(colorama.Fore.CYAN,"The entered command is not correct!!!")
              print(colorama.Fore.RED,"Use(-Help)for command prompts")
