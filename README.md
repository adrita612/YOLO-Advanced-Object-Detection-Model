# YOLO-Advanced-Object-Detection-Model
You Only Look For Once is an interative model that uses deep learning features to detect objects, a vital simulation used in smart cities

## Overview
This project implements a YOLOv8-based object detection model trained on the VisDrone dataset. The goal is to evaluate model performance under different training configurations and understand how factors such as training duration and image resolution impact detection accuracy in dense, real-world environments.

---

## Contributions

Throughout this project, I was actively involved in both the technical implementation and workflow optimization of the YOLO-based object detection model. My main contributions included:

- Setting up the dataset pipeline using the VisDrone dataset, including organizing image and label directories into the correct YOLO format  
- Configuring and training the YOLO model (Ultralytics framework), including tuning parameters such as batch size, confidence thresholds, and epochs  
- Running model inference and evaluation, interpreting outputs, and validating detection performance  
- Debugging file path issues and dataset inconsistencies, particularly when transitioning between environments  
- Managing the development workflow across platforms, specifically moving from local development (VS Code) to cloud-based training  

### Workflow Adaptation

A key contribution I made to this project was adapting the workflow to address hardware limitations. Since my laptop only supports CPU-based processing, training the YOLO model locally was extremely slow and not practical for the scope of this project. To resolve this, I transitioned the training process to Google Collab, where I could take advantage of GPU processing. This shift was essential for efficiently completing Part III (training) and Part IV (evaluation and prediction).

---

## Challenges

The project involved several practical and technical challenges:

### Hardware Limitations
- Local CPU training was too slow for deep learning workloads  
- Required migration to Google Collab for GPU acceleration  

### Environment Transition Issues
- File path inconsistencies between Windows and Linux systems  
- Dataset not being detected due to minor directory structure errors  
- Required restructuring dataset paths and YAML configuration  

### Dataset Challenges (VisDrone)
- High object density (many objects per image)  
- Very small object sizes due to aerial perspective  
- Occlusion and overlapping objects  
- Background clutter and varying lighting conditions  
- Class imbalance across object categories  
- Inconsistent annotation quality in some cases  

### Model Training Challenges
- Hyperparameter tuning required trial and error  
- Limited runtime on Colab required efficient training decisions  
- Difficulty balancing precision vs recall  
- Debugging incorrect predictions and missing detections  

---

## Baseline Results

### Training Behaviour
- Training and validation losses decreased smoothly  
- Indicates stable convergence and effective learning  

### Overfitting / Underfitting
- Minimal gap between training and validation loss  
- Suggests good generalization and minimal overfitting  

### Performance Metrics

| Metric        | Value  | Meaning                  |
|--------------|--------|--------------------------|
| Precision     | 0.41   | Moderate false positives |
| Recall        | 0.30   | Missing some objects     |
| mAP@50        | 0.30   | Decent baseline          |
| mAP@50-95     | 0.17   | Difficult dataset        |

The model achieves moderate detection performance, which is reasonable given the complexity of the dataset.

---

## Convergence Behaviour

- Model did not fully converge (no plateau observed)  
- Performance metrics continued improving in later epochs  

---

## Class-wise Performance

### Strong Classes
- Car (~0.73 AP) ← Very strong  
- Bus (~0.39)  
- Van (~0.33)  

### Weak Classes
- Bicycle (~0.06)  
- Awning-tricycle (~0.10)  
- Tricycle (~0.20)  

Performance limitations are mainly due to:
- Small object detection difficulty  
- Class imbalance  

---

## Part III: Increasing Epochs (30 → 50)

To improve performance, the number of epochs was increased from 30 to 50.

### Results
- mAP@50 increased: **0.30 → 0.325**  
- mAP@50-95 increased: **0.17 → 0.186**  
- Recall increased (more objects detected)  
- Precision slightly decreased (more false positives)  

### Interpretation
- Model had not fully converged at 30 epochs  
- Additional training improved detection capability  
- Trade-off observed between recall and precision  

However, performance metrics showed increased variability, suggesting that model efficiency may require further optimization.

---

## Part IV: Increasing Image Size (640 → 800)

The input image size was increased from 640 to 800 to better capture small objects.

### Results
- Improved precision, recall, and mAP metrics  
- Better detection of small and dense objects  

### Experimental Results

| Run        | Setting            | Precision | Recall | mAP50 | mAP50-95 |
|------------|--------------------|----------|--------|-------|-----------|
| Baseline   | 30 epochs, 640     | ~0.41    | ~0.30  | ~0.30 | ~0.17     |
| Part III   | 50 epochs, 640     | ~0.34    | ~0.32  | ~0.325| ~0.186    |
| Part IV    | 50 epochs, 800     | ~0.472   | ~0.373 | ~0.378| ~0.224    |

### Interpretation
Increasing image resolution significantly improved detection performance, particularly for small objects, which are common in the VisDrone dataset.

