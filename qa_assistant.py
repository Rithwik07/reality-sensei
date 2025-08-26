from transformers import pipeline # Imports the convenient pipeline function from Hugging Face.
import torch

def answer_question_with_gpt(scene_description, user_question):
    """
    Uses an open-weight language model to answer a question based on a scene description.
    
    This function leverages the Hugging Face `pipeline` for the 'text2text-generation' task.
    It takes the image caption as `context` and the user's query as a `question`. It then
    uses a powerful, pre-trained language model to generate an answer that is grounded
    in the provided context, ensuring the response is accurate to the visual scene.
    """
    # This pipeline automatically handles tokenization, model loading, and text generation.
    # It uses a truly open model that requires no login.
    qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-large",
                           torch_dtype=torch.float16, device_map="auto")
                           
    # This is the prompt template. It's a carefully crafted string that instructs the model
    # to perform a specific task: answer the question using the context.
    # This process is called Prompt Engineering.
    prompt_template = (
        f"Answer the question based on the provided text. Text: {scene_description}. Question: {user_question}."
    )
    
    # The model generates the answer based on the prompt.
    outputs = qa_pipeline(prompt_template, max_new_tokens=100)
    # We extract the generated text from the pipeline's output.
    return outputs[0]['generated_text']