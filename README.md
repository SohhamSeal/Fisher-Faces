# Fisher Faces for Facial Recognition

## Introduction

Facial recognition, an innate ability of humans, presents challenges when transferred to machines. This project explores the use of Linear Discriminant Analysis (LDA) in facial recognition, offering practical insights into its application.

## Importance of Facial Recognition

Facial recognition, highlighted by a [2015 INTERPOL](https://www.interpol.int/en/How-we-work/Forensics/Facial-Recognition) release, is a superior method for non-intrusive surveillance. Despite its importance, challenges such as illumination, viewpoints, and facial expressions persist.

## Methodology

### Algorithm Overview

1. **Image Matrix Construction:** Flatten images into a matrix for subsequent analysis.
2. **Class-Specific Mean Vectors:** Derive $D$-dimensional mean vectors for each class.
3. **Global Mean Vector:** Calculate the $D$-dimensional global mean vector.
4. **Scatter Matrix Construction:** Build within-class $\(S_w\)$ and between-class $\(S_b\)$ scatter matrices.
5. **Eigenvalue and Eigenvector Computation:** Find the eigendecomposition of $\(S_w^{-1}S_b\)$.
6. **Dimensionality Reduction:** Rank eigenvalues, select top $S$ eigenvectors to create matrix $U$.
7. **Projection onto $S$-dimensional subspace:** Project the original image matrix onto the new subspace.

## Dataset

For the case study, Kaggle's celebrity dataset (link: [Celebrity Face Image Dataset](https://www.kaggle.com/datasets/vishesh1412/celebrity-face-image-dataset)) with 17 celebrities and 100 images each is used.

## Implementation

Check the [Python code](https://github.com/SohhamSeal/Fisher-Faces) for the LDA implementation from scratch. 
> [!NOTE]  
> The repository also includes separate ROI (Region of Interest) code segments and testing code segments that weren't mentioned in the paper.
> Referring to the repository provides everything in one place without having to do things manually.

## Usage

### Prerequisites

- Python
- Libraries: numpy, PIL

### Getting Started

1. Install required libraries.
2. Set dataset parameters (Z, C, M, N).
3. Run the provided Python code for image classification.

## Contact

For any inquiries, contact jothiram@nitk.edu.in.

