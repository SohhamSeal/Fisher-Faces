# Celebrity Face Image Dataset Processing

> [!NOTE]  
> This preprocessing step is optional, depending on the type of available data. Proceeding without preprocessing is feasible, but it's essential to note that skipping this step may lead to a notable decrease in accuracy.

## Overview

This repository presents a comprehensive solution for the streamlined processing of a celebrity face image dataset, specifically the [Celebrity Face Image Dataset on Kaggle](https://www.kaggle.com/datasets/vishesh1412/celebrity-face-image-dataset). Similar to many other datasets, this collection features images of celebrities captured in diverse poses and backgrounds, necessitating a focused approach towards the Region Of Interest (ROI) for precise facial analysis.

However, it's crucial to note that the considerations for ROI become particularly pertinent in scenarios resembling the dataset's structure. In cases where images resemble mugshots or follow a similar pattern, such as passport photos, the need for meticulous ROI analysis is less pronounced. These images are inherently well-curated, typically comprising 80-85% of the entire frame dedicated solely to the face. In such instances, the conventional concerns regarding diverse poses and backgrounds become less relevant, simplifying the facial analysis process.

## Problem Statement

The challenge arises due to the dataset's inclusion of images that extend beyond the desired ROI, including body parts and environmental backgrounds. Manually curating the dataset for facial images can be time-consuming and tedious. With approximately 1700 images in the dataset, automating the process becomes imperative for efficiency.

## Solution

To address this issue, the repository employs a Region Of Interest (ROI) capturing algorithm, specifically the Haar Cascade, which is implemented using the OpenCV library in Python. The Haar Cascade is a powerful template matching technique for object detection, widely used in computer vision applications.

### Introduction to Haar Cascade ([see](https://github.com/opencv/opencv/tree/master/data/haarcascades))

The Haar Cascade is a robust object detection algorithm widely applied in computer vision, specifically renowned for its efficacy in facial recognition tasks. Developed by Viola and Jones, the algorithm is grounded in the concept of Haar-like features, which are essentially local intensity variations in an image.

#### Haar-like Features

Haar-like features are rectangular patterns that help capture information about the distribution of pixel values in different regions of an image. These features serve as discriminative indicators, distinguishing between the characteristics of the object being sought and the background. Each Haar-like feature calculates the difference between the sum of pixel values in two adjacent regions, providing a distinctive measure.

#### Training the Cascade

One of the Haar Cascade's key strengths lies in its ability to be trained for specific object detection tasks. During training, a cascade of classifiers is generated through a two-step process. The first step involves selecting a subset of Haar-like features and evaluating their effectiveness in discriminating between positive and negative samples. The second step utilizes AdaBoost, an ensemble learning technique, to assign weights to these features based on their discriminatory power.

#### Integral Image and Adaboost

Integral Image, a crucial component of the Haar Cascade, facilitates rapid computation of Haar-like features. By precomputing the sum of pixel values for all image sub-regions, the Integral Image significantly expedites feature calculation during runtime. AdaBoost, on the other hand, assigns weights to features iteratively, allowing the algorithm to focus more on misclassified samples in subsequent rounds, thereby enhancing accuracy.

#### Sliding Window and Detection

The Haar Cascade operates using a sliding window approach, systematically moving across the image at different scales. At each position, the cascade of classifiers assesses whether the region within the sliding window contains the target object. If a region fails a classifier, it is promptly discarded, optimizing computation. Successful regions proceed through the cascade until the final classifier, determining whether the region contains the desired object.

### Implementation in This Solution

The Haar Cascade is utilized to detect faces in images, providing a list of rectangular box coordinates representing the ROI. These coordinates are then used to crop the images, creating a new dataset that focuses solely on the facial region of celebrities. This refined dataset can be leveraged for various facial recognition and classification tasks.

### HAAR Cascade Limitations
 
While HAAR Cascade filtering is effective, it is not infallible. In some cases, the cascade may fail to accurately crop only the facial region. It might mistakenly identify small facial features as a complete face and crop accordingly.

To mitigate this, we have the following options:

1. **Manual Verification:** Manually review and correct images where the HAAR Cascade fails.
2. **Ignore Unreliable Images:** Exclude images where the HAAR Cascade performs poorly from further analysis.

## Acknowledgments

This solution simplifies the process of preparing a celebrity face image dataset, making it more suitable for facial analysis tasks. The Haar Cascade algorithm, combined with automation, provides an efficient way to curate datasets for improved accuracy in facial recognition models.
