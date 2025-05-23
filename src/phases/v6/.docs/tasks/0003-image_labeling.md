# Image Labeling

## Description

Label all images in the training and validation sets using Make Sense IA. This step is crucial for preparing the dataset for YOLO training.

## Instructions

1. Visit the Make Sense IA website (<https://www.makesense.ai/>)
2. Upload the training images to the platform
3. Configure the labeling project:
   - Select "Object Detection" as the project type
   - Create label classes for Object A and Object B
4. For each image:
   - Draw bounding boxes around all instances of Object A and Object B
   - Ensure boxes are tight and accurate around the objects
   - Assign the correct class to each bounding box
5. Export the annotations in YOLO format
6. Save the label files in the corresponding `labels` directories (train/labels, val/labels)
7. Ensure each image has a corresponding .txt label file with the same name

## Validation Criteria

- All training and validation images have corresponding label files
- Label format is compatible with YOLO (class_id, x_center, y_center, width, height)
- Bounding boxes accurately surround the objects

## Status

- [x] Completed
