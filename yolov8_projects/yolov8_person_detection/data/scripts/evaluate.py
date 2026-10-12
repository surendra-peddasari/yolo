
from ultralytics import YOLO

model = YOLO("../models/yolov8_person.pt")

metrics = model.val()
print(metrics)
