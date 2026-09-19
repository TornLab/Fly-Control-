class Autopilot:
    
  def autopilot(self):

     from easytello import tello
     import colorama
     import keyboard

     colorama.init()

     print(colorama.Fore.LIGHTWHITE_EX)

     print("Confirm to connect to the drone[Yes]:space")

     key2 = keyboard.read_key()


     if key2 == ("space"):
         drone = tello.Tello()
         print("You are connected to the drone")

         while True :

             print("Can flight data be sent?[Yes]:enter")

             key1 = keyboard.read_key()


             if key1 == "enter":
                 print(colorama.Fore.LIGHTGREEN_EX)
                 print("Autopilot activated")
                 print(colorama.Fore.LIGHTMAGENTA_EX)
                 drone.set_speed(speed=100)
                 drone.takeoff()
                 drone.streamon()
                 drone.up(100)
                 drone.forward(100)
                 drone.right(100)
                 drone.forward(50)
                 drone.left(50)
                 drone.forward(30)
                 drone.streamoff()
                 drone.land()
                 print(colorama.Fore.RED, "Autopilot disabled")
                 break
