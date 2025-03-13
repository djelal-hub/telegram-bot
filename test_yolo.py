from ultralytics import YOLO

# Load a pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")

# Run object detection on an example image
results = model("example.jpg")

# Loop through each result and show it
for result in results:
    result.show()

