#!/usr/bin/env python3

"""
Farm Tech Solutions - Computer Vision Project

This script implements a YOLO-based object detection system for agricultural applications.
It handles the training, validation, and testing of a YOLO model on the prepared dataset.

Usage:
    python GabrielRibeiro_rm560173_pbl_fase6.py --epochs 30 --batch-size 16
    
Author: Gabriel Ribeiro (RM560173)
Date: 2025-04-19
"""

import os
import sys
import argparse
import yaml
import logging
import shutil
import torch
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("yolo_training.log", mode="w"),
    ],
)


def parse_args():
    """
    Parse command line arguments for the script.

    Returns:
        argparse.Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="Train and evaluate YOLO model for agricultural object detection"
    )
    parser.add_argument(
        "--epochs", type=int, default=30, help="Number of training epochs"
    )
    parser.add_argument(
        "--batch-size", type=int, default=16, help="Batch size for training"
    )
    parser.add_argument("--img-size", type=int, default=640, help="Input image size")
    parser.add_argument(
        "--weights",
        type=str,
        default="yolov5s.pt",
        help="Pre-trained weights to start with",
    )
    parser.add_argument(
        "--data-path", type=str, default="./data", help="Path to the dataset"
    )
    parser.add_argument(
        "--save-dir", type=str, default="./results", help="Directory to save results"
    )
    parser.add_argument(
        "--compare",
        action="store_true",
        help="Run training with both 30 and 60 epochs for comparison",
    )

    return parser.parse_args()


def setup_yolov5():
    """
    Clone the YOLOv5 repository if it doesn't exist already.

    Returns:
        str: Path to the YOLOv5 repository
    """
    yolov5_path = Path("yolov5")

    if not yolov5_path.exists():
        logging.info("Cloning YOLOv5 repository...")
        os.system("git clone https://github.com/ultralytics/yolov5.git")
        os.system("pip install -r yolov5/requirements.txt")
        logging.info("YOLOv5 repository cloned and dependencies installed.")
    else:
        logging.info("YOLOv5 repository already exists.")

    return str(yolov5_path)


def generate_dataset_config(data_path):
    """
    Generate the YAML configuration file for the dataset.

    Args:
        data_path (str): Path to the dataset

    Returns:
        str: Path to the generated YAML config file
    """
    # Get the project root directory (parent directory of the data_path)
    project_root = os.path.abspath(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    # Convert relative data_path to absolute if needed
    if not os.path.isabs(data_path):
        abs_data_path = os.path.normpath(os.path.join(project_root, data_path))
    else:
        abs_data_path = os.path.normpath(data_path)

    # Ensure the path exists
    if not os.path.exists(abs_data_path):
        logging.error(f"Data path {abs_data_path} does not exist.")
        raise FileNotFoundError(f"Data path {abs_data_path} does not exist.")

    # Define absolute paths for train, val, and test directories
    train_path = os.path.normpath(os.path.join(abs_data_path, "train", "images"))
    val_path = os.path.normpath(os.path.join(abs_data_path, "val", "images"))
    test_path = os.path.normpath(os.path.join(abs_data_path, "test", "images"))

    # Verify that all required directories exist
    for path, name in [
        (train_path, "train"),
        (val_path, "validation"),
        (test_path, "test"),
    ]:
        if not os.path.exists(path):
            logging.warning(
                f"{name.capitalize()} images directory {path} does not exist."
            )

    dataset_config = {
        "path": abs_data_path,
        "train": train_path,
        "val": val_path,
        "test": test_path,
        "nc": 2,  # Number of classes
        "names": ["A_Cat", "B_Dog"],  # Class names
    }

    config_path = os.path.join(abs_data_path, "dataset.yaml")
    with open(config_path, "w") as f:
        yaml.dump(dataset_config, f, default_flow_style=False)

    logging.info(f"Dataset configuration generated at {config_path}")
    logging.info(
        f"Using the following paths:\n"
        f"  - Data path: {abs_data_path}\n"
        f"  - Train images: {train_path}\n"
        f"  - Validation images: {val_path}\n"
        f"  - Test images: {test_path}"
    )

    return str(config_path)


def train_model(
    yolov5_path, config_path, epochs, batch_size, img_size, weights, save_dir
):
    """
    Train the YOLO model with the specified parameters.

    Args:
        yolov5_path (str): Path to the YOLOv5 repository
        config_path (str): Path to the dataset config file
        epochs (int): Number of training epochs
        batch_size (int): Batch size for training
        img_size (int): Input image size
        weights (str): Pre-trained weights to start with
        save_dir (str): Directory to save results

    Returns:
        dict: Training results and paths
    """
    cwd = os.getcwd()

    # Convert paths to absolute before changing directory
    abs_config_path = os.path.abspath(config_path)
    abs_save_dir = os.path.abspath(save_dir)
    abs_weights = weights if os.path.isabs(weights) else os.path.join(cwd, weights)

    # Change to YOLOv5 directory
    os.chdir(yolov5_path)

    run_name = (
        f"train_e{epochs}_bs{batch_size}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    )

    train_cmd = f"python train.py --img {img_size} --batch {batch_size} --epochs {epochs} \
               --data {abs_config_path} --weights {abs_weights} --project {abs_save_dir} --name {run_name}"

    logging.info(
        f"Starting training with {epochs} epochs and batch size {batch_size}..."
    )
    logging.info(f"Running: {train_cmd}")

    os.system(train_cmd)

    # Return to original directory
    os.chdir(cwd)

    results_path = os.path.join(abs_save_dir, run_name)
    best_weights = os.path.join(results_path, "weights/best.pt")

    logging.info(f"Training completed. Results saved to {results_path}")

    return {
        "run_name": run_name,
        "results_path": results_path,
        "best_weights": best_weights,
    }


def validate_model(
    yolov5_path, config_path, best_weights, img_size, batch_size, save_dir
):
    """
    Validate the trained model on the validation set.

    Args:
        yolov5_path (str): Path to the YOLOv5 repository
        config_path (str): Path to the dataset config file
        best_weights (str): Path to the best weights from training
        img_size (int): Input image size
        batch_size (int): Batch size for validation
        save_dir (str): Directory to save results

    Returns:
        dict: Validation results
    """
    cwd = os.getcwd()

    # Convert paths to absolute before changing directory
    abs_config_path = os.path.abspath(config_path)
    abs_best_weights = os.path.abspath(best_weights)
    abs_save_dir = os.path.abspath(save_dir)

    # Change to YOLOv5 directory
    os.chdir(yolov5_path)

    run_name = (
        f"val_{Path(best_weights).stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    )
    val_cmd = f"python val.py --img {img_size} --batch {batch_size} \
             --data {abs_config_path} --weights {abs_best_weights} --project {abs_save_dir} --name {run_name} --task val"

    logging.info(f"Starting validation with weights {best_weights}...")
    logging.info(f"Running: {val_cmd}")

    os.system(val_cmd)

    # Return to original directory
    os.chdir(cwd)

    results_path = os.path.join(abs_save_dir, run_name)
    logging.info(f"Validation completed. Results saved to {results_path}")

    return {"run_name": run_name, "results_path": results_path}


def test_model(yolov5_path, config_path, best_weights, img_size, batch_size, save_dir):
    """
    Test the trained model on the test set.

    Args:
        yolov5_path (str): Path to the YOLOv5 repository
        config_path (str): Path to the dataset config file
        best_weights (str): Path to the best weights from training
        img_size (int): Input image size
        batch_size (int): Batch size for testing
        save_dir (str): Directory to save results

    Returns:
        dict: Test results
    """
    cwd = os.getcwd()

    # Convert paths to absolute before changing directory
    abs_config_path = os.path.abspath(config_path)
    abs_best_weights = os.path.abspath(best_weights)
    abs_save_dir = os.path.abspath(save_dir)

    # Path to test images relative to YOLOv5 directory
    abs_test_images = os.path.join(os.path.dirname(abs_config_path), "test/images")

    # Change to YOLOv5 directory
    os.chdir(yolov5_path)

    run_name = f"test_best_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    # Use absolute path to test images instead of relative path
    test_cmd = f"python detect.py --img {img_size} --source {abs_test_images} \
              --weights {abs_best_weights} --project {abs_save_dir} --name {run_name} --save-txt --save-conf"

    logging.info(f"Starting testing with weights {best_weights}...")
    logging.info(f"Running: {test_cmd}")

    os.system(test_cmd)

    # Return to original directory
    os.chdir(cwd)

    results_path = os.path.join(abs_save_dir, run_name)

    logging.info(f"Testing completed. Results saved to {results_path}")

    return {
        "run_name": run_name,
        "results_path": results_path,
    }


def compare_models(yolov5_path, config_path, img_size, batch_size, weights, save_dir):
    """
    Train and compare models with different epoch settings.

    Args:
        yolov5_path (str): Path to the YOLOv5 repository
        config_path (str): Path to the dataset config file
        img_size (int): Input image size
        batch_size (int): Batch size
        weights (str): Pre-trained weights to start with
        save_dir (str): Directory to save results

    Returns:
        dict: Comparison results
    """
    cwd = os.getcwd()

    # Convert paths to absolute before changing directory
    abs_config_path = os.path.abspath(config_path)
    abs_save_dir = os.path.abspath(save_dir)
    abs_weights = weights if os.path.isabs(weights) else os.path.join(cwd, weights)

    comparison_dir = os.path.join(abs_save_dir, "comparison")
    os.makedirs(comparison_dir, exist_ok=True)

    # Train with 30 epochs
    logging.info("Training model with 30 epochs...")
    train_30_results = train_model(
        yolov5_path,
        abs_config_path,
        30,
        batch_size,
        img_size,
        abs_weights,
        comparison_dir,
    )

    # Train with 60 epochs
    logging.info("Training model with 60 epochs...")
    train_60_results = train_model(
        yolov5_path,
        abs_config_path,
        60,
        batch_size,
        img_size,
        abs_weights,
        comparison_dir,
    )

    # Validate both models
    val_30_results = validate_model(
        yolov5_path,
        abs_config_path,
        train_30_results["best_weights"],
        img_size,
        batch_size,
        comparison_dir,
    )
    val_60_results = validate_model(
        yolov5_path,
        abs_config_path,
        train_60_results["best_weights"],
        img_size,
        batch_size,
        comparison_dir,
    )

    # Create comparison report
    report_path = os.path.join(comparison_dir, "comparison_report.md")
    with open(report_path, "w") as f:
        f.write("# YOLO Model Training Comparison Report\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        f.write("## 30 Epochs Model\n\n")
        f.write(f"- Training results: {train_30_results['results_path']}\n")
        f.write(f"- Validation results: {val_30_results['results_path']}\n")
        f.write(f"- Best weights: {train_30_results['best_weights']}\n\n")

        f.write("## 60 Epochs Model\n\n")
        f.write(f"- Training results: {train_60_results['results_path']}\n")
        f.write(f"- Validation results: {val_60_results['results_path']}\n")
        f.write(f"- Best weights: {train_60_results['best_weights']}\n\n")

        f.write("## Comparison Analysis\n\n")
        f.write(
            "For a detailed comparison of metrics, please refer to the validation results directories.\n\n"
        )
        f.write(
            "Generally, more epochs may lead to better model performance, but there is a risk of overfitting.\n"
        )
        f.write(
            "The comparison helps determine the optimal number of epochs for this specific dataset.\n"
        )

    logging.info(f"Comparison report generated at {report_path}")

    return {
        "train_30": train_30_results,
        "train_60": train_60_results,
        "val_30": val_30_results,
        "val_60": val_60_results,
        "report_path": report_path,
    }


def generate_report(train_results, val_results, test_results, save_dir):
    """
    Generate a comprehensive report of the model training, validation, and testing.

    Args:
        train_results (dict): Training results
        val_results (dict): Validation results
        test_results (dict): Test results
        save_dir (str): Directory to save the report

    Returns:
        str: Path to the generated report
    """
    report_path = os.path.join(save_dir, "model_report.md")

    with open(report_path, "w") as f:
        f.write("# YOLO Model Training and Evaluation Report\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        f.write("## Training Results\n\n")
        f.write(f"- Results directory: {train_results['results_path']}\n")
        f.write(f"- Best weights: {train_results['best_weights']}\n\n")

        f.write("## Validation Results\n\n")
        f.write(f"- Results directory: {val_results['results_path']}\n\n")

        f.write("## Test Results\n\n")
        f.write(f"- Results directory: {test_results['results_path']}\n\n")

        f.write("## Performance Analysis\n\n")
        f.write("### Metrics\n\n")
        f.write(
            "- Precision, Recall, and mAP scores can be found in the validation results directory.\n"
        )
        f.write("- Inference examples can be found in the test results directory.\n\n")

        f.write("### Suggestions for Improvement\n\n")
        f.write("1. More accurate image labels for better detection\n")
        f.write("2. Data augmentation techniques for better model generalization\n")
        f.write(
            "3. Testing different model architectures (YOLOv5s, YOLOv5m, YOLOv5l, etc.)\n"
        )

    logging.info(f"Report generated at {report_path}")

    return report_path


def main():
    """
    Main function to execute the YOLO model training, validation, and testing process.
    """
    args = parse_args()

    # Create save directory
    os.makedirs(args.save_dir, exist_ok=True)

    # Setup YOLOv5
    yolov5_path = setup_yolov5()

    # Generate dataset configuration
    config_path = generate_dataset_config(args.data_path)

    if args.compare:
        # Run comparison mode
        compare_models(
            yolov5_path,
            config_path,
            args.img_size,
            args.batch_size,
            args.weights,
            args.save_dir,
        )
    else:
        # Run normal mode
        train_results = train_model(
            yolov5_path,
            config_path,
            args.epochs,
            args.batch_size,
            args.img_size,
            args.weights,
            args.save_dir,
        )
        val_results = validate_model(
            yolov5_path,
            config_path,
            train_results["best_weights"],
            args.img_size,
            args.batch_size,
            args.save_dir,
        )
        test_results = test_model(
            yolov5_path,
            config_path,
            train_results["best_weights"],
            args.img_size,
            args.batch_size,
            args.save_dir,
        )

        # Generate report
        report_path = generate_report(
            train_results, val_results, test_results, args.save_dir
        )

        logging.info(f"All results saved to {args.save_dir}")
        logging.info(f"Report generated at {report_path}")


if __name__ == "__main__":
    main()
