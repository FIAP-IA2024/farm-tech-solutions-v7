# Dataset Splitting

## Description

Split the collected dataset into training, validation, and testing sets for both Object A and Object B. The proper division of data is crucial for developing an effective computer vision model.

## Instructions

1. From the 40 images of Object A:
   - Allocate 32 images for training
   - Allocate 4 images for validation
   - Allocate 4 images for testing
2. Apply the same distribution for the 40 images of Object B
3. Organize the images into appropriate folders with the following structure:

   ```plaintext
   data/
   ├── train/
   │   ├── images/
   │   └── labels/
   ├── val/
   │   ├── images/
   │   └── labels/
   └── test/
       ├── images/
       └── labels/
   ```

4. Ensure that the image distribution is balanced and representative

## Validation Criteria

- Training set: 64 images (32 for each object)
- Validation set: 8 images (4 for each object)
- Testing set: 8 images (4 for each object)
- Directory structure is correctly organized

## Status

- [x] Completed
