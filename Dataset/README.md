# Celebrity Faces Dataset

## Overview

This dataset has been sourced from [Kaggle's collection of celebrity faces](https://www.kaggle.com/datasets/vishesh1412/celebrity-face-image-dataset). It comprises images of 17 renowned Hollywood celebrities, each with 100 images. The celebrities included in this dataset are:

- Angelina Jolie
- Brad Pitt
- Denzel Washington
- Hugh Jackman
- Jennifer Lawrence
- Johnny Depp
- Kate Winslet
- Leonardo DiCaprio
- Megan Fox
- Natalie Portman
- Nicole Kidman
- Robert Downey Jr.
- Sandra Bullock
- Scarlett Johansson
- Tom Cruise
- Tom Hanks
- Will Smith

## Dataset Preprocessing

### Face Cropping

The original dataset contains images with improperly cropped faces, as shown below:

![Improperly Cropped Face #1](https://github.com/SohhamSeal/Eigen-Faces/blob/main/Dataset/Celebrity%20Faces%20Dataset/Angelina%20Jolie/009_fb3e6174.jpg?raw=true)
![Improperly Cropped Face #2](https://github.com/SohhamSeal/Eigen-Faces/blob/main/Dataset/Celebrity%20Faces%20Dataset/Tom%20Hanks/012_39efc245.jpg?raw=true)

To address this, the dataset needs to be cropped to focus solely on the facial features. Manual cropping is accurate but tedious. Therefore, we utilize the HAAR Cascade library to identify facial markers for template matching. Subsequently, we crop the images and save them in a separate location uing the [ROI code](https://github.com/SohhamSeal/Eigen-Faces/blob/main/ROI_Cropping.ipynb). You can find it in this [folder](https://github.com/SohhamSeal/Eigen-Faces/tree/main/Dataset/Cropped%20Celebrity%20Faces%20Dataset).

### HAAR Cascade Limitations
 
While HAAR Cascade filtering is effective, it is not infallible. In some cases, the cascade may fail to accurately crop only the facial region. It might mistakenly identify small facial features as a complete face and crop accordingly.

To mitigate this, we have the following options:

1. **Manual Verification:** Manually review and correct images where the HAAR Cascade fails.
2. **Ignore Unreliable Images:** Exclude images where the HAAR Cascade performs poorly from further analysis.
