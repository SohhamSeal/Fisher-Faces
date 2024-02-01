# Celebrity Face Image Dataset Processing

## Overview

This repository provides a solution for efficiently processing a celebrity face image dataset, specifically the [Celebrity Face Image Dataset on Kaggle](https://www.kaggle.com/datasets/vishesh1412/celebrity-face-image-dataset). The dataset, like many others, contains images of celebrities with various poses and backgrounds, making it essential to focus on the Region Of Interest (ROI) for accurate facial analysis.

## Problem Statement

The challenge arises due to the dataset's inclusion of images that extend beyond the desired ROI, including body parts and environmental backgrounds. Manually curating the dataset for facial images can be time-consuming and tedious. With approximately 1700 images in the dataset, automating the process becomes imperative for efficiency.

## Solution

To address this issue, the repository employs a Region Of Interest (ROI) capturing algorithm, specifically the Haar Cascade, which is implemented using the OpenCV library in Python. The Haar Cascade is a powerful template matching technique for object detection, widely used in computer vision applications.

### Haar Cascade in Facial Recognition: A Comprehensive Overview

#### Introduction

The Haar Cascade is a robust object detection algorithm widely applied in computer vision, specifically renowned for its efficacy in facial recognition tasks. Developed by Viola and Jones, the algorithm is grounded in the concept of Haar-like features, which are essentially local intensity variations in an image.

#### Haar-like Features

Haar-like features are rectangular patterns that help capture information about the distribution of pixel values in different regions of an image. These features serve as discriminative indicators, distinguishing between the characteristics of the object being sought and the background. Each Haar-like feature calculates the difference between the sum of pixel values in two adjacent regions, providing a distinctive measure.

#### Training the Cascade

One of the Haar Cascade's key strengths lies in its ability to be trained for specific object detection tasks. During training, a cascade of classifiers is generated through a two-step process. The first step involves selecting a subset of Haar-like features and evaluating their effectiveness in discriminating between positive and negative samples. The second step utilizes AdaBoost, an ensemble learning technique, to assign weights to these features based on their discriminatory power.

#### Integral Image and Adaboost

Integral Image, a crucial component of the Haar Cascade, facilitates rapid computation of Haar-like features. By precomputing the sum of pixel values for all image sub-regions, the Integral Image significantly expedites feature calculation during runtime. AdaBoost, on the other hand, assigns weights to features iteratively, allowing the algorithm to focus more on misclassified samples in subsequent rounds, thereby enhancing accuracy.

#### Sliding Window and Detection

The Haar Cascade operates using a sliding window approach, systematically moving across the image at different scales. At each position, the cascade of classifiers assesses whether the region within the sliding window contains the target object. If a region fails a classifier, it is promptly discarded, optimizing computation. Successful regions proceed through the cascade until the final classifier, determining whether the region contains the desired object.

#### Facial Recognition Applications

In facial recognition, Haar Cascade is instrumental in detecting faces within images. Its adaptability to various environments, robustness against occlusions, and speed make it an ideal choice for real-time applications. However, it's essential to acknowledge that while Haar Cascade excels in detecting frontal faces, its performance may diminish with non-frontal poses or variations in lighting conditions.

### Implementation in This Solution

The Haar Cascade is utilized to detect faces in images, providing a list of rectangular box coordinates representing the ROI. These coordinates are then used to crop the images, creating a new dataset that focuses solely on the facial region of celebrities. This refined dataset can be leveraged for various facial recognition and classification tasks.

## Getting Started

To execute this task, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python installed on your system.
3. Install the required libraries by running `pip install -r requirements.txt`.
4. Run the `init.py` script.
5. Enter the relative or absolute location of the dataset and the location where you want to save the processed files when prompted.

## Acknowledgments

This solution simplifies the process of preparing a celebrity face image dataset, making it more suitable for facial analysis tasks. The Haar Cascade algorithm, combined with automation, provides an efficient way to curate datasets for improved accuracy in facial recognition models.