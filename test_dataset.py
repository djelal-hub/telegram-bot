from ultralytics import YOLO

# Load the dataset YAML
dataset_yaml = "C:/Users/Babid/Desktop/Detection bag logo.v3-dataset-definitivo.yolov8/data.yaml"

# Load a YOLOv8 model (you can use 'yolov8n.pt' for now)
model = YOLO("yolov8n.pt")

# Check if the dataset loads properly
model.train(data=dataset_yaml, epochs=1, imgsz=640, batch=1)
