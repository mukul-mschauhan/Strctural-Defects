# SDNET2018 Concrete Crack Detection
## Overview
This repository contains an implementation of concrete crack detection using the **SDNET2018 dataset**, which includes over **56,000 images** of cracked and non-cracked concrete surfaces, such as bridge decks, walls, and pavements. The dataset is designed for training, validation, and benchmarking of AI-based crack detection algorithms, particularly focusing on **deep learning convolutional neural networks (CNNs)** for structural health monitoring.

## Dataset Description
- **Total Images:** 230 high-resolution images segmented into 256x256 px sub-images.
- **Categories:**
    * Bridge Decks: 54 images
    * Walls: 72 images
    * Pavements: 104 images
- **Labeling:**
  * Each sub-image is labeled as **'Cracked'** or **'Non-cracked'** based on the presence of cracks.
  * Crack Size Range: From as narrow as **0.06 mm** to as wide as **25 mm.**
  * **Challenges:** Dataset includes images with shadows, surface roughness, edges, holes, and background debris.

## Data Collection
**Equipment:** Captured using a 16 MP Nikon digital camera.
**Locations:**
**Bridge Decks:** SMASH laboratory, Utah State University.
**Walls:** Russell/Wanlass Performance Hall, USU campus.
**Pavements:** Roads and sidewalks on the USU campus.

## Purpose
The dataset serves as a benchmark for developing and evaluating crack detection algorithms using deep learning techniques, aiding in the advancement of **structural health monitoring systems.**

## Model Selection |📌 Key Advantages of ResNet (Residual Network):
1. **Skip Connections (Residual Learning):**

   * Allows information to bypass a few layers, solving vanishing gradient problems.
   * Useful for very deep networks without performance degradation.

2. **Depth without Overfitting:**

   * ResNet-50 has **50 layers** but performs better than shallower networks like VGGNet or AlexNet.
   * Greater depth enables the model to capture more complex patterns (like cracks, misalignments, etc.).

3. **Efficiency and Accuracy:**

   * Outperforms VGGNet and AlexNet with **fewer parameters** due to efficient use of residual blocks.
   * Ideal for detecting small, subtle cracks and defects with high precision.
