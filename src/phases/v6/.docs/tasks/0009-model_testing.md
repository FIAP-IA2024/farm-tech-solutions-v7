# Model Testing

## Description

Test the trained YOLO model on the test dataset to evaluate its real-world performance and generate visual results for demonstration.

## Instructions

1. Load the best-performing model weights from the training phase
2. Run inference on the test dataset (4 images of Object A and 4 images of Object B)
3. Generate visualization of detections:
   - Bounding boxes around detected objects
   - Class labels and confidence scores
   - Save processed images with annotations
4. Evaluate model performance on test data:
   - Precision, recall, and mAP
   - False positive and false negative rates
   - Detection speed (FPS)
5. Document test results in the notebook with screenshots of detection results
6. Save compelling visual results to include in the final presentation

## Validation Criteria

- Model successfully detects objects in test images
- Detection visualizations are clear and properly annotated
- Test metrics are calculated and documented
- High-quality visual examples saved for demonstration

## Status

- [x] Completed
