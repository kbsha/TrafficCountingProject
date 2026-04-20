import cv2
from ultralytics import YOLO
from counter import TrafficCounter

def main():

    model = YOLO("models/yolov8n.pt")

    cap = cv2.VideoCapture("videos/Traffic1.mp4")

    counter = TrafficCounter(line_y=300)

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        results = model(frame)[0]

        frame = counter.process_frame(frame, results)

        cv2.imshow("Traffic Counting", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()