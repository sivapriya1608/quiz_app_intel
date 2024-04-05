

# Student Assist

This repository hosts a collection of Python scripts for various AI applications, including drowsiness detection, question answering model fine-tuning, YouTube video analysis and quiz generation, and text summarization using the T5 model. Each application is accessible through a Streamlit interface for ease of use and interaction.

## Drowsiness Detection

### Overview

The drowsiness detection script utilizes facial landmark detection and convolutional neural networks (CNNs) for real-time analysis of eye status to determine whether the eyes are open or closed.

### How It Works

1. **Dependencies**:
   - Ensure the installation of necessary dependencies including PIL, face_recognition, opencv-python, tensorflow, scikit-learn, and keras.

2. **Functionality**:
   - The script includes functions for eye cropping, loading images from folders, model definition, training, and real-time detection using a webcam.

### Usage

1. Clone the repository to your local machine.
2. Install required dependencies.
3. Prepare your dataset by organizing images of open and closed eyes into separate folders.
4. Train the model by executing the main script.
5. Run the `webcam.py` script to detect drowsiness in real-time using a webcam.

## Question Answering Model Fine-Tuning (LLM)

### Overview

This script demonstrates fine-tuning a question answering model using the SQuAD dataset and evaluating its performance in different inference modes including Floating Point 32 (FP32), BFloat16 (BF16), and TorchScript. The script highlights the performance benefits of using Intel Extension for PyTorch (IPEX) for optimizing the model for inference.

### Setup Instructions

1. Install required packages.
2. Configure Intel Extension for PyTorch (IPEX) in your environment.
3. Set up the SQuAD dataset and load the pre-trained model and tokenizer from Hugging Face Transformers library.

### Usage

1. Ensure all required dependencies are installed.
2. Run the script in a Python environment with access to the necessary resources.
3. Review the output which includes inference times and speedup comparisons.
4. Visualize the results using the generated bar charts.

## YouTube Video Analysis and Quiz Generation

### Overview

This script extracts YouTube video IDs from URLs, retrieves captions using the YouTube Transcript API, generates quiz questions using an OpenAI Language Model (LLM), and transforms the questions into a structured format.

### Prerequisites

- Install required packages including pytube, youtube_transcript_api, and transformers.

### Usage

1. Extract YouTube video IDs and retrieve captions.
2. Feed captions into LLM for quiz question generation.
3. Transform output into a structured quiz format.

## Text Summarization with T5 Model

### Overview

This script fine-tunes a T5 model using the `billsum` dataset for text summarization and compares inference performance between FP32 and BF16 precision.

### Usage

1. Fine-tune the T5 model on the `billsum` dataset using the provided script.
2. Compare inference performance between FP32 and BF16 precision using the provided script.

### Dependencies

- Python 3.x
- PyTorch
- Transformers
- Datasets
- Intel Extension for PyTorch (IPEX)

