# Student Assist Repository

Welcome to the Student Assist repository! This collection of Python scripts covers various AI applications to assist students in learning and productivity tasks.

## Applications Overview

1. **Drowsiness Detection**
2. **Question Answering Model Fine-Tuning (LLM)**
3. **YouTube Video Analysis and Quiz Generation**
4. **Text Summarization with T5 Model**

## Demonstration Video

---

## Drowsiness Detection

### Overview

The drowsiness detection script utilizes facial landmark detection and CNNs for real-time analysis of eye status to determine if eyes are open or closed.

### How It Works

1. **Dependencies**:
   - Ensure installation of PIL, face_recognition, opencv-python, tensorflow, scikit-learn, and keras.

2. **Functionality**:
   - Includes functions for eye cropping, image loading, model definition, training, and real-time webcam-based detection.

### Usage

1. Clone the repository.
2. Install required dependencies.
3. Organize open/closed eye images into separate folders.
4. Train the model and run `webcam.py` for real-time detection.

---

## Question Answering Model Fine-Tuning (LLM)

### Overview

This script fine-tunes a QA model using the SQuAD dataset and evaluates performance in FP32, BF16, and TorchScript modes, highlighting benefits of using Intel Extension for PyTorch (IPEX).

### Setup Instructions

1. Install required packages.
2. Configure IPEX.
3. Set up SQuAD dataset, pre-trained model, and tokenizer from Hugging Face Transformers library.

### Usage

1. Ensure dependencies are installed.
2. Run the script in a compatible Python environment.
3. Review output for inference times and speedup comparisons.

### Benchmarking Results
![Benchmarking Results](https://github.com/sivapriya1608/quiz_app_intel/assets/149949660/b15f2874-40c1-4315-9563-2d423c7ae496)

---

## YouTube Video Analysis and Quiz Generation

### Overview

This script extracts YouTube video IDs, retrieves captions using the YouTube Transcript API, generates quiz questions using an LLM, and formats questions.

### Prerequisites

- Install pytube, youtube_transcript_api, and transformers.

### Usage

1. Extract video IDs and captions.
2. Generate quiz questions with LLM.
3. Format questions into a structured quiz.

---

## Text Summarization with T5 Model

### Overview

This script fine-tunes a T5 model on the `billsum` dataset for text summarization, comparing FP32 and BF16 precision.

### Usage

1. Fine-tune T5 on `billsum`.
2. Compare inference performance between FP32 and BF16.

### Benchmarking Results
![Benchmarking Results](https://github.com/sivapriya1608/quiz_app_intel/assets/149949660/aa4c5a0f-df7e-4597-90ab-c75262660d8d)
![download](https://github.com/sivapriya1608/quiz_app_intel/assets/149949660/efd48147-5fe5-4bd0-bf83-306267491496)

---

## Dependencies

- Python 3.x
- PyTorch
- Transformers
- Datasets
- Intel Extension for PyTorch (IPEX)

---
