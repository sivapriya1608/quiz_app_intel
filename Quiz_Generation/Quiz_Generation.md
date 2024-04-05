

## YouTube Video Analysis and Quiz Generation

This script performs the following tasks:

1. Extracts YouTube video IDs from a list of URLs.
2. Retrieves the captions of a given YouTube video using the YouTube Transcript API.
3. Feeds the video captions into an OpenAI Language Model (LLM) to generate quiz questions based on the provided text.
4. Transforms the generated quiz questions into a structured format.

### Prerequisites

Before running the script, ensure you have the following dependencies installed:

- `pytube`: A lightweight, dependency-free Python library (not required for the quiz generation part)
- `youtube_transcript_api`: A Python library for fetching YouTube video transcripts
- `transformers`: Hugging Face's `transformers` library for working with OpenAI's GPT models



### Usage

1. **Extract YouTube Video IDs**:
   
   Replace the URLs in the `urls` list with the desired YouTube video URLs. Run the script to extract the video IDs.

2. **Extract & Transform Video Captions**:
   
   Replace `video_id` with the desired YouTube video ID. Run the script to retrieve and transform the captions.

3. **Feed Video Captions into LLM (OpenAI)**:
   
   This section loads a pre-trained GPT-3.5 model and tokenizes the text. It then prompts the model to generate quiz questions based on the provided text.

4. **Transform Output**:
   
   Finally, the output generated by the LLM is transformed into a structured format suitable for a quiz.

### Notes

- Ensure you have API access enabled for the YouTube Data API v3 if you're planning to fetch video transcripts programmatically.
- The provided code assumes access to an OpenAI GPT model for quiz generation. You'll need proper credentials to access such a model.
- Adjustments may be needed depending on specific requirements or changes in the libraries used.


