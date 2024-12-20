# YOLOv8 Video Inference with OpenCV

This repository contains two Python scripts that leverage YOLOv8 for video-based object detection. The scripts allow you to perform inference either in real-time using a webcam or on a pre-recorded video.

## Features

- **Real-Time Inference**: Use the webcam to process live video streams.
- **Offline Inference**: Analyze and annotate a pre-recorded video file.
- **Performance Metrics**: Measure and display the inference time and FPS.
- **YOLOv8 Integration**: Utilize the YOLOv8 model for robust object detection.

## Prerequisites

Before running the scripts, ensure you have the following dependencies installed:

- Python 3.8 or higher
- OpenCV (`pip install opencv-python`)
- Ultralytics YOLO (`pip install ultralytics`)

## Scripts Overview

### 1. `VIDEO CAP.py`
This script uses the webcam to perform real-time object detection.

**How to Run:**
```bash
python "VIDEO CAP.py"
```

### 2. `COMPUTER VISION video.py`
This script processes a pre-recorded video file and performs object detection on each frame.

**How to Run:**
1. Place your video file in the desired directory.
2. Update the `video_path` variable in the script to point to your video file.
3. Run the script:
   ```bash
   python "COMPUTER VISION video.py"
   ```

## Configuration

Both scripts require a pre-trained YOLOv8 model. Update the model path in the following line:
```python
model = YOLO("/path/to/your/yolov8-model.pt")
```

### Real-Time Script (`VIDEO CAP.py`)
The camera index is set to `0` by default. Modify this line to use a different camera:
```python
cap = cv2.VideoCapture(0)
```

### Video Script (`COMPUTER VISION video.py`)
Replace `video_path` with the path to your video file:
```python
video_path = "/path/to/your/video.mp4"
```

## Output

- Annotated frames are displayed in a window named "YOLOv8 Inference".
- Press `q` to exit the program.

## Example Outputs

- **Real-Time Inference**:
  - Frames are processed and displayed with bounding boxes and labels for detected objects.
- **Video Inference**:
  - Annotated video frames are displayed with detection results.

## Troubleshooting

1. **Webcam Issues**:
   - Ensure no other application is using the webcam.
   - Try changing the camera index (`0`, `1`, etc.).

2. **Video File Not Opening**:
   - Verify the `video_path` is correct and points to a valid video file.

3. **Performance**:
   - Use a system with a dedicated GPU for faster inference.
   - Reduce the video resolution for better FPS.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [Ultralytics YOLO](https://github.com/ultralytics/yolov5) for the YOLOv8 framework.
- [OpenCV](https://opencv.org/) for video handling and visualization.

## Contributing

Feel free to open issues or submit pull requests to improve this project!
