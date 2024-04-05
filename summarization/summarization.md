**Summarization**

**Fine-tuning a T5 model for Text Summarization and Inference Performance Comparison**

This repository contains code for fine-tuning a T5 model using the `billsum` dataset for text summarization and comparing inference performance between floating-point (FP32) and bfloat16 (BF16) precision.


**Usage:**

1. **Fine-tuning T5 Model:**

    a. Install the required libraries by running:
   
   
   
    b. Run the `summarization.ipynb` script to fine-tune the T5 model on the `billsum` dataset for text summarization. The fine-tuned model will be saved in the specified output directory.

2. **Inference Performance Comparison:**

    a. After fine-tuning the model, ensure you have the fine-tuned model and tokenizer saved in the designated directory.

    b. Run the `inference_performance_comparison.py` script to compare the inference performance between FP32 and bfloat16 precision. The script will load the fine-tuned model and tokenizer, perform inference on a sample text, and measure the average inference time over multiple runs.

**Notes:**

- Ensure that you have a compatible GPU device for running the inference performance comparison script. 
- This code is specifically designed for comparing inference performance between FP32 and bfloat16 precision on the CPU. Adjustments may be needed for GPU-based comparisons.
- The `billsum` dataset is used for fine-tuning the T5 model, but you can replace it with any other summarization dataset as needed.

**Dependencies:**

- Python 3.x
- PyTorch
- Transformers
- Datasets
- Intel Extension for PyTorch (IPEX)



**License:**

This project is licensed under the MIT License - see the LICENSE.md file for details.

**Acknowledgments:**

- OpenAI for providing the base T5 model architecture.
- Hugging Face for the Transformers library.
- Intel for providing the Intel Extension for PyTorch (IPEX).

**References:**

- [Link to OpenAI's T5 Model](https://openai.com/research/t5/)
- [Link to Hugging Face's Transformers Library](https://huggingface.co/transformers/)
- [Link to Intel Extension for PyTorch (IPEX)](https://github.com/intel/intel-extension-for-pytorch)