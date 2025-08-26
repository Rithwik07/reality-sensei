from image_capture import capture_image
from scene_analyzer import describe_image
from qa_assistant import answer_question_with_gpt
import pyttsx3
import speech_recognition as sr # The correct import for speech recognition

def speak(text):
    """Converts text to speech and plays it."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
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
        speak(f"The scene shows: {scene_description}. Please ask your question now.")
        
        # --- Listen for the user's question ---
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening for a question...")
            audio = r.listen(source, timeout=5) # Listens for 5 seconds

        user_question = ""
        try:
            # Uses Google's Web Speech API to recognize the audio.
            user_question = r.recognize_google(audio)
            print(f"User asks: {user_question}")
        except sr.UnknownValueError:
            print("Could not understand audio.")
            speak("I'm sorry, I could not understand your question.")
            exit()
        except sr.RequestError as e:
            print(f"Could not request results from service: {e}")
            speak("I'm sorry, I could not access the speech recognition service.")
            exit()
        
        print("Answering the question...")
        try:
            answer = answer_question_with_gpt(scene_description, user_question)
            print(f"Answer: {answer}")
            speak(answer)
        except Exception as e:
            # Handles any errors that might occur during the process.
            print(f"An error occurred while answering the question: {e}")
            speak("I'm sorry, an error occurred while trying to answer that question.")