import cv2
import numpy as np
import requests
from ultralytics import YOLO

# Load trained model
model = YOLO("best.pt")

# ESP32 snapshot URL
url = "http://192.168.63.89/capture"

print("✅ Detection started...")

names = model.names

while True:
    try:
        # Get image from ESP32
        response = requests.get(url, timeout=5)
        img_array = np.frombuffer(response.content, np.uint8)
        frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if frame is None:
            print("⚠️ Frame error")
            continue

        # YOLO detection
        results = model(frame, imgsz=320, conf=0.5)

        annotated = results[0].plot()

        # Print detected objects
        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                print("Detected:", names[cls])

        # Show output
        cv2.imshow("ESP32 Detection", annotated)

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except Exception as e:
        print("Error:", e)

cv2.destroyAllWindows()
