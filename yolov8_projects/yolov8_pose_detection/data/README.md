
---

## 📄 `yolov8_pose_detection/README.md`

```markdown
# YOLOv8-Pose Detection

This project implements **YOLOv8-Pose** for human pose estimation.  
It includes trained weights, training logs, and scripts for inference, training, and evaluation.

---

## 📂 Contents
- **models/** → `yolov8_pose.pt` (trained weights)
- **results/** → `pose_results.csv` (training metrics)
- **scripts/** → Python scripts for training, detection, and evaluation

---

## 🚀 Usage

### Inference
Run pose estimation on images or videos:
```bash
python scripts/pose_detect.py --weights models/yolov8_pose.pt --source test_images/