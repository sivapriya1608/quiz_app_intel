**Drowsiness Detection**

This repository contains a Python script for detecting drowsiness using a webcam. The script utilizes facial landmark detection and convolutional neural networks (CNNs) for real-time analysis of eye status to determine whether the eyes are open or closed.

### How It Works

1. **Dependencies**:
   - Ensure you have the following dependencies installed:
     - `PIL` (Python Imaging Library)
     - `face_recognition`
     - `opencv-python` (cv2)
     - `tensorflow`
     - `scikit-learn`
     - `keras`

2. **Eye Cropper Function** (`eye_cropper`):
   - This function extracts the eye region from an image using facial landmark detection.
   - It converts the image to grayscale and detects facial landmarks using `face_recognition`.
   - The function calculates the bounding box for the eye region and crops it.
   - Finally, it resizes the cropped region to 80x80 pixels for processing.

3. **Load Images from Folder Function** (`load_images_from_folder`):
   - This function loads images of open and closed eyes from specified folders.
   - It resizes each image to 80x80 pixels and appends it to a list along with its corresponding label.

4. **Load and Preprocess Data**:
   - Images of open and closed eyes are loaded from specified folders.
   - The images and labels are preprocessed for training.

5. **Define CNN Model**:
   - A CNN model is defined using `Sequential` API from Keras.
   - It consists of convolutional layers followed by max-pooling layers for feature extraction.
   - Dense layers are added for classification, with dropout layers to prevent overfitting.
   - The output layer has a single neuron with sigmoid activation for binary classification.

6. **Compile and Train Model**:
   - The model is compiled with binary cross-entropy loss and Adam optimizer.
   - It's trained on the preprocessed training data for a specified number of epochs.

7. **Model Response Function** (`model_response`):
   - This function takes an image path and the trained model as input.
   - It extracts the eye region using the `eye_cropper` function.
   - If no eye region is found, it returns 'Yes'.
   - The eye region is normalized and passed through the trained model for prediction.
   - If the predicted probability of closed eyes is less than a specified threshold, it returns 'No'; otherwise, it returns 'Yes'.

8. **Webcam Script Execution**:
   - The main script runs a separate Python script named `webcam.py` using the command `!python webcam.py`.
   - The `webcam.py` likely contains code to capture video from a webcam, process frames, and call the `model_response` function to detect drowsiness in real-time.

### Usage
1. Clone this repository to your local machine.
2. Install the required dependencies.
3. Prepare your dataset by organizing images of open and closed eyes into separate folders.
4. Update the paths to your dataset folders in the main script.
5. Train the model by executing the main script.
6. Run the `webcam.py` script to detect drowsiness in real-time using a webcam.

