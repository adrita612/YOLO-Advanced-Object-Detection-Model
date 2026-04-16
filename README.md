# YOLO-Advanced-Object-Detection-Model
You Only Look For Once is an interative model that uses deep learning features to detect objects, a vital simulation used in smart cities

Throughout this project, I was actively involved in both the technical implementation and workflow optimization of the YOLO-based object detection model. My main contributions included:
Setting up the dataset pipeline using the VISDrone dataset, including organizing image and label directories into the correct YOLO format
Configuring and training the YOLO model (Ultralytics framework), including tuning parameters such as batch size, confidence thresholds, and epochs
Running model inference and evaluation, interpreting outputs, and validating detection performance
Debugging file path issues and dataset inconsistencies, particularly when transitioning between environments
Managing the development workflow across platforms, specifically moving from local development (VS Code) to cloud-based training
A key contribution I made to this project was adapting the workflow to address hardware limitations. Since my laptop only supports CPU-based processing, training the YOLO model locally was extremely slow and not practical for the scope of this project. To resolve this, I transferred the training to Google Collab, where I could take advantage of GPU processing. This shift was significant in completing Part III (training) and Part IV (evaluation and prediction).
However, this transition introduced several additional challenges. Moving between a local Windows environment and Collab’s Linux-based system required careful restructuring of file paths and directories. Small inconsistencies in dataset organization often resulted in errors such as missing files during training or prediction. Managing the VISDrone dataset in a cloud environment also required extra steps, including uploading, extracting, and verifying the dataset structure before it could be used effectively.
Results for each experimental procedure and workflow of the YOLO model are outlined below. 
Baseline Results
Training behaviour-> Loss Curve
Both training and validation losses decrease smoothly, indicating stable convergence and effective learning.

Overfitting/underfitting
The similarity between training and validation loss indicates minimal overfitting and good generalization to unseen data.

MaP (Performance Metrics)
Precision ≈ 0.41
Recall ≈ 0.30
mAP@50 ≈ 0.30
mAP@50-95 ≈ 0.17

Metric
Meaning
Precision (0.41)
Moderate false positives
Recall (0.30)
Missing some objects
mAP50 (0.30)
Decent baseline
mAP50-95 (0.17)
Hard dataset (normal)


The model achieves moderate detection performance, with mAP@50 around 0.30, which is reasonable given the complexity and density of the VisDrone dataset.

Convergence Behaviour

No plateau so model did not fully converge

Class-wise Performance 
Strong classes:
car (~0.73 AP) ← VERY GOOD
bus (~0.39)
van (~0.33)
Weak classes:
bicycle (~0.06)
awning-tricycle (~0.10)
tricycle (~0.20)
The training and validation loss curves show a consistent downward trend, indicating stable convergence of the model. There is no significant gap between training and validation loss, suggesting that the model does not suffer from overfitting and generalizes well to unseen data.
Additionally, the model has not fully converged, as both loss and performance metrics continue to improve at later epochs. This suggests that further training could improve performance.
The absence of overfitting can be attributed to the large dataset size and the complexity of the VisDrone dataset, which contains dense scenes and small objects. However, performance limitations arise due to class imbalance and small object detection challenges, which affect recall and accuracy for minority classes.
Part III: Increasing Epoch Testing 

I opted to increase the epoch count from 30 to 50 as the performance metrics from the initial results did not yet reach a plateau. 

After Increasing Epoch from 30 -> 50 

Increasing the number of training epochs from 30 to 50 resulted in an improvement in overall detection performance, with mAP@50 increasing from approximately 0.30 to 0.325 and mAP@50-95 improving from 0.17 to 0.186. Recall also increased, indicating that the model was able to detect more objects. However, precision decreased slightly, suggesting an increase in false positive detections. This indicates a trade-off between recall and precision, where the model becomes more sensitive but less selective. Overall, the results suggest that the model had not fully converged at 30 epochs and benefited from additional training.

However, it can be seen that the metrics for performance have more variability than before. 	This would indicate that precision has been lost or efficiency of the model needs to be improved. This will be further evaluated in Part IV: Experimental Training. 
Part IV: Increasing image size to 800

In Part IV, the input image size was increased from 640 to 800 while keeping the rest of the training setup unchanged. This improvement was motivated by the VisDrone dataset’s small-object and dense-scene characteristics. The larger image size improved all major metrics, including precision, recall, mAP@50, and mAP@50-95. This suggests that increasing input resolution helped the model capture more detail and improved detection performance, especially for smaller targets.


Run
Setting
Precision
Recall
mAP50
mAP50-95
Baseline
30 epochs, 640
~0.41
~0.30
~0.30
~0.17
Part III
50 epochs, 640
~0.34
~0.32
~0.325
~0.186
Part IV
50 epochs, 800
~0.472
~0.373
~0.378
~0.224



Part V: YOLO Model Comparison 
The YOLOv8 model was evaluated using the VisDrone validation dataset. The model successfully detected multiple object classes including pedestrians, vehicles (cars, vans, trucks), and bicycles across dense urban scenes.
The prediction outputs show that the model is capable of detecting a high number of objects per image, which is expected given the complexity and density of the VisDrone Dataset. For example, individual images contained detections of over 50 vehicles along with multiple pedestrians simultaneously.
Key findings indicate that increasing image size plays a significant role in improving object detection performance during training. However, the VisDrone image size used in this model was limited, and a real-world application would likely involve larger-scale training with higher-resolution data. Despite this limitation, the project effectively demonstrates the general capabilities of a YOLO-based object detection system.

