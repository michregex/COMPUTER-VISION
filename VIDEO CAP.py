import cv2
from ultralytics import YOLO
import time


model = YOLO("yolov8x-seg.pt")


cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("erron in file opening!")
    exit()

while cap.isOpened():
    success, frame = cap.read() 
    
    if not success:  
        print("end or error")
        break
    
  
    start = time.perf_counter()
    result = model(frame)
    end = time.perf_counter()
    total_time = end - start
    fps = 1 / total_time
    print(f"inference completed {total_time:.2f}s ({fps:.2f} FPS)")
    
    
    annotated_frame = result[0].plot()
    

    cv2.imshow("YOLOv8 Inference", annotated_frame)
    
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
