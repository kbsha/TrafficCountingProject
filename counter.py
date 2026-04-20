import cv2

class TrafficCounter:

    def __init__(self, line_y=300):
        self.line_y = line_y
        self.count = 0

    def process_frame(self, frame, results):

        for box in results.boxes:

            cls = int(box.cls[0])

            # vehicle classes
            if cls in [2, 3, 5, 7]:

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cx = int((x1 + x2) / 2)
                cy = int((y1 + y2) / 2)

                if self.line_y - 5 < cy < self.line_y + 5:
                    self.count += 1

                cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

        cv2.line(
            frame,
            (0, self.line_y),
            (frame.shape[1], self.line_y),
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            f"Count: {self.count}",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

        return frame