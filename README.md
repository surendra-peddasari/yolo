# YOLOv8 Projects: Person & Pose Detection

This repository hosts implementations of **YOLOv8** and **YOLOv8-Pose** for:
- 🔍 Person detection
- 🧍 Human pose estimation

It includes trained `.pt` weights, training results (CSV logs), dataset configs, and ready-to-run scripts for inference, training, and evaluation. The repo is organized for reproducibility, deployment, and quick experimentation.



## 📂 Repository Structure


yolov8_projects/
├── yolov8_person_detection/
│   ├── models/              # YOLOv8 person detection weights
│   ├── results/             # Training logs (CSV)
│   ├── data/                # Dataset configs
│   ├── scripts/             # Training, detection, evaluation scripts
│   └── README.md
├── yolov8_pose_detection/
│   ├── models/              # YOLOv8-Pose weights
│   ├── results/             # Training logs
│   ├── scripts/             # Training, detection, evaluation scripts
│   └── README.md
├── LICENSE
├── requirements.txt
└── .gitignore




## 🚀 Installation

```bash
git clone https://github.com/surendra-peddasari/yolo.git
cd yolo
pip install -r requirements.txt




## 🖼️ Usage

### Person Detection
```bash
python yolov8_projects/yolov8_person_detection/scripts/detect.py \
  --weights yolov8_projects/yolov8_person_detection/models/yolov8_person.pt \
  --source test_images/


### Pose Detection
```bash
python yolov8_projects/yolov8_pose_detection/scripts/pose_detect.py \
  --weights yolov8_projects/yolov8_pose_detection/models/yolov8_pose.pt \
  --source test_images/




## 📊 Results

Training metrics are logged in CSV files under each project’s `results/` folder.  
Example (YOLOv8 Person Detection):
- **Precision:** ~0.94  
- **Recall:** ~0.92  
- **mAP50:** ~0.96  
- **mAP50‑95:** ~0.89  



## 📜 License

This project is licensed under the MIT License.

