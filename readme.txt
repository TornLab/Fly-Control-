FLY CONTROL
DJI / RYZE TELLO TERMINAL CONTROL PROJECT

ABOUT
-----
FLY CONTROL is my first serious programming project. I started writing it
when I was 14 years old.

It began as an experiment to control a DJI/Ryze Tello from a computer and
grew into a project involving terminal control, keyboard control, voice
control, OpenCV, face detection, object recognition, camera streaming and
autopilot experiments.

This repository documents that learning journey. It is an educational and
experimental project, not a certified commercial flight-control system.

FULL STACK
----------
The Full Stack terminal controller includes:

- Takeoff / landing
- Forward / backward / left / right
- Up / down
- Custom movement
- Clockwise / counter-clockwise rotation
- Flips
- Motor controls
- Speed control
- Battery
- Height
- Flight time
- Roll / pitch / yaw
- Attitude
- Barometer
- TOF distance
- Temperature
- Velocity
- Wi-Fi information when supported
- Tello IP and video UDP information
- Live camera
- Camera keyboard flight controls
- Screenshots
- MP4 video recording
- Emergency command
- Built-in HELP

INSTALL
-------
1. Install Python 3.10+.

2. Connect your computer to the Tello Wi-Fi network.

3. Install dependencies:

   python -m pip install -r requirements.txt

   Windows alternative:

   py -m pip install -r requirements.txt

4. Start the main launcher:

   python MIRSSION_PLAN.py

5. Select a mode.

COMMANDS
--------
Start with:

   --Help

Examples:

   --takeoff
   --Forward
   --Turn_Right
   --Battery
   --Status
   --Camera
   --Screenshot
   --Record
   --Land

MOVEMENT
--------
Forward/back/left/right/up/down ask for a distance between 20 and 500 cm.
Rotation asks for an angle between 1 and 360 degrees.

CAMERA
------
Run:

   --Camera

Keyboard:

   T = takeoff
   L = land
   W = forward
   S = backward
   A = left
   D = right
   O = up
   K = down
   Q = rotate left
   E = rotate right
   1 = motors on
   2 = motors off
   V = stream on
   B = stream off
   P = screenshot
   R = start/stop recording
   Z / ESC = exit camera

The camera window displays basic live telemetry.

ORIGINAL PROJECT MODES
----------------------
The original FLY CONTROL project contains several separate modules:

1. Autopilot
2. Image processing
3. Command terminal
4. Voice control
5. Face detection
6. Keyboard control
7. YOLO object recognition
8. Full Stack

DJITELLOPY
----------
DJITelloPy is the Python interface used by this project for Tello control.

Project:
https://github.com/damiafuentes/DJITelloPy

API:
https://djitellopy.readthedocs.io/en/latest/

SAFETY
------
This program controls a real aircraft.

Always test new code carefully. Use an open, controlled environment. Check
battery and the flight area before takeoff. Flips require enough space.
Emergency is an emergency motor-stop command, not a normal landing command.

The author is not responsible for damage, injury, loss or misuse caused by
this software. Follow the laws and drone rules that apply to your location.

LIMITATIONS
-----------
Not every command is available on every Tello model or firmware version.
Telemetry and video can also fail temporarily. Firmware, Wi-Fi, OS and
DJITelloPy versions can affect behavior.

PROJECT STRUCTURE
-----------------
Typical repository:

   MIRSSION_PLAN.py
   Fly_control_autopilot.py
   Fly_control_Keyboard.py
   Fly_control_voice.py
   Fly_control_img_Face.py
   Fly_control_img_Object_recognition.py
   Fly_control_command.py
   Fly_control_full_stack.py
   requirements.txt
   README.TXT

   yolov3.cfg
   yolov3.weights
   coco.names
   haarcascade_frontalface_default.xml

NOTE : 
Most commands are similar across different modes, and you don't need to know how to write code; however, using the autopilot does require some basic programming knowledge.
This project is open-source, and we would be happy to see developers contribute further to it.
This is just the beginning; many updates are on the way.

AUTHOR NOTE
-----------
This is my first project, started at age 14.

I built it to learn how software can communicate with real hardware and how
Python can be used for robotics, computer vision, automation and networking + + My personal interest in the aerospace industry at that age.

Some parts are simple. Some parts are experimental. Some parts will continue
to improve. That is part of the story of the project.

Thank you for visiting FLY CONTROL.
