class Keyboard():
    def Flykey(self):
        from easytello import tello
        import keyboard
        import art
        import colorama;colorama.init();print(colorama.Fore.LIGHTWHITE_EX)
        
        print(art.text2art("FLY CONTROL"))
        
        Drone = tello.Tello()
        
        print(colorama.Fore.LIGHTRED_EX,"The attention of the drone is set to manual mode")

        while True:
          print(colorama.Fore.LIGHTWHITE_EX)
          print(
              "[Enter]:Takeoff | [Space]:Land | [w]:Forward 40° | [s]:Back 40° | [a]:Left 40°\n"
              "[d]:Right 40° | [>]:clockwise 90° | [<]:counter clockwise 90° | [^]:up 40° | [⬇]:Down 40°"
              "[q]:clockwise 180° | [t]:clockwise 360° | [m]:start video | [n]:End video"
          )
          key = keyboard.read_key()
    
          if key == "enter":
              Drone.takeoff()
          elif key == "space":
              Drone.land()
          elif key == "w":
              Drone.forward(40)
          elif key == "s":
              Drone.back(40)
          elif key == "a":
              Drone.left(40)
          elif key == "d":
              Drone.right(40)
          elif key == "right":
              Drone.cw(90)
          elif key == "left":
              Drone.ccw(90)
          elif key == "up":
              Drone.up(40)
          elif key == "down":
              Drone.down(40)
          elif key == "q":
              Drone.cw(180)
          elif key == "t":
              Drone.cw(360)
          elif key == "m":
              Drone.streamon()
          elif key == "n":
              Drone.streamoff()
          else:
              print(colorama.Fore.LIGHTRED_EX,"The data sent is wrong")
