class object():
    def Obj(self):
        from djitellopy import Tello
        import cv2
        import numpy as np
        import art
        import colorama
        
        print(colorama.Back.BLACK)
        print(colorama.Fore.LIGHTWHITE_EX)
        
        print(art.text2art("FLY CONTROL"))
        
        my_drone = Tello()

        my_drone.connect()
        my_drone.streamon()

        net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

        classes = []
        with open("coco.names", "r") as f:
            classes = [line.strip() for line in f.readlines()]

        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))

        while True:
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                my_drone.land()
            elif key == ord('t'):
                my_drone.takeoff()
            elif key == ord('u'):
                my_drone.move_up(50)
            elif key == ord('d'):
                my_drone.move_down(50)
            elif key == ord('f'):
                my_drone.move_forward(50)
            elif key == ord('b'):
                my_drone.move_back(50)
            elif key == ord('l'):
                my_drone.move_left(50)
            elif key == ord('r'):
                my_drone.move_right(50)
            elif key == ord('z'):
                break

            frame = my_drone.get_frame_read().frame

            blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
            net.setInput(blob)
            outs = net.forward(output_layers)
            class_ids = []
            confidences = []
            boxes = []
            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5:
                        center_x = int(detection[0] * frame.shape[1])
                        center_y = int(detection[1] * frame.shape[0])
                        width = int(detection[2] * frame.shape[1])
                        height = int(detection[3] * frame.shape[0])
                        x = int(center_x - width / 2)
                        y = int(center_y - height / 2)

                        cv2.rectangle(frame, (x, y), (x + width, y + height), colors[class_id], 2)
                        label = f"{classes[class_id]}: {confidence:.2f}"
                        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[class_id], 2)

            cv2.imshow('Object Detection with Tello Drone', frame)
        
