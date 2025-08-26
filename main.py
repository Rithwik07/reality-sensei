import cv2
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from transformers import pipeline
import pyttsx3

# --- 1. Image Capture ---
def capture_image(file_path="scene.jpg"):
    """Captures a single image from the webcam."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video device.")
        return None
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(file_path, frame)
        print(f"Image captured and saved to {file_path}")
    else:
        print("Error: Could not read frame from camera.")
        return None
    cap.release()
    return Image.open(file_path)

# --- 2. Vision-Language Model for Image Description ---
def describe_image(image):
    """Generates a text description of the image using a BLIP model."""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    
    # Load model and processor. This will download on first run.
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)

    # Generate the description
    inputs = processor(images=image, return_tensors="pt").to(device)
    out = model.generate(**inputs, max_new_tokens=50)
    description = processor.decode(out[0], skip_special_tokens=True)
    return description

# --- 3. Language Model for Answering Questions ---
def answer_question_with_gpt(scene_description, user_question):
    """Uses an open-weight model to answer a question based on a scene description."""
    # Use google/flan-t5-large, a powerful and truly open-weight model.
    # The `text2text-generation` pipeline is correct for this encoder-decoder model.
    qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-large",
                           torch_dtype=torch.float16, device_map="auto")

    # Construct the prompt to ground the answer in the provided context
    prompt_template = (
    f"Extract the number of people from the following sentence. "
    f"Sentence: {scene_description}."
)
    
    # Generate the answer and return the text.
    outputs = qa_pipeline(prompt_template, max_new_tokens=100)
    return outputs[0]['generated_text']

# --- 4. Text-to-Speech Output ---
def speak(text):
    """Converts text to speech and plays it."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# --- Main Program Flow ---
if __name__ == "__main__":
    print("Starting the Accessibility Scene Assistant...")
    speak("I'm ready. Taking a picture now.")
    
    # Capture the image
    captured_image = capture_image()
    if captured_image is None:
        speak("I could not capture an image. Exiting.")
    else:
        # Describe the image
        print("Analyzing the scene...")
        scene_description = describe_image(captured_image)
        print(f"Scene Description: {scene_description}")
        speak(f"The scene shows: {scene_description}")
        
        # This part requires a Speech-to-Text module for a real-time use case.
        # For this example, we'll use a hardcoded question.
        user_question = "How many people are there?"
        print(f"User asks: {user_question}")
        
        # Get the answer from the language model
        print("Answering the question...")
        try:
            answer = answer_question_with_gpt(scene_description, user_question)
            print(f"Answer: {answer}")
            speak(answer)
        except Exception as e:
            print(f"An error occurred while answering the question: {e}")
            speak("I'm sorry, an error occurred while trying to answer that question.")