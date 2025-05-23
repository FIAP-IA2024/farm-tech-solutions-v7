# Multiple Epoch Training Comparison

## Description

Perform multiple training runs with different epoch settings to compare model performance and determine the optimal configuration for the YOLO model.

## Instructions

1. Set up two different training configurations:
   - Configuration 1: Train the model with 30 epochs
   - Configuration 2: Train the model with 60 epochs
2. Keep all other hyperparameters consistent between the two runs
3. Record the following metrics for each configuration:
   - Training and validation loss
   - Precision, recall, and mAP@0.5
   - mAP@0.5:0.95 (COCO metric)
   - Training time
   - GPU utilization
4. Save model weights from both training runs for later comparison

## Validation Criteria

- Both training configurations complete successfully
- Training metrics and logs are saved for both configurations
- Model weights are saved for both configurations
- Data is properly organized for comparison analysis

## Status

- [x] Completed
