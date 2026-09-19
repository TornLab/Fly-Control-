class voice():
    def VOICE(self):

       import speech_recognition as sr
       from easytello import tello
       import colorama
       import art

       colorama.init()
       print(colorama.Back.BLACK)
       print(colorama.Fore.LIGHTGREEN_EX)
       

       print(art.text2art("0000000000000000000000000000","small"))
       print(art.text2art("0000000000000000000000000000","small"))
       print(art.text2art("0000000000000000000000000000","small"))

       print(colorama.Fore.LIGHTYELLOW_EX)

       def help():
           print(
           """
           Use your voice to control the drone:
           take off : makes the drone fly
           forward :  The drone moves forward by 30 cm
           turn or back : The drone moves back 30 cm
           right or rye : The drone moves 30 cm to the right
           left : The drone moves 30 cm to the left
           see right : drone turns 30 degrees to the right
           see left : drone turns 30 degrees to the left
           go up or up : The height of the drone increases by 30 cm
           go down or dawn or down : The height of the drone decreases by 30 cm
           land : to land the drone
           """)

       help()

       drone = tello.Tello()

       def audioRecognizer():
           speech = sr.Recognizer()

           with sr.Microphone() as source:
               print("say your command: ")
               audio = speech.listen(source,phrase_time_limit=3)

               try:
                   text = speech.recognize_google(audio,language="en-US")
                   print("your command: ",text)

               except:

                   print("i'm waiting for your command.")
           return text
     
       def Voicecontrol(input_command):
            
           if "land" in input_command:
              drone.land()

           elif "take off" in input_command:
               drone.takeoff()

           elif "forward" in input_command:
               drone.forward(30)

           elif "turn" in input_command or "back" in input_command:
               drone.back(30)

           elif "right" in input_command or "rye" in input_command:
               drone.right(30)

           elif "left" in input_command:
               drone.left(30)

           elif "see right" in input_command:
               drone.cw(30)

           elif "see left" in input_command:
               drone.ccw(30)

           elif "go up" in input_command or "up" in input_command:
               drone.up(30)

           elif "go down" in input_command or "dawn" in input_command or "down" in input_command:
               drone.down(30)



