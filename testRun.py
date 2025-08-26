from image_capture import capture_image # Imports the image capture function.
from scene_analyzer import describe_image # Imports the image description function.
from qa_assistant import answer_question_with_gpt # Imports the question-answering function.
import pyttsx3 # Imports the text-to-speech library.

def speak(text):
    """Converts text to speech and plays it."""
    engine = pyttsx3.init() # Initializes the TTS engine.
    engine.say(text) # Queues the text to be spoken.
    engine.runAndWait() # Waits for the speech to complete before the program continues.

if __name__ == "__main__":
    # This ensures the code inside the block only runs when the script is executed directly.
    # It acts as the starting point of your program.
    print("Starting the Accessibility Scene Assistant...")
    speak("I'm ready. Taking a picture now.")
    
    # The program flow:
    # 1. Capture the image.
    captured_image = capture_image()
    if captured_image is None:
        speak("I could not capture an image. Exiting.")
    else:
        # 2. Describe the scene using the BLIP model.
        print("Analyzing the scene...")
        scene_description = describe_image(captured_image)
        print(f"Scene Description: {scene_description}")
        speak(f"The scene shows: {scene_description}")
        
        # 3. Simulate a user's question. In a real app, this would be a Speech-to-Text input.
        user_question = "How many people are there?"
        print(f"User asks: {user_question}")
        
        # 4. Use the FLAN-T5 model to answer the question.
        print("Answering the question...")
        try:
            answer = answer_question_with_gpt(scene_description, user_question)
            print(f"Answer: {answer}")
            speak(answer)
        except Exception as e:
            # Handles any errors that might occur during the process.
            print(f"An error occurred while answering the question: {e}")
            speak("I'm sorry, an error occurred while trying to answer that question.")