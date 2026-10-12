# YOLOv8 Person Detection

This project implements **YOLOv8** for detecting people in images and videos.  
It includes trained weights, training logs, and scripts for inference, training, and evaluation.

---

## 📂 Contents
- **models/** → `yolov8_person.pt` (trained weights)
- **results/** → `results.csv` (training metrics)
- **data/** → `dataset.yaml` (dataset configuration)
- **scripts/** → Python scripts for training, detection, and evaluation

---

## 🚀 Usage

### Inference
Run detection on images or videos:
```bash
python scripts/detect.py --weights models/yolov8_person.pt --source test_images/