import torch # Imports the PyTorch library for machine learning computations.
from transformers import BlipProcessor, BlipForConditionalGeneration # Imports the BLIP model from Hugging Face.

def describe_image(image):
    """
    Generates a text description of the image using a BLIP model.
    
    The BLIP model is a Vision-Language Model that was trained on a massive dataset of
    images and their captions. It takes an image as input and outputs a human-readable
    sentence describing the content of the image. This process is called Image Captioning.
    This module is crucial because it provides the context that the language model needs.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu" # Automatically chooses a GPU if available, otherwise uses the CPU.
    print(f"Using device: {device}")
    
    # These lines load the pre-trained BLIP model and its tokenizer from Hugging Face.
    # The first time this code runs, it downloads the model to your local cache.
    # This is a truly open-weight model, so no login is required.
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)

    # Prepares the image for the model. The processor handles resizing, normalization, etc.
    inputs = processor(images=image, return_tensors="pt").to(device)
    # The model generates a sequence of tokens that form the text description.
    out = model.generate(**inputs, max_new_tokens=50)
    # The processor decodes the tokens back into a readable string.
    description = processor.decode(out[0], skip_special_tokens=True)
    return description