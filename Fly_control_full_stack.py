# FLY CONTROL - Full Stack Terminal Controller
import os
import time
from datetime import datetime

import cv2
from djitellopy import Tello
import colorama
from colorama import Fore
from art import text2art


class Full:
    def Stack(self):
        colorama.init(autoreset=True)
        self._clear()
        print(Fore.GREEN + text2art("FLY CONTROL"))
        print(Fore.CYAN + "FULL STACK TERMINAL CONTROLLER")
        print("=" * 68)

        tello = Tello()

        try:
            print(Fore.YELLOW + "Connecting to Tello...")
            tello.connect()
            print(Fore.GREEN + "Connected.")
            print(Fore.CYAN + f"Battery: {self._safe(tello.get_battery, 'N/A')}%")
        except Exception as e:
            print(Fore.RED + f"Connection failed: {e}")
            input("Press ENTER...")
            return

        self.help()

        while True:
            try:
                command = input(Fore.WHITE + "\nFLY CONTROL > ").strip()

                if command.lower() in ("help", "--help", "-help", "?"):
                    self.help()

                elif command.lower() in ("clear", "--clear"):
                    self._clear()

                elif command.lower() in ("exit", "quit", "--exit"):
                    self._shutdown(tello)
                    break

                # Flight
                elif command == "--takeoff":
                    self._run("Takeoff", tello.takeoff)
                elif command == "--Land":
                    self._run("Land", tello.land)
                elif command == "--Emergency":
                    print(Fore.RED + "EMERGENCY STOP. Use only in a real emergency.")
                    if input("Type EMERGENCY to confirm: ") == "EMERGENCY":
                        self._run("Emergency", tello.emergency)

                # Movement
                elif command == "--Forward":
                    self._move(tello.move_forward, "Forward")
                elif command == "--Backward":
                    self._move(tello.move_back, "Backward")
                elif command == "--Right":
                    self._move(tello.move_right, "Right")
                elif command == "--Left":
                    self._move(tello.move_left, "Left")
                elif command == "--up":
                    self._move(tello.move_up, "Up")
                elif command == "--Down":
                    self._move(tello.move_down, "Down")
                elif command == "--Move_Custom":
                    self._move_custom(tello)

                # Rotation
                elif command == "--Turn_Right":
                    self._rotate(tello.rotate_clockwise, "Clockwise")
                elif command == "--Turn_Left":
                    self._rotate(tello.rotate_counter_clockwise, "Counter-clockwise")

                # Flips
                elif command == "--Flip_Forward":
                    self._run("Forward flip", tello.flip_forward)
                elif command == "--Flip_Back":
                    self._run("Back flip", tello.flip_back)
                elif command == "--Flip_Right":
                    self._run("Right flip", tello.flip_right)
                elif command == "--Flip_Left":
                    self._run("Left flip", tello.flip_left)
                elif command == "--Flip_Custom":
                    d = input("Direction [l/r/f/b]: ").strip().lower()
                    if d in ("l", "r", "f", "b"):
                        self._run(f"Flip {d}", lambda: tello.flip(d))
                    else:
                        print(Fore.RED + "Invalid direction.")

                # Motors / speed
                elif command == "--Engines_on":
                    self._run("Motors ON", tello.turn_motor_on)
                elif command == "--Engines_off":
                    self._run("Motors OFF", tello.turn_motor_off)
                elif command in ("--Speed", "--Sspeed"):
                    self._set_speed(tello)

                # Network
                elif command == "--show_IP_UDP":
                    print(Fore.CYAN + str(self._safe(tello.get_udp_video_address, "N/A")))
                elif command == "--Show_IP_Drone":
                    print(Fore.CYAN + str(tello.TELLO_IP))
                elif command == "--Show_address":
                    print(Fore.CYAN + str(tello.address))

                # Telemetry
                elif command in ("--Battery", "--Show_the_drone_battery_voltage"):
                    print(Fore.GREEN + f"Battery: {self._safe(tello.get_battery, 'N/A')}%")
                elif command == "--Show_Height":
                    print(Fore.CYAN + f"Height: {self._safe(tello.get_height, 'N/A')} cm")
                elif command == "--Fly_Time":
                    print(Fore.CYAN + f"Flight time: {self._safe(tello.get_flight_time, 'N/A')} s")
                elif command == "--Check_the_roll":
                    print(Fore.CYAN + f"Roll: {self._safe(tello.get_roll, 'N/A')}°")
                elif command == "--Check_the_pitch":
                    print(Fore.CYAN + f"Pitch: {self._safe(tello.get_pitch, 'N/A')}°")
                elif command == "--Check_the_yaw":
                    print(Fore.CYAN + f"Yaw: {self._safe(tello.get_yaw, 'N/A')}°")
                elif command == "--Attitude":
                    print(Fore.CYAN + f"Attitude: {self._safe(tello.get_attitude, 'N/A')}")
                elif command == "--Barometer":
                    print(Fore.CYAN + f"Barometer: {self._safe(tello.get_barometer, 'N/A')}")
                elif command == "--TOF":
                    print(Fore.CYAN + f"TOF: {self._safe(tello.get_distance_tof, 'N/A')} mm")
                elif command == "--Temperature":
                    print(Fore.CYAN + f"Temperature: {self._safe(tello.get_temperature, 'N/A')} °C")
                elif command == "--Speed_Status":
                    print(Fore.CYAN + f"Speed: {self._safe(tello.get_speed, 'N/A')} cm/s")
                elif command == "--Velocity":
                    print(Fore.CYAN + "X/Y/Z: "
                          f"{self._safe(tello.get_speed_x,'N/A')} / "
                          f"{self._safe(tello.get_speed_y,'N/A')} / "
                          f"{self._safe(tello.get_speed_z,'N/A')} cm/s")
                elif command == "--WiFi":
                    print(Fore.CYAN + f"Wi-Fi: {self._safe(tello.get_wifi, 'N/A')}")
                elif command == "--Status":
                    self.status(tello)

                # Video
                elif command == "--Stream_On":
                    self._run("Stream ON", tello.streamon)
                elif command == "--Stream_Off":
                    self._run("Stream OFF", tello.streamoff)
                elif command == "--Camera":
                    self.camera(tello)
                elif command == "--Screenshot":
                    self.screenshot(tello)
                elif command == "--Record":
                    self.record(tello)
                else:
                    print(Fore.RED + "Unknown command. Type --Help.")

            except KeyboardInterrupt:
                print(Fore.YELLOW + "\nInterrupted. Use --Land when appropriate.")
            except Exception as e:
                print(Fore.RED + f"Command error: {e}")

    def help(self):
        print(Fore.YELLOW + r"""
========================= FLY CONTROL HELP =========================

GENERAL
--Help                  Show this help
--clear                 Clear terminal
--exit                  Exit controller

FLIGHT
--takeoff               Take off
--Land                  Land
--Emergency             Emergency motor stop

MOVEMENT
--Forward               Move forward; asks for 20-500 cm
--Backward              Move backward; asks for 20-500 cm
--Right                 Move right; asks for 20-500 cm
--Left                  Move left; asks for 20-500 cm
--up                    Move up; asks for 20-500 cm
--Down                  Move down; asks for 20-500 cm
--Move_Custom           Choose direction and distance

ROTATION
--Turn_Right            Clockwise rotation; asks for degrees
--Turn_Left             Counter-clockwise rotation; asks for degrees

FLIPS
--Flip_Forward          Forward flip
--Flip_Back             Back flip
--Flip_Right            Right flip
--Flip_Left             Left flip
--Flip_Custom            l/r/f/b custom flip

MOTORS / SPEED
--Engines_on            Turn motors on
--Engines_off           Turn motors off
--Speed                 Set speed (10-100 cm/s)
--Sspeed                Original-project alias

TELEMETRY
--Status                Full status dashboard
--Battery               Battery percentage
--Show_the_drone_battery_voltage
--Show_Height           Height in cm
--Fly_Time              Flight time
--Check_the_roll        Roll angle
--Check_the_pitch       Pitch angle
--Check_the_yaw         Yaw angle
--Attitude              Roll/pitch/yaw attitude
--Barometer             Barometer value
--TOF                   Time-of-flight distance
--Temperature           Temperature
--Speed_Status          Reported speed
--Velocity              X/Y/Z velocity
--WiFi                  Wi-Fi information when supported

NETWORK
--Show_IP_Drone         Tello IP
--show_IP_UDP           Video UDP address
--Show_address          Control socket address

VIDEO / CAMERA
--Stream_On             Start video stream
--Stream_Off            Stop video stream
--Camera                Live camera + keyboard flight control
--Screenshot            Save a PNG frame
--Record                Record MP4 video

CAMERA KEYBOARD
T takeoff     L land       W forward      S backward
A left        D right      O up           K down
Q rotate left E rotate right
1 motors on   2 motors off
V stream on   B stream off
P screenshot  R record toggle
Z or ESC exit camera

IMPORTANT
- Test new flight code carefully.
- Keep a safe, open flight area.
- Movement is normally 20-500 cm.
- Rotation is in degrees.
- Flips require sufficient space.
- Emergency is NOT a normal landing command.

====================================================================
""")

    @staticmethod
    def _clear():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def _safe(func, default):
        try:
            return func()
        except Exception:
            return default

    @staticmethod
    def _run(label, func):
        try:
            result = func()
            print(Fore.GREEN + f"{label}: OK")
            if result not in (None, "OK"):
                print("Response:", result)
        except Exception as e:
            print(Fore.RED + f"{label}: FAILED -> {e}")

    @staticmethod
    def _number(prompt, low, high):
        while True:
            try:
                x = int(input(prompt))
                if low <= x <= high:
                    return x
            except ValueError:
                pass
            print(Fore.RED + f"Enter a number from {low} to {high}.")

    def _move(self, func, name):
        d = self._number(f"{name} distance (20-500 cm): ", 20, 500)
        self._run(f"{name} {d} cm", lambda: func(d))

    def _rotate(self, func, name):
        a = self._number(f"{name} angle (1-360): ", 1, 360)
        self._run(f"{name} {a}°", lambda: func(a))

    def _move_custom(self, tello):
        d = input("Direction [up/down/left/right/forward/back]: ").lower().strip()
        if d not in ("up", "down", "left", "right", "forward", "back"):
            print(Fore.RED + "Invalid direction.")
            return
        x = self._number("Distance (20-500 cm): ", 20, 500)
        self._run(f"Move {d} {x} cm", lambda: tello.move(d, x))

    def _set_speed(self, tello):
        x = self._number("Speed (10-100 cm/s): ", 10, 100)
        self._run(f"Speed {x}", lambda: tello.set_speed(x))

    def status(self, t):
        print(Fore.CYAN + "\n================ DRONE STATUS ================")
        rows = [
            ("Battery", self._safe(t.get_battery, "N/A"), "%"),
            ("Height", self._safe(t.get_height, "N/A"), "cm"),
            ("Flight time", self._safe(t.get_flight_time, "N/A"), "s"),
            ("Speed", self._safe(t.get_speed, "N/A"), "cm/s"),
            ("Temperature", self._safe(t.get_temperature, "N/A"), "°C"),
            ("TOF", self._safe(t.get_distance_tof, "N/A"), "mm"),
            ("Barometer", self._safe(t.get_barometer, "N/A"), ""),
            ("Roll", self._safe(t.get_roll, "N/A"), "°"),
            ("Pitch", self._safe(t.get_pitch, "N/A"), "°"),
            ("Yaw", self._safe(t.get_yaw, "N/A"), "°"),
        ]
        for n, v, u in rows:
            print(f"{n:<16}: {v} {u}")
        print("================================================")

    def _stream(self, t):
        try:
            t.streamon()
            time.sleep(1)
            return t.get_frame_read()
        except Exception as e:
            print(Fore.RED + f"Video error: {e}")
            return None

    def camera(self, t):
        reader = self._stream(t)
        if reader is None:
            return

        recording = False
        writer = None
        filename = None

        try:
            while True:
                frame = reader.frame
                if frame is None:
                    continue
                frame = cv2.resize(frame, (1280, 720))

                battery = self._safe(t.get_battery, "N/A")
                height = self._safe(t.get_height, "N/A")
                cv2.putText(frame, f"BAT {battery}% | HEIGHT {height} cm",
                            (20, 35), cv2.FONT_HERSHEY_SIMPLEX, .8,
                            (0, 255, 0), 2)

                if recording and writer is not None:
                    writer.write(frame)
                    cv2.putText(frame, "REC", (20, 75),
                                cv2.FONT_HERSHEY_SIMPLEX, .9,
                                (0, 0, 255), 2)

                cv2.imshow("FLY CONTROL - CAMERA", frame)
                key = cv2.waitKey(1) & 0xff

                if key in (27, ord("z")):
                    break
                elif key == ord("t"):
                    self._run("Takeoff", t.takeoff)
                elif key == ord("l"):
                    self._run("Land", t.land)
                elif key == ord("w"):
                    self._run("Forward", lambda: t.move_forward(40))
                elif key == ord("s"):
                    self._run("Backward", lambda: t.move_back(40))
                elif key == ord("a"):
                    self._run("Left", lambda: t.move_left(40))
                elif key == ord("d"):
                    self._run("Right", lambda: t.move_right(40))
                elif key == ord("o"):
                    self._run("Up", lambda: t.move_up(40))
                elif key == ord("k"):
                    self._run("Down", lambda: t.move_down(40))
                elif key == ord("q"):
                    self._run("Rotate left", lambda: t.rotate_counter_clockwise(30))
                elif key == ord("e"):
                    self._run("Rotate right", lambda: t.rotate_clockwise(30))
                elif key == ord("1"):
                    self._run("Motors ON", t.turn_motor_on)
                elif key == ord("2"):
                    self._run("Motors OFF", t.turn_motor_off)
                elif key == ord("v"):
                    self._run("Stream ON", t.streamon)
                elif key == ord("b"):
                    self._run("Stream OFF", t.streamoff)
                elif key == ord("p"):
                    self._save_frame(frame)
                elif key == ord("r"):
                    if not recording:
                        filename = "tello_video_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".mp4"
                        writer = cv2.VideoWriter(
                            filename, cv2.VideoWriter_fourcc(*"mp4v"),
                            30.0, (1280, 720))
                        recording = True
                        print(Fore.RED + f"REC ON: {filename}")
                    else:
                        recording = False
                        if writer:
                            writer.release()
                        writer = None
                        print(Fore.GREEN + f"REC OFF: {filename}")
        finally:
            if writer:
                writer.release()
            cv2.destroyAllWindows()
            try:
                t.streamoff()
            except Exception:
                pass

    def screenshot(self, t):
        reader = self._stream(t)
        if reader is None:
            return
        try:
            time.sleep(1)
            frame = reader.frame
            if frame is not None:
                self._save_frame(frame)
        finally:
            try:
                t.streamoff()
            except Exception:
                pass

    def record(self, t):
        reader = self._stream(t)
        if reader is None:
            return
        name = "tello_recording_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".mp4"
        writer = None
        try:
            print(Fore.YELLOW + "Press Z or ESC in the camera window to stop.")
            while True:
                frame = reader.frame
                if frame is None:
                    continue
                frame = cv2.resize(frame, (1280, 720))
                if writer is None:
                    writer = cv2.VideoWriter(
                        name, cv2.VideoWriter_fourcc(*"mp4v"),
                        30.0, (1280, 720))
                writer.write(frame)
                cv2.imshow("FLY CONTROL - RECORDING", frame)
                if cv2.waitKey(1) & 0xff in (27, ord("z")):
                    break
        finally:
            if writer:
                writer.release()
            cv2.destroyAllWindows()
            try:
                t.streamoff()
            except Exception:
                pass
        print(Fore.GREEN + f"Saved: {name}")

    @staticmethod
    def _save_frame(frame):
        name = "tello_photo_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
        if cv2.imwrite(name, frame):
            print(Fore.GREEN + f"Screenshot saved: {name}")

    @staticmethod
    def _shutdown(t):
        try:
            if getattr(t, "is_flying", False):
                if input("Drone is flying. Land before exit? [Y/n]: ").lower() != "n":
                    t.land()
        except Exception:
            pass
        try:
            t.streamoff()
        except Exception:
            pass
        try:
            t.end()
        except Exception:
            pass
        print(Fore.GREEN + "FLY CONTROL closed.")
