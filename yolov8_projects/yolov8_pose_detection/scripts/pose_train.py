
from ultralytics import YOLO

model = YOLO("yolov8n-pose.pt")

model.train(
    data="coco8-pose.yaml",
    epochs=50,
    imgsz=640
)
