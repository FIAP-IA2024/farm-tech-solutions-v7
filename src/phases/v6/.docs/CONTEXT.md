# Project Context

## Project Overview

Academic project for FIAP focused on solutions for the agricultural sector using computer vision. The data consists of labeled images with corresponding `.txt` files, stored in `/data`.

## Dataset

### Organization

The dataset has been reorganized in YOLO format with the following structure:

```plaintext
data/  
├── train/  
│   ├── images/  (64 images: 32 of Object A, 32 of Object B)  
│   └── labels/  (64 corresponding label files)  
├── val/  
│   ├── images/  (8 images: 4 of Object A, 4 of Object B)  
│   └── labels/  (8 corresponding label files)  
└── test/  
    ├── images/  (8 images: 4 of Object A, 4 of Object B)  
    └── labels/  (8 corresponding label files)  
```

### Proper Data Distribution

- 80% of the dataset allocated to training (64 images)  
- 10% allocated to validation (8 images)  
- 10% allocated to testing (8 images)  
- Balanced representation of Object A and B maintained in each split  

## Development

### Current Progress

- Dataset organized and labeled locally.
- Task structure created in `/docs/tasks`.
- Task 1 (dataset organization) completed.
- Task 2 (dataset splitting) completed.
- Task 3 (image labeling) completed.
- Task 4 (standalone Python script) completed.
- Task 6 (YOLO model training) completed.
- Task 7 (multiple epoch training) completed.
- Task 8 (results analysis) completed.
- Task 9 (model testing) completed.

### Completed Tasks

- 0001-dataset_organization.md
- 0002-dataset_splitting.md
- 0003-image_labeling.md
- 0004-standalone_python_script.md
- 0006-yolo_model_training.md
- 0007-multiple_epoch_training.md
- 0008-results_analysis.md
- 0009-model_testing.md

### Task Sequence

1. Dataset Organization ✓
2. Dataset Splitting ✓
3. Image Labeling ✓
4. Standalone Python Script Development ✓
5. Jupyter Notebook Setup
6. YOLO Model Training ✓
7. Multiple Epoch Training ✓
8. Results Analysis ✓
9. Model Testing ✓
10. GitHub Documentation
11. Demonstration Video

### Important Notes

- Execution has been successfully done locally with the Python script before migrating to Google Colab.
- The standalone Python script implements YOLO model training, validation, and testing with flexible command-line arguments.
- YOLOv5 repository is automatically set up and configured by the script.
- Standalone Python script must be named `GabrielRibeiro_rm560173_pbl_fase6.py` to maintain consistency with the Jupyter notebook name.
- Detailed comparison between models trained for 30 and 60 epochs was performed, with the 30-epoch model showing better performance overall.

### Last Updated

2025-04-30T14:15:00-03:00
