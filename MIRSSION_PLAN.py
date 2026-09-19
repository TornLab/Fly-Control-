import colorama
import os
from art import *
import Fly_control_autopilot
import Fly_control_img
import Fly_control_command
import Fly_control_voice
import Fly_control_img_Face
import Fly_control_Keyboard
import Fly_control_img_Object_recognition
import Fly_control_full_stack

os.system("cls")
colorama.init()

print(colorama.Fore.BLUE)
print(text2art("MIRSSION PLAN"))
print(
    """
    
                                                                                    
       
                                        [1]:Fly control autopilot
                                        [2]:Fly control img
                                        [3]:Fly control command
                                        [4]:Fly control voice
                                        [5]:Fly control img Face 
                                        [6]:Fly control Keyboard
                                        [7]:Fly control img Object recognition
                                        [8]:Fly control command Full Stack
       
    
    """
)

while True :

   Mood = input("Which mode do you want?")

   if Mood == "1":
       os.system("cls")
       Fly_control_autopilot.Autopilot.autopilot(self=123)

   elif Mood == "2":
       os.system("cls")
       Fly_control_img.IMG.drone_IMG(self=123)

   elif Mood == "3":
       os.system("cls")
       Fly_control_command.COMMAND.fly_command(self=123)

   elif Mood == "4":
       os.system("cls")
       Fly_control_voice.voice.VOICE(self=123)
       
   elif Mood == "5":
       os.system("cls")
       Fly_control_img_Face.IMG_Face.drone_IMG_Face(self=123)
       
   elif Mood == "6":
       os.system("cls")
       Fly_control_Keyboard.Keyboard.Flykey(self=123)
       
   elif Mood == "7":
       os.system("cls")
       F10 = Fly_control_img_Object_recognition.object()
       F10.Obj()

   elif Mood == "8":
       os.system("cls")
       F11 = Fly_control_full_stack.Full()
       F11.Stack()

   else:
       print("The mode number is wrong")