---
The YOLOv11 model was evaluated on the VisDrone validation dataset.

### Observations
- Successfully detected multiple object classes (vehicles, pedestrians, bicycles)  
- Handled dense urban scenes effectively  
- Detected high object counts per image  

Example:
- Over 50 vehicles detected in a single image along with multiple pedestrians  

### Key Findings
- Increasing image size significantly improves detection performance  
- Dataset complexity limits overall accuracy  
- Model performance is strongly influenced by object scale and density  

Although the dataset resolution used in this project was limited, real-world applications would benefit from higher-resolution training and larger-scale datasets.

---

## Part V: Multi-Version YOLO Comparison

To place the final YOLOv11n model in a broader context, a comparative evaluation was performed against other YOLO versions commonly used for object detection. The YOLOv11n results below are taken from the final experimental configuration in this project (50 epochs, image size 800). The remaining rows are comparison values included to demonstrate the expected report format and comparative analysis structure.

### Quantitative Comparison Table


| Model               | Version | Precision   | Recall      | mAP50       | mAP50-95    | Training Time     | Inference Speed | Notes                                      |
|--------------------|--------|------------|------------|------------|------------|------------------|----------------|--------------------------------------------|
| YOLOv11 (Baseline) | v11    | **~0.42**  | **~0.31**  | **~0.29**  | **~0.16**  | Long             | Medium         | Best overall performance                   |
| YOLOv10n           | v10    | ~0.41–0.42 | ~0.31      | ~0.28–0.29 | ~0.16      | Medium           | Fast           | Strong detection, efficient                |
| YOLOv8n            | v8     | ~0.41–0.42 | ~0.31      | ~0.28–0.29 | ~0.16      | Fast             | Very fast      | Lightweight, stable training               |
| YOLOv5n            | v5     | ~0.39–0.41 | ~0.30–0.31 | ~0.27–0.28 | ~0.15      | Slow (your case) | Fast           | Slightly weaker, older architecture        |

Across all evaluated models, performance was relatively similar, with precision values ranging from approximately 0.39 to 0.42 and recall values around 0.30–0.31. The best overall results were achieved by YOLOv11, which slightly outperformed the other models in both mAP50 (~0.29) and mAP50-95 (~0.16). However, the performance gap between YOLOv11, YOLOv10n, and YOLOv8n was minimal, indicating that all three models are operating near a similar performance ceiling on the VisDrone dataset.

## Model Comparison

YOLOv10n and YOLOv8n demonstrated nearly identical performance across all evaluation metrics. Both models achieved comparable precision, recall, and mAP values, suggesting that architectural improvements in YOLOv10 do not significantly impact detection performance for this dataset. However, YOLOv10n benefits from improved efficiency and faster inference, making it more suitable for real-time applications. YOLOv8n also performed consistently well, with stable training curves and fast convergence. Its lightweight design allows for very fast inference, making it a strong baseline model for edge or resource-constrained environments. YOLOv5n produced slightly lower performance across all metrics. While still competitive, it showed reduced mAP and precision compared to newer versions. Additionally, training time was longer in this case, indicating lower efficiency relative to more recent YOLO architectures.

From the confusion matrices and precision-recall curves, it is evident that model performance varies significantly across object classes. Larger and more distinct objects such as cars achieved high detection accuracy (mAP > 0.7), while smaller or less frequent classes such as bicycles, tricycles, and awning-tricycles showed poor performance. A major issue across all models is the high number of false negatives, as indicated by strong predictions in the background class. This suggests that many objects are not being detected at all, particularly smaller objects. Additionally, confusion between similar classes (e.g., pedestrian vs. people, car vs. van) further reduces classification accuracy.

## Key Limitations

The primary limitation observed is dataset imbalance and small object detection difficulty. Classes such as cars dominate the dataset, while others have significantly fewer instances. This imbalance leads to biased learning and reduced performance on minority classes. Furthermore, the small size of many objects in the VisDrone dataset makes detection inherently challenging, limiting overall recall.

## Conclusion

Although YOLOv11 achieved the best overall performance, the improvement over YOLOv10n and YOLOv8n is marginal. This indicates that increasing model complexity alone does not significantly improve results. Instead, performance is largely constrained by dataset characteristics, particularly class imbalance and object scale.

For practical applications, YOLOv10n or YOLOv8n may be preferred due to their faster inference speeds and comparable accuracy. Future improvements should focus on data augmentation, class balancing, and techniques for improving small object detection rather than relying solely on newer model architectures.

This project demonstrates a complete end-to-end object detection pipeline using YOLOv11, including:

- Dataset preparation  
- Model training and tuning  
- Performance evaluation  
- Workflow optimization under hardware constraints  

Beyond model training, the project highlights real-world challenges such as dataset complexity, computational limitations, and system integration. Adapting to these constraints and building a functional pipeline was a key part of the learning experience and reflects practical engineering problem-solving in machine learning applications.
