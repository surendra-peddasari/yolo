
from ultralytics import YOLO

model = YOLO("../models/yolov8_pose.pt")

metrics = model.val()
print(metrics)
