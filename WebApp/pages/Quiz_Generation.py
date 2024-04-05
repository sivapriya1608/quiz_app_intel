import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain

# Initialize the Langchain model
def get_quiz_data(text):
    template = f"""
    You are a helpful assistant programmed to generate questions based on any text provided. For every chunk of text you receive, you're tasked with designing 5 distinct questions. Each of these questions will be accompanied by 3 possible answers: one correct answer and two incorrect ones. 

    For clarity and ease of processing, structure your response in a way that emulates a Python list of lists. 

    Your output should be shaped as follows:

    1. An outer list that contains 5 inner lists.
    2. Each inner list represents a set of question and answers, and contains exactly 4 strings in this order:
    - The generated question.
    - The correct answer.
    - The first incorrect answer.
    - The second incorrect answer.

    Your output should mirror this structure:
    [
        ["Generated Question 1", "Correct Answer 1", "Incorrect Answer 1.1", "Incorrect Answer 1.2"],
        ["Generated Question 2", "Correct Answer 2", "Incorrect Answer 2.1", "Incorrect Answer 2.2"],
        ...
    ]

    It is crucial that you adhere to this format as it's optimized for further Python processing.

    """
    try:
        tokenizer = AutoTokenizer.from_pretrained("Intel/neural-chat-7b-v3-1")
        model = AutoModelForCausalLM.from_pretrained("Intel/neural-chat-7b-v3-1")
        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        human_message_prompt = HumanMessagePromptTemplate.from_template("{text}")
        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )
        chain = LLMChain(
            llm=model,
            tokenizer=tokenizer,
            prompt=chat_prompt,
        )
        return chain.run(text)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.stop()

# Main Streamlit app code
import time  # Import the time module for the delay

# Define the questions, options, correct answers, and explanations

# Initialize variables for score and question index
score = 0

# Add dropdown menu for content selection
st.title("Quiz Time!")
content_type = st.selectbox("Select Content Type:", ["Text", "Youtube Video", "Document"])

# Add content based on selection
if content_type == "Text":
    text_input = st.text_input("Enter Text:")
    if text_input:
        generated_data = get_quiz_data(text_input)
        generated_questions = [question[0] for question in generated_data]
        st.write("Generated Questions:")
        st.write(generated_questions)
elif content_type == "Youtube Video":
    st.text_input("Enter Youtube Video URL:")
elif content_type == "Document":
    uploaded_file = st.file_uploader("Upload Document:", type=['pdf'])

# Add button to generate quiz
if st.button("Generate Quiz"):
    with st.spinner("Generating Quiz..."):  # Display a spinner while generating the quiz
        
        for i in range(len(questions)):
            st.header(f"Question {i + 1}: {questions[i]}")
            options_list = options[i]
            selected_option = st.radio(f"Select an option for Question {i + 1}:", options_list)
            if selected_option == correct_answers[i]:
                score += 1
                st.success("Correct!")
            else:
                st.error("Incorrect!")
            st.write(f"Explanation: {explanations[i]}")

        st.title("Quiz Completed!")
        st.write(f"You scored {score} out of {len(questions)}.")
