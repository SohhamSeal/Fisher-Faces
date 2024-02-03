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

## Dataset Preprocessing (optional)

### Face Cropping using [ROI code](Code\Preprocessing\init.py)

The original dataset contains images with improperly cropped faces, as shown below:

![Improperly Cropped Face #1](https://github.com/SohhamSeal/Fisher-Faces/blob/main/Dataset/Celebrity%20Faces%20Dataset/Denzel%20Washington/007_1f6f632a.jpg?raw=true)
![Improperly Cropped Face #2](https://github.com/SohhamSeal/Fisher-Faces/blob/main/Dataset/Celebrity%20Faces%20Dataset/Jennifer%20Lawrence/067_2cd39306.jpg?raw=true)

To address this, the dataset needs to be cropped to focus solely on the facial features. Manual cropping is accurate but tedious. Therefore, we utilize the HAAR Cascade library to identify facial markers for template matching. Subsequently, we crop the images and save them in a separate location uing the [ROI code](Code\Preprocessing\init.py). You can find it in this [folder](Code\Preprocessing).
