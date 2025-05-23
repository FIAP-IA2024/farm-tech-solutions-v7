# Standalone Python Script Development

## Description

Develop a standalone Python script that implements the YOLO model training, validation, and testing process. This script will run locally on your machine and execute all the necessary steps without requiring a Jupyter notebook environment.

## Instructions

1. Create a Python script in the `PROJECT_ROOT/src` directory with the exact same name as your Jupyter notebook will have: `GabrielRibeiro_rm560173_pbl_fase6.py`

   - Add a shebang line at the top: `#!/usr/bin/env python3`
   - Add proper documentation including project purpose and usage instructions
   - Implement command-line arguments using `argparse` for flexible execution:
     - `--epochs`: Number of training epochs (default: 30)
     - `--batch-size`: Batch size for training (default: 16)
     - `--img-size`: Input image size (default: 640)
     - `--weights`: Pre-trained weights to start with (default: 'yolov5s.pt')
     - `--data-path`: Path to the dataset (default: './data')
     - `--save-dir`: Directory to save results (default: './results')

2. Implement the following functionality:
   - Environment setup (clone YOLOv5 repository if needed)
   - Dataset configuration (create YAML configuration file)
   - Model training implementation
   - Validation on the validation set
   - Testing on the test set
   - Results analysis and visualization
   - Proper logging of progress and results

3. Ensure the script can run from the command line with appropriate output:

   ```bash
   python notebooks/GabrielRibeiro_rm560173_pbl_fase6.py --epochs 30 --batch-size 16
   ```

4. Make the script executable (if on Linux/Mac):

   ```bash
   chmod +x notebooks/GabrielRibeiro_rm560173_pbl_fase6.py
   ```

5. Test the script with different parameters to ensure it works correctly

## Important Notes

- This script MUST be executed locally on your machine before proceeding with the Jupyter notebook implementation.
- The script file name MUST exactly match the name of the Jupyter notebook you will create (with `.py` extension instead of `.ipynb`).
- Create the `src` directory if it doesn't exist already.
- All functionality that will be implemented in the Jupyter notebook must be available in this standalone script.
- Results from both the standalone script and the Jupyter notebook should be comparable.

## Validation Criteria

- Script is located in the `PROJECT_ROOT/src` directory
- Script has the correct file name format: `GabrielRibeiro_rm560173_pbl_fase6.py`
- Script runs successfully from the command line without errors
- All functionality (training, validation, testing) works correctly
- Results are properly saved and can be analyzed
- Code is well-documented and follows best practices
- Performance is comparable to the Jupyter notebook implementation

## Status

- [x] Completed
