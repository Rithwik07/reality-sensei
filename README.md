🤖 Reality Sensei: An Offline AI Accessibility Assistant with a voice

✨ Project Overview
Reality Sensei is a self-contained, AI-powered accessibility assistant designed to help visually impaired individuals understand their surroundings. It uses computer vision and large language models, all running locally on a personal computer, to capture a scene, describe it, and answer follow-up questions in real-time. This project is a proof of concept for a truly private, offline AI solution.

How It Works
Image Capture: The program takes a picture of the scene using the user's webcam.

Scene Analysis: It uses a local Vision-Language Model (VLM) to analyze the image and generate a detailed text description.

Question-Answering: A local Large Language Model (LLM) then takes this description and a user's spoken question to provide a specific, helpful answer.

Audio Output: The final answer is converted to speech, providing a seamless, hands-free experience.

🚀 Key Features
100% Offline Functionality: No internet connection required after the initial setup. All AI models run on your local machine, ensuring privacy and speed.

Open-Weight Models: Built on top of Salesforce BLIP and Google FLAN-T5, two powerful and truly open-source models.

Real-time Interaction: Designed to provide quick, verbal responses to user queries.

Modular Architecture: The code is cleanly divided into separate components (image_capture.py, scene_analyzer.py, qa_assistant.py) for easy maintenance and future expansion.

🛠️ Installation & Setup
Clone the repository to your local machine:

Bash

git clone https://github.com/Rithwik07/reality-sensei.git
cd reality-sensei
Create and activate a virtual environment:

Bash

python -m venv venv
.\venv\Scripts\activate
Install the required libraries:

Bash

pip install opencv-python pillow transformers torch pyttsx3 accelerate SpeechRecognition pyaudio
▶️ How to Run
Choose one of the following methods to run the application:

1. Text-based Input
This is the standard way to run the program, where you type your question into the terminal.

Bash

python run.py
After the scene description is given, the program will prompt you to type your question.

2. Voice-based Input
For a hands-free experience, use this script. It listens for your question through the microphone.

Bash

python runWithVoices.py
After the scene description is given, the program will prompt you to speak your question.

3. Test Run (Hardcoded Question)
Use this file to quickly test if the entire pipeline is working correctly without any user interaction. It uses a predefined question.

Bash

python testRun.py
📝 Code Structure
The project is organized into logical, single-purpose files:

image_capture.py: Handles webcam access and image saving using OpenCV.

scene_analyzer.py: Contains the BLIP model for generating image captions.

qa_assistant.py: Uses the FLAN-T5 model for question-answering based on the generated description.

run.py, runWithVoices.py, testRun.py: The main scripts that orchestrate the entire workflow and handle user interaction.

🤝 Contributions
Reality Sensei is an open-source project. Contributions are welcome! Feel free to open a pull request or report bugs in the Issues section.

<img src="https://img.shields.io/github/stars/Rithwik07/reality-sensei?style=social&label=Star" alt="GitHub stars">
<img src="https://img.shields.io/github/forks/Rithwik07/reality-sensei?style=social&label=Fork" alt="GitHub forks">
